from team import Team
from player import Player
from hand import Hand

import random

class FiveHundredGame:
	def __init__(self, players):
		# players should be passed in turn order (so teams are alternating players)
		# for now, we only support 4 player games
		if len(players) != 4:
			raise ValueError('Number of players passed was not 4')

		# assemble players into teams
		self.teams = [ Team([ players[0], players[2] ]), Team([ players[1], players[3] ]) ]

		self.hands = []

		# since this is the first hand, we randomly select the first dealer
		dealer_id = random.choice(self.get_players(attr='id'))
		player_ids = self.get_players(dealer_id=dealer_id, attr='id')
		dealer_id = player_ids[0]
		del player_ids[0]

		self.hands.append(Hand(dealer_id, player_ids))

	def get_players(self, dealer_id=None, attr=None):
		offset = 0

		player_indices = [ (0, 0), (1, 0), (0, 1), (1, 1) ]
		players = [ self.teams[index[0]].players[index[1]] for index in player_indices ]

		if dealer_id:
			try:
				dealer_index = list(map(lambda player: player.id, players)).index(dealer_id)
			except ValueError:
				raise ValueError('No player with dealer_id')
			else:
				offset = dealer_index

		if attr:
			# no need to check if the attribute exists - the default AttributeError that would be raised is perfect for our needs
			players = list(map(lambda player: getattr(player, attr), players))

		return players[offset:] + players[:offset]

	def get_player(self, player_id):
		for team in self.teams:
			for player in team.players:
				if player.id == player_id:
					return player
		return None
