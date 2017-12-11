import pytest

from player import Player

class TestPlayer:
	def test_inputs(self):
		player_ids = [ 1, '2', 34567, '89101112131415', '586d325d-b14d-417e-873c-4f6189aef722', '586d325db14d417e873c4f6189aef722', 'TheLegend27', 'with-hyphen', 'with_underscore', 'with space' ]

		names = [ 'abc', 'Def', 'Ghi Jkl', 'mnopq_rst-uv', '`~!@#$%^&*()_+1234567890-=|\\[]{};\':\",./<>?`' ]

		test_cases = [ [player_id, name] for player_id in player_ids for name in names ]

		for test_case in test_cases:
			player_id, name = test_case[0], test_case[1]
			player = Player(player_id, name)
			assert player.id == player_id
			assert player.name == name

	def test_str(self):
		test_cases = [
			[ Player('1', 'Smitty Werbenjagermanjensen'), 'Smitty Werbenjagermanjensen' ],
			[ Player(123, 'Smitty Werbenjagermanjensen'), 'Smitty Werbenjagermanjensen' ],
			[ Player('1', 'Cassidy'), 'Cassidy' ],
		]

		for test_case in test_cases:
			player, name = test_case[0], test_case[1]
			assert str(player) == name

	def test_repr(self):
		test_cases = [
			[ Player('1', 'Smitty Werbenjagermanjensen'), 'Player(1)' ],
			[ Player(123, 'Smitty Werbenjagermanjensen'), 'Player(123)' ],
			[ Player('123', 'Cassidy'), 'Player(123)' ],
		]

		for test_case in test_cases:
			player, repr_ = test_case[0], test_case[1]
			assert repr(player) == repr_

	def test_eq_ne(self):
		positive_test_cases = [
			[ Player(1, 'Name'), Player(1, 'Name') ],
			[ Player(1, 'Name'), Player(1, 'Other Name') ],
			[ Player('123', 'Name'), Player('123', 'Name') ],
			[ Player('123', 'Name'), Player('123', 'Other Name') ],
		]

		negative_test_cases = [
			[ Player(1, 'Name'), Player(2, 'Name') ],
			[ Player(1, 'Name'), Player('1', 'Other Name') ],
			[ Player('123', 'Name'), Player('124', 'Name') ],
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
