'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

import random
import string
import threading

class HoldemGame(threading.Thread):
	def __init__(self, players):
		super(self.__class__, self).__init__()
		self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
		self.players = players