import random

class CardSuit:
	suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'JOKER']

	def __init__(self, suit):
		suit = suit.upper()

		if not suit in CardSuit.suits:
			raise ValueError(f'"{suit}" is not a valid card suit')
		else:
			self.suit = suit

	def to_string(self):
		return self.suit.title()

	def to_minimal_string(self):
		return self.suit[0].upper()

	def __str__(self):
		return self.to_string()

class CardRank:
	ranks = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']

	def __init__(self, rank):
		rank = rank.upper()

		if not rank in CardRank.ranks:
			raise ValueError(f'"{rank}" is not a valid card rank')
		else:
			self.rank = rank

	def to_string(self):
		return self.rank.title()

	def to_minimal_string(self):
		return self.rank[0].upper()

	def __str__(self):
		return self.to_string()

class BidSuit:
	suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'NO_TRUMPS', 'MISERE', 'OPEN_MISERE', 'PASS']

	def __init__(self, suit):
		suit = suit.upper().replace(' ', '_')

		if not suit in BidSuit.suits:
			raise ValueError(f'"{suit}" is not a valid bid suit')
		else:
			self.suit = suit

	def to_string(self):
		return self.suit.replace('_', ' ').title()

	def to_minimal_string(self):
		return self.suit[0].upper()

	def __str__(self):
		return self.to_string()

class BidValue:
	values = [6, 7, 8, 9, 10]

	def __init__(self, value):
		if not value in BidValue.values:
			raise ValueError(f'"{value}" is not a valid bid value')
		else:
			self.value = value

	def to_string(self):
		return str(self.value)

	def to_minimal_string(self):
		return self.to_string()

	def __str__(self):
		return self.to_string()

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def to_string(self):
		return str(self.rank) + ' of ' + str(self.suit)

	def to_minimal_str(self):
		return self.rank.to_minimal_str() + self.suit.to_minimal_str()

	def __str__(self):
		return self.to_string()

class Deck:
	def __init__(self):
		self.cards = []
		self.new_deck()

	def new_deck(self):
		self.cards = []

		# # Generate full deck
		# for suit in list(Suits).remove(Suit.JOKER):
		# 	for rank in Ranks:
		# 		self.cards.append(Card(suit, rank))
		#
		# # Add Joker
		# self.cards.append(Card(Suit.JOKER, None))
		#
		# # Remove unused cards
		# def is_unused(card):
		# 	return card.rank in { Rank.TWO, Rank.THREE } or card.rank == Rank.FOUR and card.suit in { Suit.CLUBS, Suit.SPADES }
		# self.cards = [ card for card in self.cards if not is_unused(card) ]

	def shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		index = random.randint(0, len(self.cards) - 1)
		card = self.cards[index]
		del self.cards[index]
		return card

class Player:
	def __init__(self, name):
		self.name = name

class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

class Bid:
	def __init__(self, player, value, suit):
		self.player = player
		self.value = value
		self.suit = suit

class Kitty:
	def __init__(self, cards):
		self.cards = cards

class Trick:
	def __init__(self, leader, cards):
		self.leader = leader
		self.cards = []

class Hand:
	def __init__(self, dealer, hands, kitty):
		self.dealer = dealer
		self.hands = hands
		self.kitty = kitty
		self.bids = []
		self.tricks = []

class Game:
	def __init__(self, teams):
		self.teams = teams
		self.hands = []


###################################################


normal_card = Card('SPADES', 'FIVE')
print(str(normal_card))
print(normal_card.minimal_str())

joker_card = Card('JOKER', 'ACE')
print(str(joker_card))
print(joker_card.minimal_str())

wtf_card2 = Card('asdasdadad', 'ACE')
print(str(wtf_card2))
print(wtf_card2.minimal_str())
