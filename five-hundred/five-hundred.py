import random

class Player:
	def __init__(self, name):
		self.name = name

class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

class Kitty:
	def __init__(self, cards):
		self.cards = cards

class Trick:
	def __init__(self, leader, cards):
		self.leader = leader
		self.cards = []

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


###################################################


normal_card = Card('SPADES', 'FIVE')
print(str(normal_card))
print(normal_card.minimal_str())

joker_card = Card('JOKER', 'ACE')
print(str(joker_card))
print(joker_card.minimal_str())

wtf_card2 = Card('asdasdadad', 'ACE')
print(str(wtf_card2))
print(wtf_card2.minimal_str())
