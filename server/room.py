'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

import random
import string
import threading

class Room(threading.Thread):
	def __init__(self, owner):
		super(self.__class__, self).__init__()
		self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
		self.owner = owner
		self.players = [owner]

	def addPlayer(self, player):
		self.players.append(player)

	def playersJson(self):
		players = []
		for player in self.players:
			players.append(player.clientValue())
		return players
	