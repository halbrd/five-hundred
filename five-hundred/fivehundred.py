from account import *
from bid import Bid
from deck import Deck

from collections import OrderedDict
from enum import Enum

class Player:
	def __init__(self, account):
		self.account = account

class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

class Kitty:
	def __init__(self, cards=None):
		self.cards = cards or []
		self.collected = False

	def append(self, value):
		self.cards.append(value)

	def collect_cards(self):
		if len(self.cards) < 3:
			raise ValueError(f'Kitty has fewer than 3 cards')

		cards, self.cards = self.cards, []
		self.collected = True
		return cards

class Trick:
	def __init__(self, leader, cards):
		self.leader = leader
		self.cards = []

class Hand:
	def __init__(self, dealer_id, player_ids):
		self.dealer_id = dealer_id
		self.deck = Deck()
		self.hands = OrderedDict({ player_id: [] for player_id in player_ids + dealer_id})
		self.kitty = None
		self.bids = []
		self.tricks = []

		self.deal()

	def deal(self):
		self.deck.shuffle()

		# Yeah, I know, there's no point following the dealing order. It just feels better this way.

		for player_id, hand in self.hands:
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty = Kitty()
		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands:
			for _ in range(4):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands:
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

class FiveHundredGame:
	def __init__(self, teams):
		self.teams = teams
		self.hands = []

	def get_player(self, player_id):
		for team in self.teams:
			for player in team.players:
				if player.id == player_id:
					return player
		return None
