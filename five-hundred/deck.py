from card import *

import random

class Deck:
	def __init__(self, initialize=True):
		self.cards = []
		if initialize:
			self.new_deck()

	def new_deck(self):
		deck = []

		# Generate full deck
		for rank in CardRank.ranks:
			for suit in [suit for suit in CardSuit.suits if suit != 'JOKER']:
				deck.append(Card(rank, suit))

		# Add Joker
		deck.append(Card('JOKER', None))

		# Remove unused cards
		deck = filter(lamba card: not card.rank in { 'TWO', 'THREE' } and not (card.rank == "FOUR" and card.suit in { 'CLUBS', 'SPADES' }), deck)

		# Update self.cards - this step is performed at the end to preserve atomicity
		self.cards = deck

	def shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		index = random.randint(0, len(self.cards) - 1)
		card = self.cards[index]
		del self.cards[index]
		return card
