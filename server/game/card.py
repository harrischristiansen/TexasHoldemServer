'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''
from enum import Enum

class CardClass(Enum):
	HEART = 1
	DIAMOND = 2
	SPADE = 3
	CLUB = 4

class CardValue(Enum):
	ACE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13

class Card(object):
	def __init__(self, cardClass, cardValue):
		self.cardClass = cardClass
		self.cardValue = cardValue

	def clientValue(self):
		return "[%d,%d]" % (self.cardValue.value, self.cardClass.value)

	def __repr__(self):
		return "%s of %s" % (self.cardValue.name, self.cardClass.name)