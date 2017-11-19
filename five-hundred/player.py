from account import *

class Player:
	def __init__(self, account):
		self.account = account

	def __str__(self):
		return self.account.username

	def __repr__(self):
		return f'Player({self.account.uuid})'

	def __eq__(self, other):
		if type(other) is Player:
			return self.account.uuid == other.account.uuid
		elif type(other) is str:
			return self.account.uuid == other
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)
