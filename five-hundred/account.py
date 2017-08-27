import uuid

class Account:
	def __init__(self, username):
		self.id = str(uuid.uuid4())
		self.username = username
