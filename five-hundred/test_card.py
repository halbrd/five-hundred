import pytest

from card import CardRank, CardSuit, Card

class TestCardRank:
	def test_rank_normal_inputs(self):
		ranks = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']

		for rank in ranks:
			card_rank = CardRank(rank)
			assert card_rank.rank == rank.upper()

	def test_rank_alternate_inputs(self):
		ranks = ['Ace', 'two', 'ThReE', 'fOuR', 'fIVE']

		for rank in ranks:
			card_rank = CardRank(rank)
			assert card_rank.rank == rank.upper()

	def test_rank_invalid_inputs(self):
		inputs = ['ACE ', '', 'A', '4', 4, True, False, None]

		for input in inputs:
			with pytest.raises(ValueError):
				card_rank = CardRank(input)

class TestCardRankDunder:
	def test_to_string(self):
		test_cases = {
			'ACE': 'Ace', 'TWO': 'Two', 'THREE': 'Three', 'FOUR': 'Four', 'FIVE': 'Five', 'SIX': 'Six', 'SEVEN': 'Seven',
			'EIGHT': 'Eight', 'NINE': 'Nine', 'TEN': 'Ten', 'JACK': 'Jack', 'QUEEN': 'Queen', 'KING': 'King'
		}

		for input, output in test_cases.items():
			card_rank = CardRank(input)
			assert card_rank.to_string() == output

	def test_to_minimal_string(self):
		test_cases = {
			'ACE': 'A', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8',
			'NINE': '9', 'TEN': 'T', 'JACK': 'J', 'QUEEN': 'Q', 'KING': 'K'
		}

		for input, output in test_cases.items():
			card_rank = CardRank(input)
			assert card_rank.to_minimal_string() == output

	def test_repr(self):
		ranks = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']

		for rank in ranks:
			assert repr(CardRank(rank)) == f'CardRank({rank})'

	def test_eq_ne(self):
		positive_test_cases = [
			[ CardRank('SEVEN'), CardRank('SEVEN') ],
			[ CardRank('KING'), CardRank('king') ],
			[ CardRank('JACK'), 'JACK' ],
			[ CardRank('ACE'), 'ace' ]
		]

		negative_test_cases = [
			[ CardRank('SEVEN'), 7 ],
			[ CardRank('SEVEN'), '' ],
			[ CardRank('SEVEN'), '7' ],
			[ CardRank('SEVEN'), True ],
			[ CardRank('SEVEN'), False ],
			[ CardRank('SEVEN'), None ],
			[ CardRank('SEVEN'), CardRank('SIX') ],
			[ CardRank('SEVEN'), CardRank('QUEEN') ]
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left == right
			assert not left != right

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert left != right



class TestCardSuit:
	def test_suit_normal_inputs(self):
		suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'JOKER']

		for suit in suits:
			card_suit = CardSuit(suit)
			assert card_suit.suit == suit.upper()

	def test_suit_alternate_inputs(self):
		suits = ['Clubs', 'diamonds', 'HeArTs']

		for suit in suits:
			card_suit = CardSuit(suit)
			assert card_suit.suit == suit.upper()

	def test_suit_invalid_inputs(self):
		inputs = ['CLUBS ', '', 'J', '4', 4, True, False, None]

		for input in inputs:
			with pytest.raises(ValueError):
				card_suit = CardSuit(input)

class TestCardSuitDunder:
	def test_to_string(self):
		test_cases = {
			'CLUBS': 'Clubs', 'DIAMONDS': 'Diamonds', 'HEARTS': 'Hearts', 'SPADES': 'Spades', 'JOKER': 'Joker'
		}

		for input, output in test_cases.items():
			card_suit = CardSuit(input)
			assert card_suit.to_string() == output

	def test_to_minimal_string(self):
		test_cases = {
			'CLUBS': 'C', 'DIAMONDS': 'D', 'HEARTS': 'H', 'SPADES': 'S', 'JOKER': 'J'
		}

		for input, output in test_cases.items():
			card_suit = CardSuit(input)
			assert card_suit.to_minimal_string() == output

	def test_repr(self):
		suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'JOKER']

		for rank in ranks:
			assert repr(CardRank(rank)) == f'CardSuit({rank})'

	def test_eq_ne(self):
		positive_test_cases = [
			[ CardSuit('DIAMONDS'), CardSuit('DIAMONDS') ],
			[ CardSuit('SPADES'), CardSuit('spades') ],
			[ CardSuit('HEARTS'), 'HEARTS' ],
			[ CardSuit('CLUBS'), 'clubs' ]
		]

		negative_test_cases = [
			[ CardSuit('DIAMONDS'), 7 ],
			[ CardSuit('DIAMONDS'), '' ],
			[ CardSuit('DIAMONDS'), '7' ],
			[ CardSuit('DIAMONDS'), True ],
			[ CardSuit('DIAMONDS'), False ],
			[ CardSuit('DIAMONDS'), None ],
			[ CardSuit('DIAMONDS'), CardSuit('HEARTS') ],
			[ CardSuit('DIAMONDS'), CardSuit('JOKER') ]
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left == right
			assert not left != right

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert left != right
