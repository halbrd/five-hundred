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
		cards = [card.to_minimal_str() for card in self.cards]

		# split out duplicate cards
		unique_cards = set()
		extra_cards = []

		while len(cards) > 0:
			if cards[0] in unique_cards:
				extra_cards.append(cards[0])
			else:
				unique_cards.add(cards[0])
			del cards[0]


		expected_cards = {   # not including Joker
			'CLUBS':            ['FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING'],
			'DIAMONDS': ['FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING'],
			'HEARTS':   ['FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING'],
			'SPADES':           ['FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
		}

		output_lines = {
			'CLUBS':    '   ',
			'DIAMONDS': '',
			'HEARTS':   '',
			'SPADES':   '   '
		}

		for suit, ranks in expected_cards:
			for rank in ranks:
				min_str = Card(rank, suit).to_minimal_str()
				output_lines[suit] += (min_str if min_str in unique_cards else '  ') + ' '

		has_joker = Card('joker').to_minimal_str() in unique_cards

		return 'Deck( ' + ('J ' if has_joker else '') \
			+ '\n  '.join([output_lines[suit] for suit in sorted(output_lines.keys())]) + '\n' \
			+ ' '.join(extra_cards) + ')'
