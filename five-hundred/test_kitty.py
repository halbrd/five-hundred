import pytest

from kitty import Kitty
from card import Card

def card_list_types(iterable):
	''' convert an iterable of cards into all supported input types for Kitty.__init__ '''
	return [ list(iterable), tuple(iterable) ]

class TestKittyInit:
	def test_no_cards(self):
		kitty = Kitty()
		assert kitty.cards == []
		assert kitty.collected == False

	def test_three_cards(self):
		cards = [ Card('HEARTS', 'ACE'), Card('CLUBS', 'SEVEN'), Card('JOKER') ]

		for cards in card_list_types(cards):
			kitty = Kitty(cards)
			assert kitty.cards == list(cards)

	def test_fewer_than_three_cards(self):
		one_card = [ Card('HEARTS', 'ACE') ]
		two_cards = [ Card('HEARTS', 'ACE'), Card('JOKER') ]

		for cards in card_list_types(one_card) + card_list_types(two_cards):
			kitty = Kitty(cards)
			assert kitty.cards == list(cards)

	def test_too_many_cards(self):
		cards = [ Card('HEARTS', 'ACE'), Card('CLUBS', 'SEVEN'), Card('JOKER'), Card('SPADES', 'JACK') ]

		with pytest.raises(ValueError):
			kitty = Kitty(cards)

	def test_misc_valid_inputs(self):
		# these inputs all equate to no cards
		valid_inputs = [ [], (), None ]

		for input in valid_inputs:
			kitty = Kitty(input)
			assert kitty.cards == []

	def test_invalid_types(self):
		invalid_inputs = [
			Card('CLUBS', 'KING'),   # Card not wrapped in iterable
			True, False, 'a', 1,   # non-Card types
			[ True ], { 'b', 1 }, ( 'd', None, 'f' ),   # non-Card types wrapped in iterables
			[ Card('HEARTS', 'SIX'), 'b' ]   # mix of Cards and invalid types
		]

		for input in invalid_inputs:
			with pytest.raises(ValueError):
				kitty = Kitty(input)

class TestKittyOperations:
	def setup_method(self, method):
		self.kitty = Kitty()

	def test_append(self):
		# starts empty
		assert len(self.kitty) == 0

		# append first card
		self.kitty.append(Card('SPADES', 'ACE'))
		assert len(self.kitty) == 1

		# append second card
		self.kitty.append(Card('CLUBS', 'NINE'))
		assert len(self.kitty) == 2

		# append third card
		self.kitty.append(Card('DIAMONDS', 'SEVEN'))
		assert len(self.kitty) == 3


	def test_append_card_limit(self):
		for card in [ Card('SPADES', 'ACE'), Card('CLUBS', 'NINE'), Card('DIAMONDS', 'SEVEN') ]:
			self.kitty.append(card)

		with pytest.raises(ValueError):
			self.kitty.append(Card('DIAMONDS', 'NINE'))

	def test_append_invalid_values(self):
		invalid_values = [ True, False, None, 1, 'a', [], {}, (), [ Card('CLUBS', 'SIX') ] ]

		for value in invalid_values:
			with pytest.raises(ValueError):
				self.kitty.append(value)

	def test_collect(self):
		for card in [ Card('SPADES', 'ACE'), Card('CLUBS', 'NINE'), Card('DIAMONDS', 'SEVEN') ]:
			# make sure that we can't collect yet
			with pytest.raises(ValueError):
				kitty_cards = self.kitty.collect_cards()

			# make sure that the kitty hasn't been collected despite the attempt
			assert self.kitty.collected == False

			self.kitty.append(card)

		# now that we have 3 cards in the kitty, we should be able to collect them
		kitty_cards = self.kitty.collect_cards()
		assert len(kitty_cards) == 3

		# the kitty should still have the cards, but should be marked as collected
		assert kitty_cards == self.kitty.cards
		assert self.kitty.collected

	def test_collect_twice(self):
		for card in [ Card('SPADES', 'ACE'), Card('CLUBS', 'NINE'), Card('DIAMONDS', 'SEVEN') ]:
			self.kitty.append(card)

		kitty_cards = self.kitty.collect_cards()

		# make sure we can't collect the kitty twice
		with pytest.raises(ValueError):
			kitty_cards_2 = self.kitty.collect_cards()

class TestKittyDunders:
	def setup_method(self, method):
		self.kitty = Kitty()

	def test_str(self):
		# empty kitty
		assert str(self.kitty) == '[] (uncollected)'

		# one card
		card_1 = Card('DIAMONDS', 'SEVEN')
		self.kitty.append(card_1)
		assert str(self.kitty) == f'[{card_1}] (uncollected)'

		# two cards
		card_2 = Card('JOKER')
		self.kitty.append(card_2)
		assert str(self.kitty) == f'[{card_1}, {card_2}] (uncollected)'

		# three cards
		card_3 = Card('CLUBS', 'NINE')
		self.kitty.append(card_3)
		assert str(self.kitty) == f'[{card_1}, {card_2}, {card_3}] (uncollected)'

		# collected
		kitty_cards = self.kitty.collect_cards()
		assert str(self.kitty) == f'[{card_1}, {card_2}, {card_3}] (collected)'

	def test_repr(self):
		# empty kitty
		assert repr(self.kitty) == 'Kitty(cards=[], collected=False)'

		# one card
		card_1 = Card('DIAMONDS', 'SEVEN')
		self.kitty.append(card_1)
		assert repr(self.kitty) == f'Kitty(cards=[{card_1.to_minimal_string()}], collected=False)'

		# two cards
		card_2 = Card('JOKER')
		self.kitty.append(card_2)
		assert repr(self.kitty) == f'Kitty(cards=[{card_1.to_minimal_string()}, {card_2.to_minimal_string()}], collected=False)'

		# three cards
		card_3 = Card('CLUBS', 'NINE')
		self.kitty.append(card_3)
		assert repr(self.kitty) == f'Kitty(cards=[{card_1.to_minimal_string()}, {card_2.to_minimal_string()}, {card_3.to_minimal_string()}], collected=False)'

		# collected
		kitty_cards = self.kitty.collect_cards()
		assert repr(self.kitty) == f'Kitty(cards=[{card_1.to_minimal_string()}, {card_2.to_minimal_string()}, {card_3.to_minimal_string()}], collected=True)'

	def test_len(self):
		# empty kitty
		assert len(self.kitty) == 0

		# one card
		self.kitty.append(Card('DIAMONDS', 'SEVEN'))
		assert len(self.kitty) == 1

		# two cards
		self.kitty.append(Card('JOKER'))
		assert len(self.kitty) == 2

		# three cards
		self.kitty.append(Card('CLUBS', 'NINE'))
		assert len(self.kitty) == 3

		# collected
		kitty_cards = self.kitty.collect_cards()
		assert len(self.kitty) == 3
