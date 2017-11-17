# TODO list
# - it might be better to define some 500-specific exceptions, e.g. NotPlayersTurnError, CardNotPosessedError, etc.
# - docstrings

class FiveHundredGame:
	def __init__(self, teams):
		self.teams = teams
		self.spectators = []
		self.hands = []

	def get_player(self, player_id):
		for team in self.teams:
			for player in team.players:
				if player.id == player_id:
					return player
		return None
