from card import Card

class Trick:
	def __init__(self, leader_id):
		self.leader_id = leader_id
		self.cards = []

	def append(self, card):
		if not type(card) == Card:
			raise TypeError('Cannot append non-Cards to trick')

		if len(self.cards) + 1 > 4:
			raise ValueError('Trick already has 4 cards played')

		self.cards.append(card)

	def __str__(self):
		return f'Trick leader: {self.leader_id}; Cards: ' + ', '.join([str(card) for card in self.cards])

	def __repr__(self):
		return f'Trick(leader={self.leader_id}, cards=[' + ', '.join([card.to_minimal_string() for card in self.cards]) + '])'

	def __len__(self):
		return len(self.cards)
