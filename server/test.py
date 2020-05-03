from game import deck, hand

if __name__ == '__main__':
	deck = deck.Deck()
	hand = hand.Hand()
	hand.addCard(deck[0])
	hand.addCard(deck[1])
	print(hand.isPair())
	hand.addCard(deck[1])
	print(hand.isPair())