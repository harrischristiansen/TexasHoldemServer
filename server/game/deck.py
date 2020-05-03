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

if __name__ == '__main__':
	print("Hello World")