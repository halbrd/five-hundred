from card import Card

class Kitty:
	def __init__(self, cards=None):
		# if cards were passed, check that they are actually 3 Cards
		if cards is not None and (
			not type(cards) in { list, tuple }   # is not a relevant type
			or len(cards) > 3   # has too many cards
			or not all([type(card) == Card for card in cards])   # contains non-Cards
		):
			raise ValueError('cards parameter must be an iterable of 3 or fewer cards (or nothing)')

		self.cards = list(cards or [])
		self.collected = False

	def append(self, value):
		if len(self.cards) + 1 > 3:
			raise ValueError('Kitty cannot contain more than 3 cards')
		if not type(value) == Card:
			raise ValueError('Kitty cannot contain non-Card types')

		self.cards.append(value)

	def collect_cards(self):
		if len(self.cards) < 3:
			raise ValueError('Kitty cannot be collected until it has all 3 cards')
		if self.collected:
			raise ValueError('Kitty has already been collected')

		self.collected = True
		return self.cards

	def __str__(self):
		return '[' + ', '.join([str(card) for card in self.cards]) + '] (' + ('' if self.collected else 'un') + 'collected)'

	def __repr__(self):
		return 'Kitty(cards=[' + ', '.join([card.to_minimal_string() for card in self.cards]) + f'], collected={self.collected})'

	def __len__(self):
		return len(self.cards)
