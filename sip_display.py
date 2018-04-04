#! /usr/bin/env python

import sys
from twisted.internet import reactor
from twisted.protocols import sip
from twisted.internet.protocol import ServerFactory
from urlparse import urlparse


class SipProxy(sip.Proxy):
	def __init__(self):
		sip.Proxy.__init__(self, host=listenip, port=5060)
	def handle_request(self, message, addr):
		print message.toString()	
		response = self.responseFromRequest(200, message)
		response.creationFinished()
		self.deliverResponse(response)

listenip = "192.168.1.2"
reactor.listenUDP(5060, SipProxy(), listenip)
reactor.run()

