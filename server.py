'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

from server.game import deck

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

games = []

class GameClient(WebSocketServerProtocol):

	def onConnect(self, request):
		self.currentGame = -1
		self.lock = threading.Lock()

	def onOpen(self):
		self.currentGame = -1

	def sendMsg(self, msg):
		with self.lock:
			self.sendMessage(msg.encode('utf-8'), False)

	def onMessage(self, payload, isBinary):
		global games

		data = format(payload.decode('utf8'))

		if "games" in data:
			gameIDs = []
			for game in games:
				gameIDs.append(game)

			self.sendMsg("G|"+json.dumps(gameIDs));

		elif "join" in data:
			try: # Set Current Game
				myDeck = deck.Deck()
				myDeck.shuffle()
				cards = [myDeck[0], myDeck[1]]
				cards = [myDeck[0].clientValue(), myDeck[1].clientValue()]
				self.sendMsg(str(cards))
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