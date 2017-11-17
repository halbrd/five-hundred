from account import *

class Player:
	def __init__(self, account):
		self.account = account

	def __str__(self):
		return self.account.username

	def __repr__(self):
		return f'Player({self.account.uuid})'

	def __eq__(self, other):
		return type(other) is Player and self.account.uuid == other.account.uuid

	def __ne__(self, other):
		return not self.__eq__(other)
