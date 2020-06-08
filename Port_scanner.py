import socket
from threading import Thread 
import time

port_scan_dict = {}

def port_80(thread_id):
	sock = socket.socket()
	print('Scanning port 80')
	host = socket.gethostname()
	scan = sock.connect_ex((host, 80))
	if scan == 0:
		port_scan_dict['Port 80'] = 'open'
	else:
		port_scan_dict['Port 80'] = 'closed'
	sock.close()
def port_22(thread_id):
	sock = socket.socket()
	print('Scanning port 22')
	host = socket.gethostname()
	scan = sock.connect_ex((host, 22))
	if scan == 0:
		port_scan_dict['Port 22'] = 'open'
	else:
		port_scan_dict['Port 22'] = 'closed'
	sock.close()
def port_443(thread_id):
	sock = socket.socket()
	print('Scanning port 443')
	host = socket.gethostname()
	scan = sock.connect_ex((host, 443))
	if scan == 0:
		port_scan_dict['Port 443'] = 'open'
	else:
		port_scan_dict['Port 443'] = 'closed'
	sock.close()
def port_21(thread_id):
	sock = socket.socket()
	print('Scanning port 21')
	host = socket.gethostname()
	scan = sock.connect_ex((host, 21))
	if scan == 0:
		port_scan_dict['Port 21'] = 'open'
	else:
		port_scan_dict['Port 21'] = 'closed'
	sock.close()


def main():


	for i in range(1):


		thread_80 = Thread(target=port_80, args=(i,))

		thread_80.start()

		time.sleep(2)

		thread_22 = Thread(target=port_22, args=(i,))

		thread_22.start()

		time.sleep(2)

		thread_443 = Thread(target=port_443, args=(i,))

		thread_443.start()

		time.sleep(2)

		thread_21 = Thread(target=port_21, args=(i,))

		thread_21.start()

		time.sleep(2)

	print(port_scan_dict)







if __name__ == '__main__':

	main() 
