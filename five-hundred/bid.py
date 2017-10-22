class BidValue:
	values = ['6', '7', '8', '9', '10']

	def __init__(self, value):
		if type(value) == int:
			value = str(value)

		if not value in BidValue.values:
			raise ValueError(f'"{value}" is not a valid bid value')

		self.value = value

	def to_string(self):
		return str(self.value)

	def to_minimal_string(self):
		return str(self.value)[0]

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		return f'BidValue({self.value})'

	def __eq__(self, other):
		# Value to Value comparison - e.g. value == other_value
		if type(other) is BidValue:
			return self.value == other.value

		# Value to str comparison - e.g. value == '8'
		if type(other) is str:
			return self.value == other.upper()

		# Value to int comparison - e.g. value == 8
		if type(other) is int:
			return int(self.value) == other

		return False

	def __ne__(self, other):
		return not self.__eq__(other)

class BidSuit:
	dependent_suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'NO_TRUMPS']
	independent_suits = ['MISERE', 'OPEN_MISERE', 'PASS']
	suits = dependent_suits + independent_suits

	def __init__(self, suit):
		if not type(suit) == str:
			raise ValueError('BidSuit argument must be a string')

		suit = suit.upper()

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

	def __repr__(self):
		return f'BidSuit({self.suit})'

	def __eq__(self, other):
		# Suit to Suit comparison - e.g. suit == other_suit
		if type(other) is BidSuit or type(other) is CardSuit:
			return self.suit == other.suit

		# Suit to string comparison - e.g. suit == 'HEARTS'
		if type(other) is str:
			return self.suit == other.upper()

		return False

	def __ne__(self, other):
		return not self.__eq__(other)

class Bid:
	def __init__(self, input1, input2=None, player_id=None):
		# argument names can't be specific (eg. value, suit) to remain accurate with flexible inputs
		# eg. ('6', 'NO_TRUMPS'), ('MISERE')
		self.player_id = player_id

		if input1 in BidSuit.independent_suits and input2 is None:
			self.suit = BidSuit(input1)
		elif input1 in BidSuit.independent_suits:
			raise ValueError('Independent suits cannot be instantiated with a value')
		else:
			self.value = BidValue(input1)
			self.suit = BidSuit(input2)

	def to_string(self):
		if self.suit in BidSuit.independent_suits:
			return f'{self.player_id}: {self.suit}'
		else:
			return f'{self.player_id}: {self.value} {self.suit}'

	def to_minimal_string(self):
		if self.suit in BidSuit.independent_suits:
			return self.suit.to_minimal_string() + ' '
		else:
			return self.value.to_minimal_string() + self.suit.to_minimal_string()

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		return f'Bid(player_id={self.player_id}, {self.value.value} {self.suit.suit})'

	def __eq__(self, other):
		return type(other) == Bid and self.value == other.value and self.suit == other.suit

	def __ne__(self, other):
		return not self.__eq__(other)

	def strict_equals(self, other):
		return type(other) == Bid and self.player_id == other.player_id and self.value == other.value and self.suit == other.suit

	def _compare(self, other):
		hierarchy = [
			Bid('6', 'SPADES'), Bid('6', 'CLUBS'), Bid('6', 'DIAMONDS'), Bid('6', 'HEARTS'), Bid('6', 'NO_TRUMPS'),
			Bid('7', 'SPADES'), Bid('7', 'CLUBS'), Bid('7', 'DIAMONDS'), Bid('7', 'HEARTS'), Bid('7', 'NO_TRUMPS'),
			Bid('MISERE'),
			Bid('8', 'SPADES'), Bid('8', 'CLUBS'), Bid('8', 'DIAMONDS'), Bid('8', 'HEARTS'), Bid('8', 'NO_TRUMPS'),
			Bid('9', 'SPADES'), Bid('9', 'CLUBS'), Bid('9', 'DIAMONDS'), Bid('9', 'HEARTS'), Bid('9', 'NO_TRUMPS'),
			Bid('10', 'SPADES'), Bid('10', 'CLUBS'), Bid('10', 'DIAMONDS'),
			Bid('OPEN_MISERE'),
			Bid('10', 'HEARTS'), Bid('10', 'NO_TRUMPS')
		]

		if not self in hierarchy:
			raise ValueError(repr(self) + ' is not a valid Bid')

		if not other in hierarchy:
			raise ValueError(repr(other) + ' is not a valid Bid')

		# I don't like using string codes, but if you have a better idea for how to represent ternary values, I'm all ears
		if hierarchy.index(self) > hierarchy.index(other):
			return '>'
		elif hierarchy.index(self) < hierarchy.index(other):
			return '<'
		else:
			return '='

	def __gt__(self, other):
		if other is None:   # any bid is bigger than no bid
			return True

		if not type(other) == Bid:
			raise TypeError(f'\'>\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) == '>'

	def __lt__(self, other):
		if other is None:   # any bid is bigger than no bid
			return False

		if not type(other) == Bid:
			raise TypeError(f'\'<\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) == '<'

	def __ge__(self, other):
		if other is None:   # any bid is bigger than no bid
			return True

		if not type(other) == Bid:
			raise TypeError(f'\'>=\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) in { '>', '=' }

	def __le__(self, other):
		if other is None:   # any bid is bigger than no bid
			return False

		if not type(other) == Bid:
			raise TypeError(f'\'<=\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) in { '<', '=' }
