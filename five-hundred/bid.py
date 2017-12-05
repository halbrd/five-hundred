import card

class BidValue:
	values = ['6', '7', '8', '9', '10']

	def __init__(self, value):
		value = str(value)

		if not value in BidValue.values:
			raise ValueError(f'"{value}" is not a valid bid value')

		self.value = value

	def to_string(self):
		return str(self.value)

	def to_minimal_string(self):
		if self.value == '10':
			return 'T'
		else:
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

	def __repr__(self):
		return f'BidSuit({self.suit})'

	def __eq__(self, other):
		# Suit to Suit comparison - e.g. suit == other_suit
		if type(other) is BidSuit or type(other) is card.CardSuit:
			return self.suit == other.suit

		# Suit to string comparison - e.g. suit == 'HEARTS'
		if type(other) is str:
			return self.suit == other.upper()

		return False

	def __ne__(self, other):
		return not self.__eq__(other)

class Bid:
	def __init__(self, suit, value=None, player_id=None):
		self.player_id = player_id

		suit = str(suit).upper().replace(' ', '_')

		if suit in BidSuit.independent_suits and value is None:
			self.suit = BidSuit(suit)
		elif suit in BidSuit.independent_suits:
			raise ValueError('Independent suits cannot be instantiated with a value')
		else:
			self.suit = BidSuit(suit)
			self.value = BidValue(value)

	def to_string(self):
		if self.suit in BidSuit.independent_suits:
			r = str(self.suit)
		else:
			r = f'{self.value} {self.suit}'

		if self.player_id is not None:
			r = f'{self.player_id}: {r}'

		return r

	def to_minimal_string(self):
		if self.suit in BidSuit.independent_suits:
			return self.suit.to_minimal_string() + '-'
		else:
			return self.value.to_minimal_string() + self.suit.to_minimal_string()

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		if self.suit in BidSuit.independent_suits:
			return f'Bid({self.suit.suit}, player_id={self.player_id})'
		else:
			return f'Bid({self.suit.suit}, {self.value.value}, player_id={self.player_id})'

	def __eq__(self, other):
		both_have_no_value = not hasattr(self, 'value') and not hasattr(other, 'value')

		return type(other) == Bid \
			and self.suit == other.suit \
			and ( both_have_no_value or self.value == other.value )

	def __ne__(self, other):
		return not self.__eq__(other)

	def strict_equals(self, other):
		return self.__eq__(other) and self.player_id == other.player_id

	def _compare(self, other):
		hierarchy = [
			Bid('PASS'),
			Bid('SPADES', '6'), Bid('CLUBS', '6'), Bid('DIAMONDS', '6'), Bid('HEARTS', '6'), Bid('NO_TRUMPS', '6'),
			Bid('SPADES', '7'), Bid('CLUBS', '7'), Bid('DIAMONDS', '7'), Bid('HEARTS', '7'), Bid('NO_TRUMPS', '7'),
			Bid('MISERE'),
			Bid('SPADES', '8'), Bid('CLUBS', '8'), Bid('DIAMONDS', '8'), Bid('HEARTS', '8'), Bid('NO_TRUMPS', '8'),
			Bid('SPADES', '9'), Bid('CLUBS', '9'), Bid('DIAMONDS', '9'), Bid('HEARTS', '9'), Bid('NO_TRUMPS', '9'),
			Bid('SPADES', '10'), Bid('CLUBS', '10'), Bid('DIAMONDS', '10'),
			Bid('OPEN_MISERE'),
			Bid('HEARTS', '10'), Bid('NO_TRUMPS', '10')
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
		if not type(other) == Bid:
			raise TypeError(f'\'>\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) == '>'

	def __lt__(self, other):
		if not type(other) == Bid:
			raise TypeError(f'\'<\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) == '<'

	def __ge__(self, other):
		if not type(other) == Bid:
			raise TypeError(f'\'>=\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) in { '>', '=' }

	def __le__(self, other):
		if not type(other) == Bid:
			raise TypeError(f'\'<=\' not supported between instances of \'Bid\' and \'{type(other)}\'')

		return self._compare(other) in { '<', '=' }
