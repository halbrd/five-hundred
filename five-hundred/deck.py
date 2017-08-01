from card import CardRank, CardSuit, Card

class Deck:
	def __init__(self):
		self.cards = []
		self.new_deck()

	def new_deck(self):
		self.cards = []

		# Generate full deck
		for rank in CardRank.ranks:
			for suit in [suit for suit in CardSuit.suits if suit != 'JOKER']:
				self.cards.append(Card(rank, suit))

		# Add Joker
		self.cards.append(Card('JOKER', None))

		# Remove unused cards
		self.cards = filter(lamba card: not card.rank in { 'TWO', 'THREE' } and not (card.rank == "FOUR" and card.suit in { 'CLUBS', 'SPADES' }), self.cards)

	def shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		index = random.randint(0, len(self.cards) - 1)
		card = self.cards[index]
		del self.cards[index]
		return card
