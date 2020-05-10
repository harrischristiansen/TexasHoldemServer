'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

from .room import Room
from .game import game, deck

import json
import threading

from autobahn.twisted.websocket import WebSocketServerProtocol

rooms = {}

class PlayerClient(WebSocketServerProtocol):
	def __repr__(self):
		return "%s" % (self.request.peer)

	def clientValue(self):
		return [self.currentSeat(), str(self), self.balance]

	def currentSeat(self):
		if self.currentRoom == -1:
			return -1
		return self.currentRoom.players.index(self)

	def onConnect(self, request):
		self.request = request
		self.currentRoom = -1
		self.balance = 0.0
		self.lock = threading.Lock()

	def onOpen(self):
		self.currentRoom = -1

	def sendMsg(self, msg):
		with self.lock:
			self.sendMessage(msg.encode('utf-8'), False)

	def onMessage(self, payload, isBinary):
		global rooms

		data = format(payload.decode('utf8'))
		command = data.split(' ')

		if "rooms" in data:
			if self.currentRoom != -1:
				return self.sendMsg("R|"+json.dumps([self.currentRoom.id]));
			self.sendMsg("R|"+json.dumps(list(rooms.keys())));

		elif "create" in data:
			if self.currentRoom != -1:
				return self.sendMsg("Error|Already In Room");
			newRoom = Room(self)
			rooms[newRoom.id] = newRoom
			self.sendMsg(json.dumps(newRoom.id));

		elif "join" in data:
			if self.currentRoom != -1:
				return self.sendMsg("Error|Already In Room");
			roomID = command[1] if len(command) > 1 else "null"
			if roomID not in rooms.keys():
				return self.sendMsg("Error|Room Not Found");
			self.currentRoom = rooms[roomID]
			self.currentRoom.addPlayer(self)
			self.sendMsg("Players|"+json.dumps(self.currentRoom.playersJson()))

		elif "buyin" in data:
			if len(command) > 1:
				try:
					amount = float(command[1])
					self.balance += amount
					self.currentRoom.sendToRoom("Player|"+json.dumps(self.clientValue()));
				except:
					None

		elif "cards" in data:
			myDeck = deck.Deck()
			myDeck.shuffle()
			cards = [myDeck[0].clientValue(), myDeck[1].clientValue()]
			self.sendMsg(json.dumps(cards))


	def onClose(self, wasClean, code, reason):
		return None