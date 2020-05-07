'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

import json
import random
import string
import threading

class Room(threading.Thread):
	def __init__(self, owner):
		super(self.__class__, self).__init__()
		self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
		self.owner = owner
		self.players = []
		self.addPlayer(owner)

	def addPlayer(self, player):
		self.players.append(player)
		player.currentRoom = self
		self.sendToRoom("Player|"+json.dumps(player.clientValue()));

	def sendToRoom(self, msg):
		for player in self.players:
			player.sendMsg(msg)

	def playersJson(self):
		players = []
		for player in self.players:
			players.append(player.clientValue())
		return players
	