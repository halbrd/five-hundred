class Deck:
	def __init__(self):
		self.cards = []
		self.new_deck()

	def new_deck(self):
		self.cards = []

		# # Generate full deck
		# for suit in list(Suits).remove(Suit.JOKER):
		# 	for rank in Ranks:
		# 		self.cards.append(Card(suit, rank))
		#
		# # Add Joker
		# self.cards.append(Card(Suit.JOKER, None))
		#
		# # Remove unused cards
		# def is_unused(card):
		# 	return card.rank in { Rank.TWO, Rank.THREE } or card.rank == Rank.FOUR and card.suit in { Suit.CLUBS, Suit.SPADES }
		# self.cards = [ card for card in self.cards if not is_unused(card) ]

	def shuffle(self):
		random.shuffle(self.cards)

	def draw_card(self):
		index = random.randint(0, len(self.cards) - 1)
		card = self.cards[index]
		del self.cards[index]
		return card
