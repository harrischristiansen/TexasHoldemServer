'''
	@ Harris Christiansen (Harris@HarrisChristiansen.com)
	2020-05-03
	Poker - Texas Holdem
'''

class Player(object):
	def __init__(self, connection):
		super(self.__class__, self).__init__()
		self.connection = connection
	