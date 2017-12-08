class Trick:
	def __init__(self, leader_id):
		self.leader_id = leader_id
		self.cards = []

	def __str__(self):
		return f'Leader: {self.leader_id}\n' \
			+ 'Cards: ' + ', '.join([str(card) for card in self.cards])

	def __repr__(self):
		return f'Trick(leader={self.leader_id}, cards=[' + ', '.join([card.to_minimal_str() for card in self.cards]) + '])'
