'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

from server import room
from server.game import game, deck

import json
import sys
import threading
########## Start Web Sockets ##########
from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor
## End WS ##

DEBUG_ENABLED = True
PORT_GAME_SERVER = 23345

############################################ Web Client ############################################

rooms = []

class GameClient(WebSocketServerProtocol):
	global games

	def onConnect(self, request):
		self.currentGame = -1
		self.lock = threading.Lock()

	def onOpen(self):
		self.currentGame = -1

	def sendMsg(self, msg):
		with self.lock:
			self.sendMessage(msg.encode('utf-8'), False)

	def onMessage(self, payload, isBinary):
		global rooms

		data = format(payload.decode('utf8'))

		if "rooms" in data:
			roomIDs = []
			for room in rooms:
				roomIDs.append(room.id)

			self.sendMsg("R|"+json.dumps(roomIDs));

		elif "create" in data:
			newRoom = room.Room(1)
			rooms.append(newRoom)

		elif "join" in data:
			try: # Set Current Game
				myDeck = deck.Deck()
				myDeck.shuffle()
				cards = [myDeck[0].clientValue(), myDeck[1].clientValue()]
				self.sendMsg(json.dumps(cards))
			except:
				None


	def onClose(self, wasClean, code, reason):
		return None

#################### Main ####################
if __name__ == "__main__":
	########## Start Web Sockets ##########
	if DEBUG_ENABLED:
		log.startLogging(sys.stdout)
	factory = WebSocketServerFactory()
	factory.protocol = GameClient
	#factory.setProtocolOptions(failByDrop=False, openHandshakeTimeout=90, closeHandshakeTimeout=5)
	# factory.setProtocolOptions(maxConnections=2)
	reactor.listenTCP(PORT_GAME_SERVER, factory)
	reactor.run()
	## End WS ##