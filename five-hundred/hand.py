from bid import Bid
from card import Card
from deck import Deck
from kitty import Kitty

from collections import OrderedDict

class GameStateException(Exception):
	pass

class BiddingConcludedError(GameStateException):
	def __init__(self, message='Cannot perform action because bidding is concluded'):
		super().__init__(message)

class BiddingNotConcludedError(GameStateException):
	def __init__(self, message='Cannot perform action because bidding is not concluded'):
		super().__init__(message)

class TrickConcludedError(GameStateException):
	def __init__(self, message='Cannot perform action because trick is concluded'):
		super().__init__(message)

class TrickNotConcludedError(GameStateException):
	def __init__(self, message='Cannot perform action because trick is not concluded'):
		super().__init__(message)

class HandConcludedError(GameStateException):
	def __init__(self, message='Cannot perform action because hand is concluded'):
		super().__init__(message)

class HandNotConcludedError(GameStateException):
	def __init__(self, message='Cannot perform action because hand is not concluded'):
		super().__init__(message)

class OutOfTurnError(GameStateException):
	def __init__(self, message='Cannot perform action because it is another player\'s turn'):
		super().__init__(message)

class CardNotPossessedError(GameStateException):
	def __init__(self, message='Cannot perform action because the player does not posess the given card'):
		super().__init__(message)

class CardNotAllowedError(GameStateException):
	def __init__(self, message='Cannot perform action because the player is not allowed to play the given card'):
		super().__init__(message)


def check_bidding_concluded(state=True):
	def check(function):
		def wrapper(*args, **kwargs):
			self = args[0]

			if self.bidding_is_concluded() != state:
				if state:   # bidding should be concluded but isn't
					raise BiddingNotConcludedError
				else:   # bidding shouldn't be concluded but is
					raise BiddingConcludedError

			function(*args, **kwargs)
		return wrapper
	return check

def check_trick_concluded(state=True):
	def check(function):
		def wrapper(*args, **kwargs):
			self = args[0]
			trick_index = args[1]

			trick = self.tricks[trick_index]
			if self.trick_is_concluded(trick_index) != state:
				if state:   # trick should be concluded but isn't
					raise TrickNotConcludedError
				else:   # trick shouldn't be concluded but is
					raise TrickConcludedError

			function(*args, **kwargs)
		return wrapper
	return check

def check_hand_concluded(state=True):
	def check(function):
		def wrapper(*args, **kwargs):
			self = args[0]

			if self.hand_is_concluded() != state:
				if state:   # hand should be concluded but isn't
					raise HandNotConcludedError
				else:   # hand shouldn't be concluded but is
					raise HandConcludedError

			function(*args, **kwargs)
		return wrapper
	return check

class Hand:
	def __init__(self, player_ids, deal=True):
		self.dealer_id = player_ids[-1]
		self.deck = Deck()
		self.deck.shuffle()
		self.hands = OrderedDict({ player_id: [] for player_id in player_ids })
		self.kitty = None
		self.bids = []
		self.tricks = []

		if deal:
			self.deal()

	def __str__(self):
		return 'Bids:' + ('\n  ' if len(self.bids) > 0 else '') \
		+ '\n  '.join([str(bid) for bid in self.bids]) \
		+ '\nTricks:' + ('\n  ' if len(self.tricks) > 0 else '') \
		+ '\n  '.join([str(trick) for trick in self.tricks])

	def deal(self):
		# Yeah, I know, there's no point following the dealing order. It just feels better this way.

		for player_id, hand in self.hands.items():
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty = Kitty()
		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands.items():
			for _ in range(4):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands.items():
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

	def bidding_is_concluded(self):
		# TODO: remove these notes when everthing is a-ok good to go
		# yes conditions:
		# 4 passes
		# normal bid + 3 passes
		# hit bidding ceiling (10 no trumps)

		enough_passes = len(self.bids) == 4 and self.bids.count(Bid('PASS')) >= 3
		bid_ceiling = len(self.bids) > 0 and self.bids[-1] == Bid('NO_TRUMPS', '10')

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

	@check_bidding_concluded
	def winning_bid(self):
		# if bidding not concluded throw error
		# return last non-pass item of self.bids

		if self.bids.count(Bid('PASS')) == 4:
			return None

		return [bid for bid in self.bids if bid != Bid('PASS')][-1]

	def trick_is_concluded(self, trick_index):
		# check length of trick at index
		# if winning bid is open misere, concluded = len == 3
		# else, concluded = len == 4

		return len(self.tricks[trick_index].cards) == (3 if self.winning_bid() in { Bid('MISERE'), Bid('OPEN_MISERE') } else 4)

	@check_bidding_concluded
	@check_trick_concluded
	def trick_winner(self, trick_index):
		if len(self.tricks) - 1 > trick_index:
			raise ValueError(f'Trick {trick_index} does not exist')

		if not self.trick_is_concluded(trick_index):
			raise ValueError(f'Trick {trick_index} is not concluded')

		trick = self.tricks[trick_index]

		def highest_trump(trump, cards):
			if Card('JOKER') in cards:
				return Card('JOKER')

			# if the Joker was played, then the function has already returned, so we can safely access card.suit
			trumps = [ card for card in cards if card.suit == trump ]

			if not trumps:
				return None

			return max(trumps, key=lambda card: card.rank)

		def highest_non_trump(trump, cards):
			non_trumps = [ card for card in cards if not card.is_joker() and not card.suit == trump ]

			return max(non_trumps, key=lambda card: card.rank)

		bid = self.winning_bid()
		if bid in { Bid('MISERE'), Bid('OPEN_MISERE') } or bid.suit == 'NO_TRUMPS':
			trump = None
		else:
			trump = bid.suit

		# time to figure out who won this thing
		winning_card = highest_trump(trump, trick.cards) or highest_non_trump(trump, trick.cards)
		winning_index = trick.cards.index(winning_card)

		# the winning player will be the player who is winning_index places to the left of the trick leader
		# this means that the winning player will be (number of places between the bid winner and the trick leader + winning_index) to the left of the bid winner
		if trick_index == 0:
			trick_leader = self.winning_bid().player_id
		else:
			trick_leader = self.trick_winner(trick_index - 1)
		trick_leader_index = self.hands.keys().index(trick_leader)

		winning_player = self.hands.keys()[ (trick_leader_index + winning_index) % len(self.hands.keys()) ]
		return winning_player

	def last_normal_bid(self):
		normal_bids = [ bid for bid in self.bids if not bid == Bid('PASS') ]
		return normal_bids[-1] if normal_bids else None

	@check_hand_concluded(state=False)
	@check_bidding_concluded(state=False)
	def accept_bid(self, bid):
		# if hand concluded throw error
		# if bidding concluded throw error
		# if it's not the player's turn throw error
		# if the bid isn't allowed throw error
		#   bid greater than previous
		#   if misere, required threshold of past bids is met

		if not self.next_player() == bid.player_id:
			raise OutOfTurnError

		# make sure new bid is higher than the last one
		if not ( bid == Bid('PASS')
		  or self.last_normal_bid() is None
		  or bid > self.last_normal_bid() ):
			raise ValueError('New Bid must be higher than previous bid')

		# if the bid is misere, make sure that a 7 bid has been made
		if bid == Bid('MISERE') and not self.last_normal_bid() >= Bid('SPADES', '7'):
			raise ValueError('Misere cannot be bid until a 7 Bid has been made')

		# the bid is valid
		self.bids.append(bid)

		# if this was the last bid, start the first trick
		if self.bidding_is_concluded():
			self.tricks.append(Trick(self.winning_bid().player_id))

	@check_hand_concluded(state=False)
	@check_bidding_concluded(state=False)
	def accept_card(self, card, player_id):
		# TODO
		# if hand concluded throw error
		# if bidding not concluded throw error

		# validate
		#   is it that player's turn (and are they playing (not partner's misere))
		#   do they have that card in their hand
		#   are they allowed to play that card
		# record

		if not self.next_player() == player_id:
			raise OutOfTurnError

		if not self.player_has_card(player_id, card):
			raise CardNotPossessedError

		if not self.card_can_be_played(player_id, card):
			raise CardNotAllowedError

		# card can be played
		self.tricks[-1].append(self.hands[player_id].pop(card))

		# check if this was the last card of the trick - if so, prepare the next trick
		if len(self.tricks[-1].cards) == len(self.hands):
			self.tricks.append(Trick(self.trick_winner(len(self.tricks) - 1)))

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
					player_pointer = (player_pointer + 1) % len(player_circle)

			return player_circle[player_pointer]

		else:
			current_trick = self.tricks[-1]

			# next player is at (index of trick leader + number of cards played in current trick) % player count

			trick_leader_index = player_circle.index(self.tricks[-2].trick_winner()) if len(self.tricks) > 1 else 0
			cards_played_this_trick = len(current_trick.cards)

			return player_circle[len(current_trick.cards) % len(player_circle)]

	def player_index(self, player_id):
		try:
			return self.hands.keys().index(player_id)
		except ValueError:
			return None

	def player_has_card(self, player_id, card):
		return card in self.hands[player_id]

	@check_hand_concluded(state=False)
	@check_bidding_concluded
	def card_can_be_played(self, player_id, card):
		current_trick = self.tricks[-1]

		if self.next_player() != player_id:
			return False

		if len(current_trick.cards) == 0:   # player is leading, so anything can be played
			return True
		else:   # player is not leading, so we have to check if they're following suit (and at least one edge case rule)
			led_suit = current_trick.cards[0].suit
			player_can_follow_suit = len([ card for card in self.hands[player_id] if card.suit == led_suit ]) > 0

			# if other team won bidding with misere/open misere, and the player can't follow suit, and the player has the Joker, they must play it
			if self.winning_bid() in { Bid('MISERE'), BID('OPEN_MISERE') } and not self.are_teammates(self.winning_bid().player_id, player_id) and not player_can_follow_suit and Card('JOKER') in self.hands[player_id] and not card == Card('JOKER'):
				return False

			# make sure the player follows suit if they can
			return card.suit == led_suit or not player_can_follow_suit


	def are_teammates(self, player1_id, player2_id):
		try:
			player1_index = self.hands.keys().index(player1_id)
			player2_index = self.hands.keys().index(player2_id)
		except KeyError:
			raise ValueError('One or both players do not exist')

		return player1_index % 2 == player2_index % 2
