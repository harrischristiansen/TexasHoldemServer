'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''
from .card import *

class Deck(object):
	def __init__(self):
		self.deck = []
		for cClass in CardClass:
			for cValue in CardValue:
				self.deck.append(Card(cClass, cValue))

	def __getitem__(self, index):
		return self.deck[index]

	def __setitem__(self, index, value):
		self.deck[index] = value