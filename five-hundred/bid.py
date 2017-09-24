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

class BidSuit:
	suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'NO_TRUMPS', 'MISERE', 'OPEN_MISERE', 'PASS']
	dependent_suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'NO_TRUMPS']
	independent_suits = ['MISERE', 'OPEN_MISERE', 'PASS']

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

class Bid:
	def __init__(self, player, input1, input2=None):
		# argument names can't be specific (eg. value, suit) to remain accurate with flexible inputs
		# eg. ('6', 'NO_TRUMPS'), ('MISERE')
		self.player = player

		if input1 in BidSuit.independent_suits and input2 is None:
			self.suit = BidSuit(input1)
		elif input1 in BidSuit.independent_suits:
			raise ValueError('Independent suits cannot be instantiated with a value')
		else:
			self.value = BidValue(input1)
			self.suit = BidSuit(input2)

	def to_string(self):
		if self.suit in BidSuit.independent_suits:
			return f'{self.player}: {self.suit}'
		else:
			return f'{self.player}: {self.value} {self.suit}'

	def to_minimal_string(self):
		if self.suit in BidSuit.independent_suits:
			return self.suit.to_minimal_string() + ' '
		else:
			return self.value.to_minimal_string() + self.suit.to_minimal_string()

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		return f'Bid(player={self.player}, {self.value.value} {self.suit.suit})'

	def __eq__(self, other):
		return type(other) == Bid and self.value == other.value and self.suit == other.suit

	def strict_equals(self, other):
		return type(other) == Bid and self.player == other.player and self.value == other.value and self.suit == other.suit
