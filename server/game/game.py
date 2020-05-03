'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

import threading

class HoldemGame(threading.Thread):
	def __init__(self, players):
		super(self.__class__, self).__init__()
		self.players = players

	