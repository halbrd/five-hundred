class Player:
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __str__(self):
		return self.name

	def __repr__(self):
		return f'Player({self.id})'

	def __eq__(self, other):
		if type(other) is Player:
			return self.id == other.id
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)
