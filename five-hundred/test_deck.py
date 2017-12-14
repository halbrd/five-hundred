import pytest

from deck import Deck
from card import Card, CardSuit, CardRank

class TestDeck:
	def test_init(self):
		deck = Deck(initialize=False)
		assert deck.cards == []

		deck = Deck()
		assert len(deck.cards) == 43

	def test_new_deck(self):
		deck = Deck(initialize=False)
		assert deck.cards == []

		deck.new_deck()
		assert len(deck.cards) == 43
		assert deck.cards[:3] == [ Card('DIAMONDS', 'FOUR'), Card('HEARTS', 'FOUR'), Card('CLUBS', 'FIVE') ]
		assert deck.cards[-3:] == [ Card('HEARTS', 'ACE'), Card('SPADES', 'ACE'), Card('JOKER') ]

		deck.shuffle()

		deck.new_deck()
		assert len(deck.cards) == 43
		assert deck.cards[:3] == [ Card('DIAMONDS', 'FOUR'), Card('HEARTS', 'FOUR'), Card('CLUBS', 'FIVE') ]
		assert deck.cards[-3:] == [ Card('HEARTS', 'ACE'), Card('SPADES', 'ACE'), Card('JOKER') ]

	def test_shuffle(self):
		deck = Deck()
		assert deck.cards[:3] == [ Card('DIAMONDS', 'FOUR'), Card('HEARTS', 'FOUR'), Card('CLUBS', 'FIVE') ]

		deck.shuffle()
		assert not deck.cards[:3] == [ Card('DIAMONDS', 'FOUR'), Card('HEARTS', 'FOUR'), Card('CLUBS', 'FIVE') ]

	def test_draw_card(self):
		deck = Deck()

		for _ in range(42):
			deck_size = len(deck.cards)
			top_card = deck.cards[0]

			drawn_card = deck.draw_card()

			assert len(deck.cards) == deck_size - 1
			assert drawn_card == top_card
			assert top_card != deck.cards[0]

		# one card left in deck
		assert len(deck.cards) == 1
		top_card = deck.cards[0]

		drawn_card = deck.draw_card()

		assert len(deck.cards) == 0
		assert drawn_card == top_card

		# make sure that an exception is raised if draw_card is called on an empty deck
		with pytest.raises(IndexError):
			drawn_card = deck.draw_card()

	def test_prepend(self):
		deck = Deck()
		assert deck.cards[:2] == [ Card('DIAMONDS', 'FOUR'), Card('HEARTS', 'FOUR') ]
		assert len(deck.cards) == 43

		deck.prepend(Card('SPADES', 'TWO'))
		assert deck.cards[:2] == [ Card('SPADES', 'TWO'), Card('DIAMONDS', 'FOUR') ]
		assert len(deck.cards) == 44

		invalid_inputs = [ CardSuit('HEARTS'), CardRank('JACK'), None, True, False, [], 'string!' ]

		for input in invalid_inputs:
			with pytest.raises(TypeError):
				deck.prepend(input)

	def test_append(self):
		deck = Deck()
		assert deck.cards[-2:] == [ Card('SPADES', 'ACE'), Card('JOKER') ]
		assert len(deck.cards) == 43

		deck.append(Card('SPADES', 'TWO'))
		assert deck.cards[-2:] == [ Card('JOKER'), Card('SPADES', 'TWO') ]
		assert len(deck.cards) == 44

		invalid_inputs = [ CardSuit('HEARTS'), CardRank('JACK'), None, True, False, [], 'string!' ]

		for input in invalid_inputs:
			with pytest.raises(TypeError):
				deck.append(input)

class TestDeckDunder:
	def test_contains(self):
		deck = Deck()

		assert Card('SPADES', 'SEVEN') in deck
		assert Card('JOKER') in deck
		assert not Card('HEARTS', 'TWO') in deck
		assert Card('HEARTS', 'TWO') not in deck

	def test_str(self):
		deck = Deck(initialize=False)
		assert str(deck) == 'Deck with 0 cards'

		deck.new_deck()
		assert str(deck) == 'Deck with 43 cards'

		deck.append(Card('CLUBS', 'JACK'))
		assert str(deck) == 'Deck with 44 cards'

		deck.draw_card()
		deck.draw_card()
		assert str(deck) == 'Deck with 42 cards'

	def test_repr(self):
		# oh boy
		# here we go

		deck = Deck(initialize=False)
		assert repr(deck) == 'Deck()'

		# Default Deck
		deck = Deck()
		assert repr(deck) == \
'''Deck( J-
     5C 6C 7C 8C 9C TC JC QC KC AC
  4D 5D 6D 7D 8D 9D TD JD QD KD AD
  4H 5H 6H 7H 8H 9H TH JH QH KH AH
     5S 6S 7S 8S 9S TS JS QS KS AS
)'''

		# Take away some cards
		del deck.cards[6]
		del deck.cards[19]
		del deck.cards[32]
		assert repr(deck) == \
'''Deck( J-
     5C    7C 8C 9C TC JC QC    AC
  4D 5D 6D 7D 8D 9D TD JD QD KD AD
  4H 5H 6H 7H 8H    TH JH QH KH AH
     5S 6S 7S 8S 9S TS JS QS KS AS
)'''

		# add some extra cards (including duplicate)
		deck.append(Card('CLUBS', 'EIGHT'))
		deck.append(Card('HEARTS', 'JACK'))
		deck.append(Card('JOKER'))
		assert repr(deck) == \
'''Deck( J-
     5C    7C 8C 9C TC JC QC    AC
  4D 5D 6D 7D 8D 9D TD JD QD KD AD
  4H 5H 6H 7H 8H    TH JH QH KH AH
     5S 6S 7S 8S 9S TS JS QS KS AS
  8C JH J-
)'''

		# replace an expected card and check that extra sorting works
		deck.append(Card('CLUBS', 'SIX'))
		deck.append(Card('CLUBS', 'TEN'))
		assert repr(deck) == \
'''Deck( J-
     5C 6C 7C 8C 9C TC JC QC    AC
  4D 5D 6D 7D 8D 9D TD JD QD KD AD
  4H 5H 6H 7H 8H    TH JH QH KH AH
     5S 6S 7S 8S 9S TS JS QS KS AS
  8C TC JH J-
)'''

		# build a deck from scratch
		deck = Deck(initialize=False)
		deck.append(Card('CLUBS', 'EIGHT'))
		deck.append(Card('HEARTS', 'JACK'))
		deck.append(Card('HEARTS', 'SEVEN'))
		assert repr(deck) == \
'''Deck(
              8C

           7H          JH

)'''

		deck.append(Card('CLUBS', 'NINE'))
		deck.append(Card('JOKER'))
		assert repr(deck) == \
'''Deck( J-
              8C 9C

           7H          JH

)'''


	def test_len(self):
		deck = Deck(initialize=False)
		assert len(deck) == len(deck.cards) == 0

		deck = Deck()
		assert len(deck) == len(deck.cards) == 43

		deck.append(Card('JOKER'))
		assert len(deck) == len(deck.cards) == 44

		deck.draw_card()
		deck.draw_card()
		deck.draw_card()
		assert len(deck) == len(deck.cards) == 41
