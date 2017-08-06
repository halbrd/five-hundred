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

	def __eq__(self, other):
		# Rank to Rank comparison - e.g. rank == other_rank
		if type(other) is CardRank:
			return self.rank == other.rank

		# Rank to string comparison - e.g. rank == 'QUEEN'
		if type(other) is str:
			return self.rank == other

		return False

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

	def __eq__(self, other):
		# Suit to Suit comparison - e.g. suit == other_suit
		if type(other) is CardSuit or type(other) is BidSuit:
			return self.suit == other.suit

		# Suit to string comparison - e.g. suit == 'HEARTS'
		if type(other) is str:
			return self.suit == other.upper()

		return False

class Card:
	def __init__(self, rank, suit):
		self.rank = CardRank(rank)
		self.suit = CardSuit(suit)

	def to_string(self):
		return f'{self.rank} of {self.suit}'

	def to_minimal_string(self):
		return self.rank.to_minimal_str() + self.suit.to_minimal_str()

	def __str__(self):
		return self.to_string()

	def __eq__(self, other):
	return type(other) == Card and self.suit == other.suit and self.rank == other.rank
