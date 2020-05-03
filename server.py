'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

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
			self.sendMessage(msg, False)

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
				self.currentGame = int(data.split()[1])
				sendmsg(self.currentGame)
			except:
				None


	def onClose(self, wasClean, code, reason):
		return None

#################### Main ####################
if __name__ == "__main__":
	########## Start Web Sockets ##########
	if DEBUG_ENABLED:
		log.startLogging(sys.stdout)
	factory = WebSocketServerFactory(u"ws://127.0.0.1:"+str(PORT_GAME_SERVER))
	factory.protocol = GameClient
	# factory.setProtocolOptions(maxConnections=2)
	reactor.listenTCP(PORT_GAME_SERVER, factory)
	reactor.run()
	## End WS ##