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
				deck.append(Card(suit, rank))

		# Remove unused cards
		deck = list(filter(lambda card: not card.rank in [ 'TWO', 'THREE' ] and not (card.rank == "FOUR" and card.suit in [ 'CLUBS', 'SPADES' ]), deck))

		# Add Joker
		deck.append(Card('JOKER'))

		# Update self.cards - this step is performed at the end to preserve atomicity
		self.cards = deck

	def shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		if len(self.cards) == 0:
			raise IndexError('Draw from empty deck')

		card = self.cards[0]
		del self.cards[0]
		return card

	def prepend(self, card):
		if not type(card) == Card:
			raise TypeError('Cannot store non-Cards in deck')

		self.cards.insert(0, card)

	def append(self, card):
		if not type(card) == Card:
			raise TypeError('Cannot store non-Cards in deck')

		self.cards.append(card)

	def __contains__(self, card):
		return card in self.cards

	def __str__(self):
		return f'Deck with {len(self.cards)} cards'

	def __repr__(self):
		# we first need to split our deck of cards into two groups:
		#   - cards that are members of the expected deck of cards
		#   - cards that are not expected in the deck or are duplicates

		suits = [ 'CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES' ]
		ranks = [ 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE' ]

		normal_deck = set()
		normal_deck.update([ Card('DIAMONDS', 'FOUR'), Card('HEARTS', 'FOUR') ])
		normal_deck.update([ Card(suit, rank) for suit in suits for rank in ranks ])
		normal_deck.update([ Card('JOKER') ])

		expected_cards = set()   # we should really use a set for performance reasons, since we'll be doing lots of membership checks
		extra_cards = []

		for card in self.cards:
			if card in normal_deck and not card in expected_cards:
				expected_cards.add(card)
			else:
				extra_cards.append(card)

		# next we need to convert these two sequences into two strings:
		#   - expected_cards into a pre-arranged grid of cards that highlights gaps - a full deck would look something like:
		# 			   5C 6C 7C 8C 9C TC JC QC KC AC
		# 			4D 5D 6D 7D 8D 9D TD JD QD KD AD
		# 			4H 5H 6H 7H 8H 9H TH JH QH KH AH
		# 			   5S 6S 7S 8S 9S TS JS QS KS AS
		#   - extra_cards into a sorted line of space-separated cards

		# we have an edge case - if the deck is empty, we should just return 'Deck()'
		if len(extra_cards) == len(expected_cards) == 0:
			return 'Deck()'

		# we're now going to turn out cards into lines to output
		lines = []

		for suit in suits:
			expected_suit_cards = sorted([ card for card in normal_deck if card.suit == suit ])

			actual_suit_cards = [ card for card in expected_cards if card.suit == suit ]
			actual_suit_cards_with_gaps = []

			for card in expected_suit_cards:
				actual_suit_cards_with_gaps.append(card.to_minimal_string() if card in actual_suit_cards else '  ')

			line = ' '.join(actual_suit_cards_with_gaps)
			lines.append(line)

		# we'll just sort the extras and stick them on their own line - unless there aren't any extras
		if extra_cards:
			extra_cards = sorted(extra_cards)
			lines.append(' '.join([card.to_minimal_string() for card in extra_cards]))

		# now we will assemble the final string
		lines.insert(0, 'Deck(')

		# add the Joker to the first line
		if Card('JOKER') in expected_cards:
			lines[0] += ' ' + Card('JOKER').to_minimal_string()

		lines.append(')')

		# we want to indent the inside lines by the correct amount
		lines[1] = '     ' + lines[1]   # Clubs line
		lines[2] = '  ' + lines[2]   # Diamonds line
		lines[3] = '  ' + lines[3]   # Hearts line
		lines[4] = '     ' + lines[4]   # Spades line
		if extra_cards:
			lines[5] = '  ' + lines[5]   # extra cards line

		# now we just assemble the lines
		lines = list(map(lambda line: line.rstrip(), lines))   # remove trailing spaces
		r = '\n'.join(lines)

		return r

	def __len__(self):
		return len(self.cards)
