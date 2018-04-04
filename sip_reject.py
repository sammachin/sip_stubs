import sys
from twisted.internet import reactor
from twisted.protocols import sip
from twisted.internet.protocol import ServerFactory


class SipProxy(sip.Proxy):
	def __init__(self):
		sip.Proxy.__init__(self, host=listenip, port=5065)
	def handle_request(self, message, addr):
		print message.toString()
		if message.method == 'ACK':
			return
		response = self.responseFromRequest(486, message)
		response.creationFinished()
		self.deliverResponse(response)
		print response.toString()


listenip = "192.168.1.2"
reactor.listenUDP(5065, SipProxy(), listenip)
reactor.run()