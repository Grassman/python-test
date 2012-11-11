#! /usr/bin/env python
import socket
import sys
import unittest

class TestBoa(unittest.TestCase):
	def make_request(self, port): 
		HOST = 'localhost'
		GET = 'faulty'
        	try:
  			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error, msg:
	  		sys.stderr.write("[ERROR] %s\n" % msg[1])
  			sys.exit(1)
		try:
  			sock.connect((HOST, port))
		except socket.error, msg:
  			sys.stderr.write("[ERROR] %s\n" % msg[1])
  			sys.exit(2)
 
		sock.send("GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (GET, HOST))
 
		data = sock.recv(1024)
		string = ""
		while len(data):
  			string = string + data
  			data = sock.recv(1024)
		sock.close()
		return string
 
	#Check that the BAD REQUEST is part of the response.
	def test_that_9411_returns_bad_request(self):
        	response = self.make_request(9411)
		assert response.find('400 Bad Request') > 0

	def test_that_9412_returns_bad_request(self):
        	response = self.make_request(9412)
        	assert response.find('400 Bad Request') > 0

if __name__ == "__main__":
     unittest.main() # run all tests
