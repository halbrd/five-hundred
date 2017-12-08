import pytest

from card import CardRank, CardSuit, Card
from bid import BidSuit

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

		# check that all minimal strings are unique
		assert len(test_cases.values()) == len(set(test_cases.values()))

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
			assert right == left
			assert not left != right
			assert not right != left

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert right != left

	def test_gt_lt_ge_le(self):
		less_than_cases = [
			[ CardRank('TWO'), CardRank('THREE') ],
			[ CardRank('FOUR'), CardRank('ACE') ],
			[ CardRank('TEN'), CardRank('JACK') ],
			[ CardRank('EIGHT'), CardRank('JACK') ],
			[ CardRank('KING'), CardRank('ACE') ],
			[ CardRank('SIX'), CardRank('SEVEN') ]
		]

		equal_cases = [
			[ CardRank('ACE'), CardRank('ACE') ],
			[ CardRank('THREE'), CardRank('THREE') ],
			[ CardRank('NINE'), CardRank('NINE') ]
		]

		error_cases = [
			[ CardRank('FIVE'), 'FOUR' ],
			[ CardRank('FIVE'), 4 ],
			[ CardRank('FIVE'), [] ],
			[ CardRank('FIVE'), None ],
			[ CardRank('FIVE'), True ],
			[ CardRank('FIVE'), False ]
		]

		for test_case in less_than_cases:
			left, right = test_case[0], test_case[1]
			assert left < right
			assert left <= right
			assert not left > right
			assert not left >= right

		for test_case in equal_cases:
			left, right = test_case[0], test_case[1]
			assert not left < right
			assert left <= right
			assert not left > right
			assert left >= right

		for test_case in error_cases:
			left, right = test_case[0], test_case[1]

			with pytest.raises(TypeError):
				left < right
			with pytest.raises(TypeError):
				left <= right
			with pytest.raises(TypeError):
				left > right
			with pytest.raises(TypeError):
				left >= right


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

		# check that all minimal strings are unique
		assert len(test_cases.values()) == len(set(test_cases.values()))

		for input, output in test_cases.items():
			card_suit = CardSuit(input)
			assert card_suit.to_minimal_string() == output

	def test_repr(self):
		suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'JOKER']

		for suit in suits:
			assert repr(CardSuit(suit)) == f'CardSuit({suit})'

	def test_eq_ne(self):
		positive_test_cases = [
			[ CardSuit('DIAMONDS'), CardSuit('DIAMONDS') ],
			[ CardSuit('SPADES'), CardSuit('spades') ],
			[ CardSuit('HEARTS'), 'HEARTS' ],
			[ CardSuit('CLUBS'), 'clubs' ]
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left == right
			assert right == left
			assert not left != right
			assert not right != left

		negative_test_cases = [
			# CardSuit to CardSuit
			[ CardSuit('DIAMONDS'), CardSuit('HEARTS') ],
			[ CardSuit('DIAMONDS'), CardSuit('JOKER') ],
			# CardSuit to other
			[ CardSuit('DIAMONDS'), 7 ],
			[ CardSuit('DIAMONDS'), '' ],
			[ CardSuit('DIAMONDS'), '7' ],
			[ CardSuit('DIAMONDS'), True ],
			[ CardSuit('DIAMONDS'), False ],
			[ CardSuit('DIAMONDS'), None ],
			# CardSuit to BidSuit - general inequalities
			[ CardSuit('CLUBS'), BidSuit('DIAMONDS') ],
			[ CardSuit('DIAMONDS'), BidSuit('HEARTS') ],
			[ CardSuit('HEARTS'), BidSuit('SPADES') ],
			[ CardSuit('SPADES'), BidSuit('CLUBS') ],
			# CardSuit to BidSuit - no BidSuits should equal a Joker
			[ CardSuit('JOKER'), BidSuit('CLUBS') ],
			[ CardSuit('JOKER'), BidSuit('DIAMONDS') ],
			[ CardSuit('JOKER'), BidSuit('HEARTS') ],
			[ CardSuit('JOKER'), BidSuit('SPADES') ],
			# CardSuit to BidSuit - no BidSuits should equal a No Trumps
			[ CardSuit('CLUBS'), BidSuit('NO_TRUMPS') ],
			[ CardSuit('DIAMONDS'), BidSuit('NO_TRUMPS') ],
			[ CardSuit('HEARTS'), BidSuit('NO_TRUMPS') ],
			[ CardSuit('SPADES'), BidSuit('NO_TRUMPS') ],
			[ CardSuit('JOKER'), BidSuit('NO_TRUMPS') ],
			# CardSuit to BidSuit - no BidSuits should equal a Misere
			[ CardSuit('CLUBS'), BidSuit('MISERE') ],
			[ CardSuit('DIAMONDS'), BidSuit('MISERE') ],
			[ CardSuit('HEARTS'), BidSuit('MISERE') ],
			[ CardSuit('SPADES'), BidSuit('MISERE') ],
			[ CardSuit('JOKER'), BidSuit('MISERE') ],
			# CardSuit to BidSuit - no BidSuits should equal an Open Misere
			[ CardSuit('CLUBS'), BidSuit('OPEN_MISERE') ],
			[ CardSuit('DIAMONDS'), BidSuit('OPEN_MISERE') ],
			[ CardSuit('HEARTS'), BidSuit('OPEN_MISERE') ],
			[ CardSuit('SPADES'), BidSuit('OPEN_MISERE') ],
			[ CardSuit('JOKER'), BidSuit('OPEN_MISERE') ],
			# CardSuit to BidSuit - no BidSuits should equal a Pass
			[ CardSuit('CLUBS'), BidSuit('PASS') ],
			[ CardSuit('DIAMONDS'), BidSuit('PASS') ],
			[ CardSuit('HEARTS'), BidSuit('PASS') ],
			[ CardSuit('SPADES'), BidSuit('PASS') ],
			[ CardSuit('JOKER'), BidSuit('PASS') ],
		]

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert right != left

	def test_gt_lt_ge_le(self):
		less_than_cases = [
			[ CardSuit('CLUBS'), CardSuit('DIAMONDS') ],
			[ CardSuit('DIAMONDS'), CardSuit('HEARTS') ],
			[ CardSuit('HEARTS'), CardSuit('SPADES') ],
			[ CardSuit('SPADES'), CardSuit('JOKER') ],
			[ CardSuit('CLUBS'), CardSuit('HEARTS') ],
			[ CardSuit('HEARTS'), CardSuit('JOKER') ]
		]

		equal_cases = [
			[ CardSuit('CLUBS'), CardSuit('CLUBS') ],
			[ CardSuit('JOKER'), CardSuit('JOKER') ]
		]

		error_cases = [
			[ CardSuit('HEARTS'), 'HEARTS' ],
			[ CardSuit('HEARTS'), 4 ],
			[ CardSuit('HEARTS'), [] ],
			[ CardSuit('HEARTS'), None ],
			[ CardSuit('HEARTS'), True ],
			[ CardSuit('HEARTS'), False ]
		]

		for test_case in less_than_cases:
			left, right = test_case[0], test_case[1]
			assert left < right
			assert left <= right
			assert not left > right
			assert not left >= right

		for test_case in equal_cases:
			left, right = test_case[0], test_case[1]
			assert not left < right
			assert left <= right
			assert not left > right
			assert left >= right

		for test_case in error_cases:
			left, right = test_case[0], test_case[1]

			with pytest.raises(TypeError):
				left < right
			with pytest.raises(TypeError):
				left <= right
			with pytest.raises(TypeError):
				left > right
			with pytest.raises(TypeError):
				left >= right

class TestCard:
	def test_normal_inputs(self):
		card = Card('HEARTS', 'FOUR')
		assert card.suit == CardSuit('HEARTS')
		assert card.rank == CardRank('FOUR')

		card = Card('Spades', 'ace')
		assert card.suit == CardSuit('SPADES')
		assert card.rank == CardRank('ACE')

		card = Card('JOKER')
		assert card.is_joker()
		assert card.suit == CardSuit('JOKER')
		assert not hasattr(card, 'rank')

		card = Card('JOKER', None)
		assert card.is_joker()
		assert card.suit == CardSuit('JOKER')
		assert not hasattr(card, 'rank')

	def test_joker_with_rank(self):
		with pytest.raises(ValueError):
			card = Card('JOKER', 'TWO')

	def test_invalid_inputs(self):
		inputs = [
			[ 'FOUR', 'HEARTS' ],
			[ 'JOKER', 'FOUR' ],
			[ 'FOUR', 'JOKER' ],
			[ None, 'JOKER' ],
			[ 'HEARTS', None ],
			[ None, 'FOUR' ],
			[ 'FOUR', None ],
			[ 'HEARTS', 4 ],
			[ 'HEARTS', True ],
			[ 'HEARTS', False ],
			[ 'HEARTS', [] ],
		]

		for input in inputs:
			with pytest.raises(ValueError):
				card = Card(input[0], input[1])

	def test_is_joker(self):
		card = Card('HEARTS', 'FOUR')
		assert not card.is_joker()

		card = Card('JOKER')
		assert card.is_joker()

class TestCardDunder:
	def test_to_string(self):
		test_cases = [
			# [ param1, param2, str ]
			[ 'HEARTS', 'FOUR', 'Four of Hearts' ],
			[ 'SPADES', 'ACE', 'Ace of Spades' ],
			[ 'JOKER', None, 'Joker' ],
			[ 'DIAMONDS', 'QUEEN', 'Queen of Diamonds' ],
			[ 'CLUBS', 'TEN', 'Ten of Clubs' ],
		]

		for test_case in test_cases:
			assert Card(test_case[0], test_case[1]).to_string() == test_case[2]

	def test_to_minimal_string(self):
		test_cases = [
			# [ param1, param2, str ]
			[ 'HEARTS', 'FOUR', '4H' ],
			[ 'SPADES', 'ACE', 'AS' ],
			[ 'DIAMONDS', 'QUEEN', 'QD' ],
			[ 'CLUBS', 'TEN', 'TC' ],
			[ 'JOKER', None, 'J-' ]
		]

		for test_case in test_cases:
			assert Card(test_case[0], test_case[1]).to_minimal_string() == test_case[2]

	def test_repr(self):
		test_cases = [
			# [ param1, param2, str ]
			[ 'HEARTS', 'FOUR', 'Card(HEARTS, FOUR)' ],
			[ 'SPADES', 'ACE', 'Card(SPADES, ACE)' ],
			[ 'DIAMONDS', 'QUEEN', 'Card(DIAMONDS, QUEEN)' ],
			[ 'CLUBS', 'TEN', 'Card(CLUBS, TEN)' ],
			[ 'JOKER', None, 'Card(JOKER)' ]
		]

		for test_case in test_cases:
			assert repr(Card(test_case[0], test_case[1])) == test_case[2]

	def test_eq_ne(self):
		positive_test_cases = [
			[ Card('DIAMONDS', 'FIVE'), Card('DIAMONDS', 'FIVE') ],
			[ Card('JOKER'), Card('JOKER') ],
			[ Card('JOKER', None), Card('JOKER') ],
		]

		negative_test_cases = [
			[ Card('DIAMONDS', 'FIVE'), Card('DIAMONDS', 'FOUR') ],
			[ Card('DIAMONDS', 'FIVE'), Card('HEARTS', 'FIVE') ],
			[ Card('DIAMONDS', 'FIVE'), Card('SPADES', 'QUEEN') ],
			[ Card('DIAMONDS', 'FIVE'), Card('JOKER') ],
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left == right
			assert right == left
			assert not left != right
			assert not right != left

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert right != left

	def test_gt_lt_ge_le(self):
		less_than_cases = [
			# suit-internal rank tests
			[ Card('HEARTS', 'THREE'), Card('HEARTS', 'FOUR') ],
			[ Card('HEARTS', 'FOUR'), Card('HEARTS', 'FIVE') ],
			[ Card('HEARTS', 'THREE'), Card('HEARTS', 'FIVE') ],
			[ Card('HEARTS', 'TWO'), Card('HEARTS', 'ACE') ],
			[ Card('HEARTS', 'KING'), Card('HEARTS', 'ACE') ],
			# suit tests
			[ Card('CLUBS', 'ACE'), Card('DIAMONDS', 'TWO') ],
			[ Card('DIAMONDS', 'ACE'), Card('HEARTS', 'TWO') ],
			[ Card('HEARTS', 'ACE'), Card('SPADES', 'TWO') ],
			[ Card('SPADES', 'ACE'), Card('JOKER') ]
		]

		equal_cases = [
			[ Card('CLUBS', 'EIGHT'), Card('CLUBS', 'EIGHT') ],
			[ Card('HEARTS', 'TWO'), Card('HEARTS', 'TWO') ],
			[ Card('DIAMONDS', 'JACK'), Card('DIAMONDS', 'JACK') ],
			[ Card('SPADES', 'TWO'), Card('SPADES', 'TWO') ],
			[ Card('JOKER'), Card('JOKER') ]
		]

		error_cases = [
			[ Card('SPADES', 'ACE'), CardSuit('SPADES') ],
			[ Card('SPADES', 'ACE'), CardRank('NINE') ],
			[ Card('SPADES', 'ACE'), 'HEARTS' ],
			[ Card('SPADES', 'ACE'), 4 ],
			[ Card('SPADES', 'ACE'), [] ],
			[ Card('SPADES', 'ACE'), None ],
			[ Card('SPADES', 'ACE'), True ],
			[ Card('SPADES', 'ACE'), False ]
		]

		for test_case in less_than_cases:
			left, right = test_case[0], test_case[1]
			# left - right
			assert left < right
			assert left <= right
			assert not left > right
			assert not left >= right
			# right - left
			assert not right < left
			assert not right <= left
			assert right > left
			assert right >= left

		for test_case in equal_cases:
			left, right = test_case[0], test_case[1]
			# left - right
			assert not left < right
			assert left <= right
			assert not left > right
			assert left >= right
			# right - left
			assert not right < left
			assert right <= left
			assert not right > left
			assert right >= left

		for test_case in error_cases:
			left, right = test_case[0], test_case[1]

			with pytest.raises(TypeError):
				left < right
			with pytest.raises(TypeError):
				left <= right
			with pytest.raises(TypeError):
				left > right
			with pytest.raises(TypeError):
				left >= right
