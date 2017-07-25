from enum import Enum
import random

Suits = Enum('Suit', 'CLUBS DIAMONDS HEARTS SPADES JOKER')
Ranks = Enum('Rank', 'ACE 2 3 4 5 6 7 8 9 10 JACK QUEEN KING')

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "JOKER" if self.suit == Suit.JOKER else self.rank.value + " of " + self.suit.value

class Deck:
    def __init__(self):
        self.cards = []
        self.new_deck()

    def new_deck(self):
        self.cards = []

        # Generate full deck
        for suit in list(Suits).remove(Suit.JOKER):
            for rank in Ranks:
                self.cards.append(Card(suit, rank))

        # Add Joker
        self.cards.append(Card(Suit.JOKER, None))

        # Remove unused cards
        def is_unused(card):
            return card.rank in { Rank.2, Rank.3 } or card.rank == Rank.4 and card.suit in { Suit.CLUBS, Suit.SPADES }
        self.cards = [ card for card in self.cards if not is_unused(card) ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        index = random.randint(0, len(self.cards) - 1)
        card = self.cards[index]
        del self.cards[index]
        return card

class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players
        self.score = 0

class Bid:
    def __init__(self, player, value, suit):
        self.player = player
        self.value = value
        self.suit = suit

class Kitty:
    def __init__(self, cards):
        self.cards = cards

class Trick:
    def __init__(self, leader, cards):
        self.leader = leader
        self.cards = []

class Hand:
    def __init__(self, dealer, hands, kitty):
        self.dealer = dealer
        self.hands = hands
        self.kitty = kitty
        self.bids = []
        self.tricks = []

class Game:
    def __init__(self, teams):
        self.teams = teams
        self.hands = []
