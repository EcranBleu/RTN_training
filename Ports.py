import socket

class Port80():
	def __init__(self, port80):
		self.port80 = 80

	def openport(self):
		sock = socket.socket()
		host = socket.gethostname()
		port = self.port80
		sock.bind((host, port))
		sock.listen(1)

		#Using 'if' instead of 'while' for a one-off server session. The server program will shut down after only one thread loop.

		if True:
			client, address = sock.accept()
			print('Connection From {0}'.format(address))
			client.close()
			

#Repeated for each port

class Port22():
	def __init__(self, port22):
		self.port22 = 22

	def openport(self):
		sock = socket.socket()
		host = socket.gethostname()
		port = self.port22
		sock.bind((host, port))
		sock.listen(1)
		if True:
			client, address = sock.accept()
			print('Connection From {0}'.format(address))
			client.close()

class Port443():
	def __init__(self, port443):
		self.port443 = 443

	def openport(self):
		sock = socket.socket()
		host = socket.gethostname()
		port = self.port443
		sock.bind((host, port))
		sock.listen(1)
		if True:
			client, address = sock.accept()
			print('Connection From {0}'.format(address))
			client.close()

class Port21():
	def __init__(self, port21):
		self.port21 = 21

	def openport(self):
		sock = socket.socket()
		host = socket.gethostname()
		port = self.port21
		sock.bind((host, port))
		sock.listen(1)
		if True:
			client, address = sock.accept()
			print('Connection From {0}'.format(address))
			client.close()
			