class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

	def __str__(self):
		return 'Players: ' + ', '.join([str(player.account) for player in self.players]) + '\n'
			+ 'Score: ' + str(self.score)

	def __repr__(self):
		return 'Team(players=[' + ', '.join([player.account.uuid for player in self.players]) + f'], score={self.score})'
