import pytest

from bid import BidValue, BidSuit, Bid
from card import CardSuit

class TestBidValue:
	def test_valid_inputs(self):
		inputs = ['6', '7', '8', '9', '10', 6, 7, 8, 9, 10]

		for input in inputs:
			bid_value = BidValue(input)
			assert bid_value.value == str(input)

	def test_invalid_inputs(self):
		inputs = ['SIX', '', '6 ', 11, 6.01, True, False, None]

		for input in inputs:
			with pytest.raises(ValueError):
				bid_value = BidValue(input)

class TestBidValueDunder:
	def test_to_string(self):
		inputs = ['6', '7', '8', '9', '10', 6, 7, 8, 9, 10]

		for input in inputs:
			assert BidValue(input).to_string() == str(input)

	def test_to_minimal_string(self):
		inputs = ['6', '7', '8', '9', 6, 7, 8, 9]

		for input in inputs:
			assert BidValue(input).to_minimal_string() == str(input)

		assert BidValue('10').to_minimal_string() == BidValue(10).to_minimal_string() == 'T'

		# check that all minimal strings are unique
		minimal_strings = [ BidValue(value).to_minimal_string() for value in BidValue.values ]
		assert len(minimal_strings) == len(set(minimal_strings))

	def test_repr(self):
		inputs = ['6', '7', '8', '9', '10', 6, 7, 8, 9, 10]

		for input in inputs:
			assert repr(BidValue(input)) == f'BidValue({input})'

	def test_eq_ne(self):
		# positive test cases
		# BidValue to BidValue comparison
		inputs = [
			[ BidValue('6'), BidValue('6') ],
			[ BidValue('6'), BidValue(6) ]
		]

		for input in inputs:
			left, right = input[0], input[1]
			assert left == right
			assert right == left
			assert not left != right
			assert not right != left

		# BidValue to str/int comparison
		inputs = ['6', '7', '8', '9', '10', 6, 7, 8, 9, 10]

		for input in inputs:
			left, right = BidValue(input), input
			assert left == right
			assert right == left
			assert not left != right
			assert not right != left

		# negative test cases
		# BidValue to BidValue comparison
		inputs = [
			[ BidValue('6'), BidValue('7') ],
			[ BidValue('6'), BidValue(7) ]
		]

		for input in inputs:
			left, right = input[0], input[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert  right != left

		# BidValue to str/int comparison
		inputs = [
			[ '6', '7' ],
			[ '6', 7 ],
			[ 6, '7' ],
			[ 6, 7 ]
		]

		for input in inputs:
			left, right = BidValue(input[0]), input[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert right != left

class TestBidSuit:
	def test_valid_inputs(self):
		inputs = [
			'CLUBS', 'diamonds', 'Hearts', 'SpAdEs',   # different capitalization
			'No_trumps', 'no trumps',   # space or underscore
			'MISERE', 'OPEN_MISERE', 'OPEN MISERE', 'PASS'
		]

		for input in inputs:
			assert BidSuit(input).suit == input.replace(' ', '_').upper()

	def test_invalid_inputs(self):
		inputs = ['CLUBS ', '', True, False, None, 'NO-TRUMPS', 'NOTRUMPS', 'OPENMISERE', 'CLU_BS', 'CLU BS']

		for input in inputs:
			with pytest.raises(ValueError):
				bid_suit = BidSuit(input)

class TestBidSuitDunder:
	def test_to_string(self):
		inputs = ['CLUBS', 'diamonds', 'Hearts', 'SpAdEs', 'No Trumps', 'misere', 'OPEN_misere']

		for input in inputs:
			assert BidSuit(input).to_string() == input.replace('_', ' ').title()

	def test_to_minimal_string(self):
		inputs = ['CLUBS', 'diamonds', 'Hearts', 'SpAdEs', 'No Trumps', 'misere', 'OPEN_misere']

		for input in inputs:
			assert BidSuit(input).to_minimal_string() == input[0].upper()

		# check that all minimal strings are unique
		minimal_strings = [ BidSuit(suit).to_minimal_string() for suit in BidSuit.suits ]
		assert len(minimal_strings) == len(set(minimal_strings))

	def test_repr(self):
		inputs = ['CLUBS', 'diamonds', 'Hearts', 'SpAdEs', 'No Trumps', 'misere', 'OPEN_misere']

		for input in inputs:
			expected = input.replace(' ', '_').upper()
			assert repr(BidSuit(input)) == f'BidSuit({expected})'

	def test_eq_ne(self):
		positive_test_cases = [
			# BidSuit to Bidsuit
			[ BidSuit('CLUBS'), BidSuit('CLUBS') ],
			[ BidSuit('CLUBS'), BidSuit('Clubs') ],
			[ BidSuit('CLUBS'), BidSuit('clubs') ],
			[ BidSuit('cLuBs'), BidSuit('CLUBS') ],
			[ BidSuit('CLUBS'), BidSuit('CLUBS') ],
			[ BidSuit('DIAMONDS'), BidSuit('diamonds') ],
			[ BidSuit('hearts'), BidSuit('HEARTS') ],
			[ BidSuit('SPADES'), BidSuit('spades') ],
			[ BidSuit('no_trumps'), BidSuit('NO_TRUMPS') ],
			[ BidSuit('MISERE'), BidSuit('misere') ],
			[ BidSuit('open_misere'), BidSuit('OPEN_MISERE') ],
			[ BidSuit('PASS'), BidSuit('pass') ],
			# BidSuit to str
			[ BidSuit('CLUBS'), 'CLUBS' ],
			[ BidSuit('CLUBS'), 'Clubs' ],
			[ BidSuit('CLUBS'), 'clubs' ],
			[ BidSuit('cLuBs'), 'CLUBS' ],
			[ BidSuit('CLUBS'), 'CLUBS' ],
			[ BidSuit('DIAMONDS'), 'diamonds' ],
			[ BidSuit('hearts'), 'HEARTS' ],
			[ BidSuit('SPADES'), 'spades' ],
			[ BidSuit('no_trumps'), 'NO_TRUMPS' ],
			[ BidSuit('MISERE'), 'misere' ],
			[ BidSuit('open_misere'), 'OPEN_MISERE' ],
			[ BidSuit('PASS'), 'pass' ],
			# BidSuit to CardSuit
			[ BidSuit('CLUBS'), CardSuit('CLUBS') ],
			[ BidSuit('DIAMONDS'), CardSuit('DIAMONDS') ],
			[ BidSuit('HEARTS'), CardSuit('HEARTS') ],
			[ BidSuit('SPADES'), CardSuit('SPADES') ],
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left == right
			assert right == left
			assert not left != right
			assert not right != left


		negative_test_cases = [
			# BidSuit to BidSuit
			[ BidSuit('CLUBS'), BidSuit('HEARTS') ],
			[ BidSuit('CLUBS'), BidSuit('spades') ],
			[ BidSuit('NO_TRUMPS'), 'NO TRUMPS' ],
			[ BidSuit('NO_TRUMPS'), 'No Trumps' ],
			[ BidSuit('OPEN_MISERE'), 'open misere' ],
			[ BidSuit('OPEN_MISERE'), 'open-misere' ],
			# BidSuit to str
			[ BidSuit('CLUBS'), 'HEARTS' ],
			[ BidSuit('CLUBS'), 'spades' ],
			[ BidSuit('NO_TRUMPS'), 'NO TRUMPS' ],
			[ BidSuit('NO_TRUMPS'), 'No Trumps' ],
			[ BidSuit('OPEN_MISERE'), 'open misere' ],
			[ BidSuit('OPEN_MISERE'), 'open-misere' ],
			[ BidSuit('CLUBS'), '' ],
			[ BidSuit('CLUBS'), True ],
			[ BidSuit('CLUBS'), False ],
			[ BidSuit('CLUBS'), None ],
			# BidSuit to CardSuit - general inequalities
			[ BidSuit('CLUBS'), CardSuit('DIAMONDS') ],
			[ BidSuit('DIAMONDS'), CardSuit('HEARTS') ],
			[ BidSuit('HEARTS'), CardSuit('SPADES') ],
			[ BidSuit('SPADES'), CardSuit('CLUBS') ],
			# BidSuit to CardSuit - no BidSuits should equal a Joker
			[ BidSuit('CLUBS'), CardSuit('JOKER') ],
			[ BidSuit('DIAMONDS'), CardSuit('JOKER') ],
			[ BidSuit('HEARTS'), CardSuit('JOKER') ],
			[ BidSuit('SPADES'), CardSuit('JOKER') ],
			# BidSuit to CardSuit - no CardSuits should equal a No Trumps
			[ BidSuit('NO_TRUMPS'), CardSuit('CLUBS') ],
			[ BidSuit('NO_TRUMPS'), CardSuit('DIAMONDS') ],
			[ BidSuit('NO_TRUMPS'), CardSuit('HEARTS') ],
			[ BidSuit('NO_TRUMPS'), CardSuit('SPADES') ],
			[ BidSuit('NO_TRUMPS'), CardSuit('JOKER') ],
			# BidSuit to CardSuit - no CardSuits should equal a Misere
			[ BidSuit('MISERE'), CardSuit('CLUBS') ],
			[ BidSuit('MISERE'), CardSuit('DIAMONDS') ],
			[ BidSuit('MISERE'), CardSuit('HEARTS') ],
			[ BidSuit('MISERE'), CardSuit('SPADES') ],
			[ BidSuit('MISERE'), CardSuit('JOKER') ],
			# BidSuit to CardSuit - no CardSuits should equal an Open Misere
			[ BidSuit('OPEN_MISERE'), CardSuit('CLUBS') ],
			[ BidSuit('OPEN_MISERE'), CardSuit('DIAMONDS') ],
			[ BidSuit('OPEN_MISERE'), CardSuit('HEARTS') ],
			[ BidSuit('OPEN_MISERE'), CardSuit('SPADES') ],
			[ BidSuit('OPEN_MISERE'), CardSuit('JOKER') ],
			# BidSuit to CardSuit - no CardSuits should equal a Pass
			[ BidSuit('PASS'), CardSuit('CLUBS') ],
			[ BidSuit('PASS'), CardSuit('DIAMONDS') ],
			[ BidSuit('PASS'), CardSuit('HEARTS') ],
			[ BidSuit('PASS'), CardSuit('SPADES') ],
			[ BidSuit('PASS'), CardSuit('JOKER') ]
		]

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert right != left

class TestBid:
	def setup_method(self, method):
		# set up a bunch of Bids that cover all bases
		# we do this by making a Bid out of all combinations of the following values

		player_ids = [ None, 1, '2', 34567, '89101112131415', '586d325d-b14d-417e-873c-4f6189aef722', '586d325db14d417e873c4f6189aef722', 'TheLegend27', 'with-hyphen', 'with_underscore', 'with space' ]

		independent_suits = [ 'MISERE', 'OPEN_MISERE', 'pass', 'open MISERE' ]

		dependent_suits = [ 'CLUBS', 'diamonds', 'HeArTs', 'SPADES', 'NO_TRUMPS', 'no trumps' ]
		dependent_values = [ '6', '7', '8', '9', '10', 6, 7, 8, 9, 10 ]

		self.valid_dependent_inputs = [ [player_id, suit, value] for player_id in player_ids for suit in dependent_suits for value in dependent_values ]
		self.valid_independent_inputs = [ [player_id, suit, None] for player_id in player_ids for suit in independent_suits  ]
		self.valid_inputs = self.valid_dependent_inputs + self.valid_independent_inputs

	def test_valid_inputs(self):
		# dependent suits
		for test_case in self.valid_dependent_inputs:
			player_id, suit, value = test_case[0], test_case[1], test_case[2]
			bid = Bid(suit, value=value, player_id=player_id)
			assert bid.suit == suit.upper().replace(' ', '_')
			assert bid.value == value
			assert bid.player_id == player_id

		# independent suits
		for test_case in self.valid_independent_inputs:
			player_id, suit, value = test_case[0], test_case[1], test_case[2]   # value will always be none
			bid = Bid(suit, player_id=player_id)
			assert bid.suit == suit.upper().replace(' ', '_')
			assert not hasattr(bid, 'value')
			assert bid.player_id == player_id

	def test_invalid_inputs(self):
		# invalid values should generally be handled in BidSuit/BidValue
		inputs = [
			# parameters swapped
			[ 'SIX', 'HEARTS' ],
			[ '7', 'DIAMONDS'],
			[ 8, 'HEARTS' ],
			# independent suits with values
			[ 'MISERE', '6' ],
			[ 'OPEN_MISERE', '7' ],
			[ 'PASS', '8' ],
			# no suit
			[ None, '8' ],
			# value too high or low
			[ 'HEARTS', 5 ],
			[ 'HEARTS', 11 ],
			# misc invalid values
			[ 'HEARTS', True ],
			[ 'HEARTS', False ],
			[ 'HEARTS', [] ],
			[ True, '8' ],
			[ False, '8' ],
			[ [], '8' ],
		]

		for test_case in inputs:
			suit, value = test_case[0], test_case[1]
			with pytest.raises(ValueError):
				bid = Bid(suit, value)

	def test_compare(self):
		hierarchy = [
			Bid('PASS'),
			Bid('SPADES', '6'), Bid('CLUBS', '6'), Bid('DIAMONDS', '6'), Bid('HEARTS', '6'), Bid('NO_TRUMPS', '6'),
			Bid('SPADES', '7'), Bid('CLUBS', '7'), Bid('DIAMONDS', '7'), Bid('HEARTS', '7'), Bid('NO_TRUMPS', '7'),
			Bid('MISERE'),
			Bid('SPADES', '8'), Bid('CLUBS', '8'), Bid('DIAMONDS', '8'), Bid('HEARTS', '8'), Bid('NO_TRUMPS', '8'),
			Bid('SPADES', '9'), Bid('CLUBS', '9'), Bid('DIAMONDS', '9'), Bid('HEARTS', '9'), Bid('NO_TRUMPS', '9'),
			Bid('SPADES', '10'), Bid('CLUBS', '10'), Bid('DIAMONDS', '10'),
			Bid('OPEN_MISERE'),
			Bid('HEARTS', '10'), Bid('NO_TRUMPS', '10')
		]

		for i in range(len(hierarchy) - 1):
			assert hierarchy[i]._compare(hierarchy[i + 1]) == '<'
			assert hierarchy[i + 1]._compare(hierarchy[i]) == '>'
		for bid in hierarchy:
			assert bid._compare(bid) == '='

		# make sure player_ids don't break anything
		assert Bid('SPADES', 7)._compare(Bid('SPADES', 8, player_id='123')) == '<'
		assert Bid('SPADES', 8)._compare(Bid('SPADES', 7, player_id='999')) == '>'
		assert Bid('MISERE')._compare(Bid('MISERE', player_id=555)) == '='
		assert Bid('SPADES', 7, player_id='123')._compare(Bid('SPADES', 8)) == '<'
		assert Bid('SPADES', 8, player_id='999')._compare(Bid('SPADES', 7)) == '>'
		assert Bid('MISERE', player_id=555)._compare(Bid('MISERE')) == '='

		# _comparing with non-Bids
		bid = Bid('HEARTS', 8)
		others = [ None, '', 'HEARTS', 1, [] ]

		for other in others:
			with pytest.raises(ValueError):
				bid._compare(other)

class TestBidDunder:
	def setup_method(self, method):
		self.bids = [
			Bid('PASS'), Bid('CLUBS', 6), Bid('DIAMONDS', 7), Bid('MISERE'), Bid('NO_TRUMPS', 8), Bid('HEARTS', 9), Bid('OPEN_MISERE'), Bid('NO_TRUMPS', 10),

			Bid('PASS', player_id=123), Bid('CLUBS', 6, player_id='123'), Bid('DIAMONDS', 7, player_id=123), Bid('MISERE', player_id='123'), Bid('NO_TRUMPS', 8, player_id=123), Bid('HEARTS', 9, player_id='123'), Bid('OPEN_MISERE', player_id=123), Bid('NO_TRUMPS', 10, player_id='123'),
		]

	def test_to_string(self):
		strings = [
			'Pass', '6 Clubs', '7 Diamonds', 'Misere', '8 No Trumps', '9 Hearts', 'Open Misere', '10 No Trumps',
			'123: Pass', '123: 6 Clubs', '123: 7 Diamonds', '123: Misere', '123: 8 No Trumps', '123: 9 Hearts', '123: Open Misere', '123: 10 No Trumps',
		]

		for bid, string in zip(self.bids, strings):
			assert bid.to_string() == string

	def test_to_minimal_string(self):
		minimal_strings = [
			'P-', '6C', '7D', 'M-', '8N', '9H', 'O-', 'TN',
			'P-', '6C', '7D', 'M-', '8N', '9H', 'O-', 'TN',
		]

		for bid, minimal_string in zip(self.bids, minimal_strings):
			assert bid.to_minimal_string() == minimal_string

	def test_repr(self):
		reprs = [
			'Bid(PASS, player_id=None)', 'Bid(CLUBS, 6, player_id=None)', 'Bid(DIAMONDS, 7, player_id=None)', 'Bid(MISERE, player_id=None)', 'Bid(NO_TRUMPS, 8, player_id=None)', 'Bid(HEARTS, 9, player_id=None)', 'Bid(OPEN_MISERE, player_id=None)', 'Bid(NO_TRUMPS, 10, player_id=None)',
			'Bid(PASS, player_id=123)', 'Bid(CLUBS, 6, player_id=123)', 'Bid(DIAMONDS, 7, player_id=123)', 'Bid(MISERE, player_id=123)', 'Bid(NO_TRUMPS, 8, player_id=123)', 'Bid(HEARTS, 9, player_id=123)', 'Bid(OPEN_MISERE, player_id=123)', 'Bid(NO_TRUMPS, 10, player_id=123)',
		]

		for bid, _repr in zip(self.bids, reprs):
			assert repr(bid) == _repr

	def test_eq_ne(self):
		positive_test_cases = [
			[ Bid('SPADES', '8'), Bid('SPADES', 8) ],
			[ Bid('HEARTS', '10'), Bid('HEARTS', 10) ],
			[ Bid('MISERE'), Bid('MISERE') ],
			[ Bid('OPEN_MISERE'), Bid('OPEN_MISERE') ],
			[ Bid('PASS'), Bid('PASS') ],
			# with player IDs
			[ Bid('SPADES', '8'), Bid('SPADES', 8, player_id='123') ],
			[ Bid('HEARTS', '10', player_id=123), Bid('HEARTS', 10, player_id='123') ],
			[ Bid('MISERE'), Bid('MISERE', player_id='123') ],
			[ Bid('OPEN_MISERE', player_id='456'), Bid('OPEN_MISERE', player_id='123') ],
			[ Bid('PASS'), Bid('PASS', player_id='123') ],
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left == right
			assert right == left
			assert not left != right
			assert not right != left


		negative_test_cases = [
			[ Bid('SPADES', '8'), Bid('SPADES', 9) ],
			[ Bid('HEARTS', '10'), Bid('SPADES', 10) ],
			[ Bid('MISERE'), Bid('OPEN_MISERE') ],
			[ Bid('OPEN_MISERE'), Bid('PASS') ],
			[ Bid('PASS'), Bid('MISERE') ],
			# with player IDs
			[ Bid('SPADES', '8'), Bid('SPADES', 9, player_id='123') ],
			[ Bid('HEARTS', '10'), Bid('SPADES', 10, player_id='123') ],
			[ Bid('MISERE'), Bid('OPEN_MISERE', player_id='123') ],
			[ Bid('OPEN_MISERE'), Bid('PASS', player_id='123') ],
			[ Bid('PASS'), Bid('MISERE', player_id='123') ],
		]

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left == right
			assert not right == left
			assert left != right
			assert right != left

	def test_strict_equals(self):
		positive_test_cases = [
			[ Bid('SPADES', '8'), Bid('SPADES', 8) ],
			[ Bid('HEARTS', '10'), Bid('HEARTS', 10) ],
			[ Bid('MISERE'), Bid('MISERE') ],
			[ Bid('OPEN_MISERE'), Bid('OPEN_MISERE') ],
			[ Bid('PASS'), Bid('PASS') ],
		]

		for test_case in positive_test_cases:
			left, right = test_case[0], test_case[1]
			assert left.strict_equals(right)
			assert right.strict_equals(left)


		negative_test_cases = [
			[ Bid('SPADES', '8'), Bid('SPADES', 9) ],
			[ Bid('HEARTS', '10'), Bid('SPADES', 10) ],
			[ Bid('MISERE'), Bid('OPEN_MISERE') ],
			[ Bid('OPEN_MISERE'), Bid('PASS') ],
			[ Bid('PASS'), Bid('MISERE') ],
			# same bid but different  player IDs
			[ Bid('SPADES', '8'), Bid('SPADES', 8, player_id='123') ],
			[ Bid('HEARTS', '10', player_id=123), Bid('HEARTS', 10, player_id='123') ],
			[ Bid('MISERE'), Bid('MISERE', player_id='123') ],
			[ Bid('OPEN_MISERE', player_id='456'), Bid('OPEN_MISERE', player_id='123') ],
			[ Bid('PASS'), Bid('PASS', player_id='123') ],
			# different bids with different with player IDs
			[ Bid('SPADES', '8'), Bid('SPADES', 9, player_id='123') ],
			[ Bid('HEARTS', '10'), Bid('SPADES', 10, player_id='123') ],
			[ Bid('MISERE'), Bid('OPEN_MISERE', player_id='123') ],
			[ Bid('OPEN_MISERE'), Bid('PASS', player_id='123') ],
			[ Bid('PASS'), Bid('MISERE', player_id='123') ],
		]

		for test_case in negative_test_cases:
			left, right = test_case[0], test_case[1]
			assert not left.strict_equals(right)
			assert not right.strict_equals(left)

	def test_gt_lt(self):
		hierarchy = [
			Bid('PASS'),
			Bid('SPADES', '6'), Bid('CLUBS', '6'), Bid('DIAMONDS', '6'), Bid('HEARTS', '6'), Bid('NO_TRUMPS', '6'),
			Bid('SPADES', '7'), Bid('CLUBS', '7'), Bid('DIAMONDS', '7'), Bid('HEARTS', '7'), Bid('NO_TRUMPS', '7'),
			Bid('MISERE'),
			Bid('SPADES', '8'), Bid('CLUBS', '8'), Bid('DIAMONDS', '8'), Bid('HEARTS', '8'), Bid('NO_TRUMPS', '8'),
			Bid('SPADES', '9'), Bid('CLUBS', '9'), Bid('DIAMONDS', '9'), Bid('HEARTS', '9'), Bid('NO_TRUMPS', '9'),
			Bid('SPADES', '10'), Bid('CLUBS', '10'), Bid('DIAMONDS', '10'),
			Bid('OPEN_MISERE'),
			Bid('HEARTS', '10'), Bid('NO_TRUMPS', '10')
		]

		for i in range(len(hierarchy) - 1):
			assert hierarchy[i] < hierarchy[i + 1]
			assert hierarchy[i + 1] > hierarchy[i]

		# other types
		bid = Bid('SPADES', 7)
		others = [ 1, '1', True, False, None, [], BidSuit('CLUBS'), BidValue('9') ]

		for other in others:
			with pytest.raises(TypeError):
				bid > other
			with pytest.raises(TypeError):
				bid < other

	def test_ge_le(self):
		hierarchy = [
			Bid('PASS'),
			Bid('SPADES', '6'), Bid('CLUBS', '6'), Bid('DIAMONDS', '6'), Bid('HEARTS', '6'), Bid('NO_TRUMPS', '6'),
			Bid('SPADES', '7'), Bid('CLUBS', '7'), Bid('DIAMONDS', '7'), Bid('HEARTS', '7'), Bid('NO_TRUMPS', '7'),
			Bid('MISERE'),
			Bid('SPADES', '8'), Bid('CLUBS', '8'), Bid('DIAMONDS', '8'), Bid('HEARTS', '8'), Bid('NO_TRUMPS', '8'),
			Bid('SPADES', '9'), Bid('CLUBS', '9'), Bid('DIAMONDS', '9'), Bid('HEARTS', '9'), Bid('NO_TRUMPS', '9'),
			Bid('SPADES', '10'), Bid('CLUBS', '10'), Bid('DIAMONDS', '10'),
			Bid('OPEN_MISERE'),
			Bid('HEARTS', '10'), Bid('NO_TRUMPS', '10')
		]

		for i in range(len(hierarchy) - 1):
			assert hierarchy[i] <= hierarchy[i + 1]
			assert hierarchy[i + 1] >= hierarchy[i]
		for bid in hierarchy:
			assert bid <= bid
			assert bid >= bid

		# other types
		bid = Bid('SPADES', 7)
		others = [ 1, '1', True, False, None, [], BidSuit('CLUBS'), BidValue('9') ]

		for other in others:
			with pytest.raises(TypeError):
				bid >= other
			with pytest.raises(TypeError):
				bid <= other
