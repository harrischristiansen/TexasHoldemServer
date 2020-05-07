'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

import sys
from server.player import PlayerClient
########## Start Web Sockets ##########
from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor
## End WS ##

DEBUG_ENABLED = True
PORT_GAME_SERVER = 23345

#################### Main ####################
if __name__ == "__main__":
	########## Start Web Sockets ##########
	if DEBUG_ENABLED:
		log.startLogging(sys.stdout)
	factory = WebSocketServerFactory()
	factory.protocol = PlayerClient
	#factory.setProtocolOptions(failByDrop=False, openHandshakeTimeout=90, closeHandshakeTimeout=5)
	# factory.setProtocolOptions(maxConnections=2)
	reactor.listenTCP(PORT_GAME_SERVER, factory)
	reactor.run()
	## End WS ##