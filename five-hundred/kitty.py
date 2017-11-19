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
		return 'Kitty(cards=[' + ', '.join([card.to_minimal_string() for card in self.cards]) + f'], collected={self.collected})'
