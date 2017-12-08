import bid

class CardRank:
	ranks = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

	def __init__(self, rank):
		if not type(rank) == str:
			raise ValueError('CardRank argument must be a string')

		rank = rank.upper()

		if not rank in CardRank.ranks:
			raise ValueError(f'"{rank}" is not a valid card rank')

		self.rank = rank

	def to_string(self):
		return self.rank.title()

	def to_minimal_string(self):
		str_to_int = {
			'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9
		}

		if self.rank in str_to_int:
			return str(str_to_int[self.rank])
		else:
			return self.rank[0].upper()

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		return f'CardRank({self.rank})'

	def __eq__(self, other):
		# Rank to Rank comparison - e.g. rank == other_rank
		if type(other) is CardRank:
			return self.rank == other.rank

		# Rank to string comparison - e.g. rank == 'QUEEN'
		if type(other) is str:
			return self.rank == other.upper()

		return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def _compare(self, op, other):
		if not type(other) == CardRank:
			raise TypeError(f'\'{op}\' not supported between instances of \'CardRank\' and \'{type(other)}\'')

		left = CardRank.ranks.index(self.rank)
		right = CardRank.ranks.index(other.rank)

		operator_map = {
			'>': left > right,
			'<': left < right,
			'>=': left >= right,
			'<=': left <= right
		}

		if not op in operator_map.keys():
			raise ValueError(f'Unknown comparison operator: \'{op}\'')

		return operator_map[op]

	def __gt__(self, other):
		return self._compare('>', other)

	def __lt__(self, other):
		return self._compare('<', other)

	def __ge__(self, other):
		return self._compare('>=', other)

	def __le__(self, other):
		return self._compare('<=', other)

class CardSuit:
	suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'JOKER']

	def __init__(self, suit):
		if not type(suit) == str:
			raise ValueError('CardSuit argument must be a string')

		suit = suit.upper()

		if not suit in CardSuit.suits:
			raise ValueError(f'"{suit}" is not a valid card suit')

		self.suit = suit

	def to_string(self):
		return self.suit.title()

	def to_minimal_string(self):
		return self.suit[0].upper()

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		return f'CardSuit({self.suit})'

	def __eq__(self, other):
		# Suit to Suit comparison - e.g. suit == other_suit
		if type(other) is CardSuit or type(other) is bid.BidSuit:
			return self.suit == other.suit

		# Suit to string comparison - e.g. suit == 'HEARTS'
		if type(other) is str:
			return self.suit == other.upper()

		return False

	def __ne__(self, other):
		return not self.__eq__(other)

class Card:
	def __init__(self, suit, rank=None):
		self.suit = CardSuit(suit)

		if self.suit == 'JOKER' and rank is not None:
			raise ValueError('Jokers cannot be instantiated with a rank')
		elif self.suit != 'JOKER':
			self.rank = CardRank(rank)

	def is_joker(self):
		return self.suit == 'JOKER'

	def to_string(self):
		if self.suit == 'joker':
			return 'Joker'
		else:
			return f'{self.rank} of {self.suit}'

	def to_minimal_string(self):
		if self.suit == 'joker':
			return 'J-'
		else:
			return self.rank.to_minimal_string() + self.suit.to_minimal_string()

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		if self.suit == 'joker':
			return 'Card(JOKER)'
		else:
			return f'Card({self.suit.suit}, {self.rank.rank})'

	def __eq__(self, other):
		return type(other) == Card and hash(self) == hash(other)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return int.from_bytes(self.to_minimal_string().encode(), 'little')
		# https://stackoverflow.com/a/31702461/4809728
