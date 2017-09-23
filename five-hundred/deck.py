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
		deck = filter(lambda card: not card.rank in { 'TWO', 'THREE' } and not (card.rank == "FOUR" and card.suit in { 'CLUBS', 'SPADES' }), deck)

		# Update self.cards - this step is performed at the end to preserve atomicity
		self.cards = deck

	def shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		index = random.randint(0, len(self.cards) - 1)
		card = self.cards[index]
		del self.cards[index]
		return card

	def __contains__(self, card):
		return card in self.cards

	def __str__(self):
		return f'Deck with {len(self.cards)} cards'

	def __repr__(self):
		return '' # TODO: finish this when Joker representation is working

		expected_cards = {
			'clubs':            ['FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING'],
			'diamonds': ['FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING'],
			'hearts':   ['FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING'],
			'spades':           ['FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
		}

		output_lines = {
			'clubs': '   ',
			'diamonds': '',
			'hearts': '',
			'spades': '   '
		}

		for suit, ranks in expected_cards:
			for rank in ranks:
				output_lines[suit] += (Card(rank, suit).to_minimal_str() if Card(rank, suit) in self else '  ') + ' '
