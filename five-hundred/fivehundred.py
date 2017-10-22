from account import *
from bid import Bid
from deck import Deck

from collections import OrderedDict

# TODO list
# - it might be better to define some 500-specific exceptions, e.g. NotPlayersTurnError, CardNotPosessedError, etc.
# - docstrings

class Player:
	def __init__(self, account):
		self.account = account

	def __str__(self):
		return self.account.username

	def __repr__(self):
		return f'Player({self.account.uuid})'

	def __eq__(self, other):
		return type(other) is Player and self.account.uuid == other.account.uuid

	def __ne__(self, other):
		return not self.__eq__(other)

class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

	def __str__(self):
		return 'Players: ' + ', '.join([str(player.account) for player in self.players]) + '\n'
			+ 'Score: ' + str(self.score)

	def __repr__(self):
		return 'Team(players=[' + ', '.join([player.account.uuid for player in self.players]) + f'], score={self.score})'

class Kitty:
	def __init__(self, cards=None):
		self.cards = cards or []
		self.collected = False

	def append(self, value):
		self.cards.append(value)

	def collect_cards(self):
		if len(self.cards) < 3:
			raise ValueError(f'Kitty cannot be collected until it has all 3 cards')

		cards, self.cards = self.cards, []
		self.collected = True
		return cards

	def __str__(self):
		return ', '.join([str(card) for card in self.cards]) + ' (' + ('' if self.collected else 'un') + 'collected)'

	def __repr__(self):
		return 'Kitty(cards=[' + ', '.join([card.to_minimal_string() for card in self.cards]) + f'], collected={self.collected})

class Trick:
	def __init__(self, leader):
		self.leader = leader
		self.cards = []

	def __str__(self):
		return f'Leader: {self.leader}\n'
			+ 'Cards: ' + ', '.join([str(card) for card in self.cards])

	def __repr__(self):
		return f'Trick(leader={self.leader}, cards=[' + ', '.join([card.to_minimal_str() for card in self.cards]) + '])'

class Hand:
	def __init__(self, dealer, player_ids):
		self.dealer = dealer
		self.deck = Deck()
		self.hands = OrderedDict({ player_id: [] for player_id in player_ids + [dealer]})   # TODO: maybe convert this to a json.dump compatible format
		self.kitty = None
		self.bids = []
		self.tricks = []

		self.deal()

	def deal(self):
		self.deck.shuffle()

		# Yeah, I know, there's no point following the dealing order. It just feels better this way.

		for player_id, hand in self.hands:
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty = Kitty()
		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands:
			for _ in range(4):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands:
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

	def __str__(self):
		return 'Bids:' + '\n  '.join([str(bid) for bid in self.bids]) + '\nTricks:' + '\n  '.join([str(trick) for trick in self.tricks])

	def bidding_is_concluded(self):
		# TODO: remove these notes when everthing is a-ok good to go
		# yes conditions:
		# 4 passes
		# normal bid + 3 passes
		# hit bidding ceiling (10 no trumps)

		enough_passes = len(self.bids) == 4 and self.bids.count(Bid('PASS')) >= 3
		bid_ceiling = len(self.bids) > 0 and self.bids[-1] == Bid('10', 'NO_TRUMPS')

		return enough_passes or bid_ceiling

	def hand_is_concluded(self):
		# yes conditions:
		# 4 passes
		# 10 tricks complete
		# misere/open misere bidder wins a trick

		if not self.bidding_is_concluded():   # this check allows safe usage of self.winning_bid
			return False

		four_passes = self.bids.count(Bid('PASS')) == 4
		ten_tricks_complete = len(self.tricks) == 10
		misere_won_trick = self.winning_bid() in { Bid('MISERE'), BID('OPEN_MISERE') }

		return four_passes or ten_tricks_complete or misere_won_trick

	def winning_bid(self):
		# if bidding not concluded throw error
		# return last non-pass item of self.bids

		if not self.bidding_is_concluded():
			raise ValueError('Winning bid is unknown because bidding is not yet concluded')

		if self.bids.count(Bid('PASS')) == 4:
			return None

		return [bid for bid in self.bids if bid != Bid('PASS')][-1]

	def trick_is_concluded(self, trick_index):
		# check length of trick at index
		# if winning bid is open misere, concluded = len == 3
		# else, concluded = len == 4

		return len(self.tricks[trick_index].cards) == (3 if self.winning_bid() in { Bid('MISERE'), Bid('OPEN_MISERE') } else 4)

	def trick_winner():
		# TODO

	def last_normal_bid(self):
		normal_bids = [ bid for bid in self.bids if not bid == Bid('PASS') ]
		return normal_bids[-1] if normal_bids else None

	def accept_bid(self, bid):
		# if hand concluded throw error
		# if bidding concluded throw error
		# if it's not the player's turn throw error
		# if the bid isn't allowed throw error
		#   bid greater than previous
		#   if misere, required threshold of past bids is met

		if self.hand_is_concluded():
			raise ValueError('Hand is concluded')

		if self.bidding_is_concluded():
			raise ValueError('Bidding is concluded')

		if not self.next_player() == bid.player_id:
			raise ValueError('It is not the given player\'s turn')

		# make sure new bid is higher than the last one
		if not bid > self.last_normal_bid():
			raise ValueError('New Bid must be higher than previous bid')

		# if the bid is misere, make sure that a 7 bid has been made
		if bid == Bid('MISERE') and not self.last_normal_bid() >= Bid('SEVEN', 'SPADES'):
			raise ValueError('Misere cannot be bid until a 7 Bid has been made')

		# the bid is valid
		self.bids.append(bid)


	def accept_card(self, player_id, card):
		# TODO
		# if hand concluded throw error
		# if bidding not concluded throw error

		# validate
		#   is it that player's turn (and are they playing (not partner's misere))
		#   do they have that card in their hand
		#   are they allowed to play that card
		# record

	def next_player(self):
		if self.hand_is_concluded():
			return None

		player_circle = [ player_id for player_id in self.hands.keys() ]

		if not self.bidding_is_concluded():
			# working this out is more complicated and more manual than I'd like;
			# there might be a better formulaic method that I didn't come up with

			player_pointer = 0

			for bid in self.bids:

				if bid == Bid('PASS'):
					# remove the player who passed from player_circle 
					del player_circle[player_pointer]

					# if the player_pointer was pointing to the end of the list, it should now point to the beginning
					if player_pointer == len(player_circle):
						player_pointer = 0

				else:
					# move the player_pointer around the circle 1 space
					player_pointer = (player_pointer + i) % len(player_circle)

			return player_circle[player_pointer]

		else:
			current_trick = self.tricks[-1]

			# next player is at (index of trick leader + number of cards played in current trick) % player count

			trick_leader_index = player_circle.index(self.tricks[-2].trick_winner()) if len(self.tricks) > 1 else 0
			cards_played_this_trick = len(current_trick.cards)

			return player_circle[len(current_trick.cards) % len(player_circle)]


class FiveHundredGame:
	def __init__(self, teams):
		self.teams = teams
		self.spectators = []
		self.hands = []

	def get_player(self, player_id):
		for team in self.teams:
			for player in team.players:
				if player.id == player_id:
					return player
		return None
