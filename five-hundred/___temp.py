from hand import Hand
from bid import Bid
from card import Card
from kitty import Kitty

PLAYER_IDS = [ 123, '456', 'abc', '01234567-8901-2345-6789-012345678901' ]

hand = Hand(PLAYER_IDS)

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
hand.accept_bid(Bid('PASS', player_id=PLAYER_IDS[0]))

hand.accept_card(Card('CLUBS', 'ACE'), PLAYER_IDS[3])
hand.accept_card(Card('CLUBS', 'SIX'), PLAYER_IDS[0])
hand.accept_card(Card('CLUBS', 'FIVE'), PLAYER_IDS[1])
hand.accept_card(Card('CLUBS', 'SEVEN'), PLAYER_IDS[2])
hand.accept_card(Card('CLUBS', 'KING'), PLAYER_IDS[3])
hand.accept_card(Card('CLUBS', 'TEN'), PLAYER_IDS[0])
hand.accept_card(Card('SPADES', 'SIX'), PLAYER_IDS[1])
hand.accept_card(Card('CLUBS', 'JACK'), PLAYER_IDS[2])
hand.accept_card(Card('DIAMONDS', 'SEVEN'), PLAYER_IDS[3])
hand.accept_card(Card('DIAMONDS', 'NINE'), PLAYER_IDS[0])
hand.accept_card(Card('DIAMONDS', 'FOUR'), PLAYER_IDS[1])
hand.accept_card(Card('DIAMONDS', 'FIVE'), PLAYER_IDS[2])
hand.accept_card(Card('HEARTS', 'EIGHT'), PLAYER_IDS[0])
hand.accept_card(Card('HEARTS', 'SEVEN'), PLAYER_IDS[1])
hand.accept_card(Card('HEARTS', 'ACE'), PLAYER_IDS[2])
hand.accept_card(Card('HEARTS', 'QUEEN'), PLAYER_IDS[3])
hand.accept_card(Card('DIAMONDS', 'QUEEN'), PLAYER_IDS[2])

print(hand.tricks)