import pytest

from trick import Trick
from card import Card

class TestTrick:
	def test_init(self):
		trick = Trick('0123456789')
		assert trick.leader_id == '0123456789'
		assert trick.cards == []

	def test_append(self):
		trick = Trick('12345')
		assert len(trick.cards) == 0

		trick.append(Card('DIAMONDS', 'SEVEN'))
		assert len(trick.cards) == 1

		trick.append(Card('DIAMONDS', 'JACK'))
		assert len(trick.cards) == 2

		trick.append(Card('SPADES', 'FIVE'))
		assert len(trick.cards) == 3

		trick.append(Card('DIAMONDS', 'FIVE'))
		assert len(trick.cards) == 4

		with pytest.raises(ValueError):
			trick.append(Card('HEARTS', 'QUEEN'))
		assert len(trick.cards) == 4

		invalid_inputs = [ None, True, False, '1', 1 ]

		for input in invalid_inputs:
			with pytest.raises(TypeError):
				trick.append(input)

	def test_str(self):
		trick = Trick('12345')
		assert str(trick) == 'Trick leader: 12345; Cards: '

		trick.append(Card('DIAMONDS', 'SEVEN'))
		assert str(trick) == 'Trick leader: 12345; Cards: Seven of Diamonds'

		trick.append(Card('DIAMONDS', 'JACK'))
		assert str(trick) == 'Trick leader: 12345; Cards: Seven of Diamonds, Jack of Diamonds'

		trick.append(Card('SPADES', 'FIVE'))
		assert str(trick) == 'Trick leader: 12345; Cards: Seven of Diamonds, Jack of Diamonds, Five of Spades'

		trick.append(Card('DIAMONDS', 'FIVE'))
		assert str(trick) == 'Trick leader: 12345; Cards: Seven of Diamonds, Jack of Diamonds, Five of Spades, Five of Diamonds'

	def test_repr(self):
		trick = Trick('12345')
		assert repr(trick) == 'Trick(leader=12345, cards=[])'

		trick.append(Card('DIAMONDS', 'SEVEN'))
		assert repr(trick) == 'Trick(leader=12345, cards=[7D])'

		trick.append(Card('DIAMONDS', 'JACK'))
		assert repr(trick) == 'Trick(leader=12345, cards=[7D, JD])'

		trick.append(Card('SPADES', 'FIVE'))
		assert repr(trick) == 'Trick(leader=12345, cards=[7D, JD, 5S])'

		trick.append(Card('DIAMONDS', 'FIVE'))
		assert repr(trick) == 'Trick(leader=12345, cards=[7D, JD, 5S, 5D])'

	def test_len(self):
		trick = Trick('12345')
		assert len(trick) == 0

		trick.append(Card('DIAMONDS', 'SEVEN'))
		assert len(trick) == 1

		trick.append(Card('DIAMONDS', 'JACK'))
		assert len(trick) == 2

		trick.append(Card('SPADES', 'FIVE'))
		assert len(trick) == 3

		trick.append(Card('DIAMONDS', 'FIVE'))
		assert len(trick) == 4
