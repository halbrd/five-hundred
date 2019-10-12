import pytest
from collections import OrderedDict

from hand import Hand
from bid import Bid
from card import Card
from kitty import Kitty

PLAYER_IDS = [ 123, '456', 'abc', '0-f' ]

def setup_methods():
	r = {}

	# Random hand
	# for tests that apply to any arrangement of cards
	r['hand_random'] = Hand(PLAYER_IDS)

	# Hand (not dealt)
	r['hand_no_deal'] = Hand(PLAYER_IDS, deal=False)

	# Hand 1
	# for more specific testing
	'''
	Hand 1:
	123: JD 6D TC QS 5S 5H 7S 6C 9D 8H
	456: 7H KH TH JH 6S AD 5C 9H 4D AS
	abc: 8D 9S 7C 6H 5D AH 8S JC QC QD
	0-f: TD J- JS 7D AC QH 9C 8C KC KD
	Kitty: TS KS 4H
	'''
	cards = [Card('DIAMONDS', 'JACK'), Card('DIAMONDS', 'SIX'), Card('CLUBS', 'TEN'), Card('SPADES', 'QUEEN'), Card('SPADES', 'FIVE'), Card('HEARTS', 'FIVE'), Card('SPADES', 'SEVEN'), Card('CLUBS', 'SIX'), Card('DIAMONDS', 'NINE'), Card('HEARTS', 'EIGHT'), Card('HEARTS', 'SEVEN'), Card('HEARTS', 'KING'), Card('HEARTS', 'TEN'), Card('HEARTS', 'JACK'), Card('SPADES', 'SIX'), Card('DIAMONDS', 'ACE'), Card('CLUBS', 'FIVE'), Card('HEARTS', 'NINE'), Card('DIAMONDS', 'FOUR'), Card('SPADES', 'ACE'), Card('DIAMONDS', 'EIGHT'), Card('SPADES', 'NINE'), Card('CLUBS', 'SEVEN'), Card('HEARTS', 'SIX'), Card('DIAMONDS', 'FIVE'), Card('HEARTS', 'ACE'), Card('SPADES', 'EIGHT'), Card('CLUBS', 'JACK'), Card('CLUBS', 'QUEEN'), Card('DIAMONDS', 'QUEEN'), Card('DIAMONDS', 'TEN'), Card('JOKER'), Card('SPADES', 'JACK'), Card('DIAMONDS', 'SEVEN'), Card('CLUBS', 'ACE'), Card('HEARTS', 'QUEEN'), Card('CLUBS', 'NINE'), Card('CLUBS', 'EIGHT'), Card('CLUBS', 'KING'), Card('DIAMONDS', 'KING'), Card('SPADES', 'TEN'), Card('SPADES', 'KING'), Card('HEARTS', 'FOUR')]

	hand = Hand(PLAYER_IDS, deal=False)

	hand.hands[PLAYER_IDS[0]] = cards[:10]
	hand.hands[PLAYER_IDS[1]] = cards[10:20]
	hand.hands[PLAYER_IDS[2]] = cards[20:30]
	hand.hands[PLAYER_IDS[3]] = cards[30:40]
	hand.kitty = Kitty(cards=cards[40:43])

	r['hand_1'] = hand

	return r

class TestHand:
	def setup_method(self, method):
		for name, value in setup_methods().items():
			setattr(self, name, value)

	def test_inputs(self):
		hand = self.hand_random

		assert hand.dealer_id == PLAYER_IDS[-1]
		assert list(hand.hands.keys()) == PLAYER_IDS
		assert all([len(hand) == 10 for hand in hand.hands.values()])
		assert len(hand.kitty) == 3
		assert hand.bids == []
		assert hand.tricks == []

	def test_deal(self):
		hand = self.hand_no_deal

		assert len(hand.deck) == 43
		assert all([hand == [] for hand in hand.hands.values()])
		assert hand.kitty is None

		hand.deal()

		assert len(hand.deck) == 0
		assert all([len(hand) == 10 for hand in hand.hands.values()])
		assert len(hand.kitty) == 3

	

class TestHandDunder:
	def setup_method(self, method):
		for name, value in setup_methods().items():
			setattr(self, name, value)

	def test_str_basic(self):
		hand = Hand(PLAYER_IDS)
		assert str(hand) == 'Bids:\nTricks:'

	def test_str_bidding(self):
		hand = self.hand_1

		hand.accept_bid(Bid('SPADES', '6', player_id=PLAYER_IDS[0]))
		hand.accept_bid(Bid('CLUBS', '6', player_id=PLAYER_IDS[1]))
		hand.accept_bid(Bid('HEARTS', '6', player_id=PLAYER_IDS[2]))
		hand.accept_bid(Bid('NO_TRUMPS', '7', player_id=PLAYER_IDS[3]))
		hand.accept_bid(Bid('MISERE', player_id=PLAYER_IDS[0]))
		hand.accept_bid(Bid('PASS', player_id=PLAYER_IDS[1]))
		hand.accept_bid(Bid('PASS', player_id=PLAYER_IDS[2]))
		hand.accept_bid(Bid('SPADES', '8', player_id=PLAYER_IDS[3]))
		hand.accept_bid(Bid('SPADES', '9', player_id=PLAYER_IDS[0]))
		hand.accept_bid(Bid('CLUBS', '9', player_id=PLAYER_IDS[3]))

		assert str(hand) == \
'''Bids:
  123: 6 Spades
  456: 6 Clubs
  abc: 6 Hearts
  0-f: 7 No Trumps
  123: Misere
  456: Pass
  abc: Pass
  0-f: 8 Spades
  123: 9 Spades
  0-f: 9 Clubs
Tricks:'''

	# def test_str_playing(self):
	# 	# TODO
	# 	hand = self.hand_1
    #
	# 	hand.accept_bid(Bid('SPADES', '6', player_id=PLAYER_IDS[0]))
	# 	hand.accept_bid(Bid('CLUBS', '6', player_id=PLAYER_IDS[1]))
	# 	hand.accept_bid(Bid('HEARTS', '6', player_id=PLAYER_IDS[2]))
	# 	hand.accept_bid(Bid('NO_TRUMPS', '7', player_id=PLAYER_IDS[3]))
	# 	hand.accept_bid(Bid('MISERE', player_id=PLAYER_IDS[0]))
	# 	hand.accept_bid(Bid('PASS', player_id=PLAYER_IDS[1]))
	# 	hand.accept_bid(Bid('PASS', player_id=PLAYER_IDS[2]))
	# 	hand.accept_bid(Bid('SPADES', '8', player_id=PLAYER_IDS[3]))
	# 	hand.accept_bid(Bid('SPADES', '9', player_id=PLAYER_IDS[0]))
	# 	hand.accept_bid(Bid('CLUBS', '9', player_id=PLAYER_IDS[3]))
	# 	hand.accept_bid(Bid('PASS', player_id=PLAYER_IDS[0]))
    #
	# 	hand.accept_card(Card('CLUBS', 'ACE'), PLAYER_IDS[3])
	# 	hand.accept_card(Card('CLUBS', 'SIX'), PLAYER_IDS[0])
	# 	hand.accept_card(Card('CLUBS', 'FIVE'), PLAYER_IDS[1])
	# 	hand.accept_card(Card('CLUBS', 'SEVEN'), PLAYER_IDS[2])
	# 	hand.accept_card(Card('CLUBS', 'KING'), PLAYER_IDS[3])
	# 	hand.accept_card(Card('CLUBS', 'TEN'), PLAYER_IDS[0])
	# 	hand.accept_card(Card('SPADES', 'SIX'), PLAYER_IDS[1])
	# 	hand.accept_card(Card('CLUBS', 'JACK'), PLAYER_IDS[2])
	# 	hand.accept_card(Card('DIAMONDS', 'SEVEN'), PLAYER_IDS[3])
	# 	hand.accept_card(Card('DIAMONDS', 'NINE'), PLAYER_IDS[0])
	# 	hand.accept_card(Card('DIAMONDS', 'FOUR'), PLAYER_IDS[1])
	# 	hand.accept_card(Card('DIAMONDS', 'FIVE'), PLAYER_IDS[2])
	# 	hand.accept_card(Card('HEARTS', 'EIGHT'), PLAYER_IDS[0])
	# 	hand.accept_card(Card('HEARTS', 'SEVEN'), PLAYER_IDS[1])
	# 	hand.accept_card(Card('HEARTS', 'ACE'), PLAYER_IDS[2])
	# 	hand.accept_card(Card('HEARTS', 'QUEEN'), PLAYER_IDS[3])
	# 	hand.accept_card(Card('DIAMONDS', 'QUEEN'), PLAYER_IDS[2])
