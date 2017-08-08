from account import *
from bid import Bid

class Player:
	def __init__(self, account):
		self.account = account

class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

class Kitty:
	def __init__(self, cards):
		self.cards = cards
		self.collected = False

class Trick:
	def __init__(self, leader, cards):
		self.leader = leader
		self.cards = []

	def winner(self):
		pass

	def value(self):
		pass

class Hand:
	def __init__(self, dealer, hands, kitty):
		self.dealer = dealer
		self.hands = hands
		self.kitty = kitty
		self.bids = []
		self.tricks = []

class FiveHundredGame:
	def __init__(self, teams):
		self.teams = teams
		self.hands = []
