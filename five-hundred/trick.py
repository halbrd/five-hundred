class Trick:
	def __init__(self, leader):
		self.leader = leader
		self.cards = []

	def __str__(self):
		return f'Leader: {self.leader}\n' \
			+ 'Cards: ' + ', '.join([str(card) for card in self.cards])

	def __repr__(self):
		return f'Trick(leader={self.leader}, cards=[' + ', '.join([card.to_minimal_str() for card in self.cards]) + '])'
