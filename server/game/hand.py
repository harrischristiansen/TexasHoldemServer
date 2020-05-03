'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''
from .card import *

class Hand(object):
	def __init__(self):
		self.cards = []

	def addCard(self, card):
		self.cards.append(card)

	def isManyOfKind(self, amount):
		cardValues = [c.cardValue for c in self.cards]
		pairCard = None
		for cardValue in cardValues:
			if cardValues.count(cardValue) >= amount:
				pairCard = cardValue
		return pairCard

	def isPair(self):
		return self.isManyOfKind(2)

	def isThreeOfKind(self):
		return self.isManyOfKind(3)

	def isFourOfKind(self):
		return self.isManyOfKind(4)

	def isFlush(self):
		cardClasses = [c.cardClass for c in self.cards]
		for cardClass in cardClasses:
			if cardClasses.count(cardClass) >= 5:
				return True
		return False

	def isStright(self):
		cardValues = [c.cardValue for c in self.cards]
		for cardValue in cardValues:
			if cardsValues.count(cardValue-1) >= 1:
				if cardsValues.count(cardValue-2) >= 1:
					if cardsValues.count(cardValue-3) >= 1:
						if cardsValues.count(cardValue-4) >= 1:
							return cardValue
		return None