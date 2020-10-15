import socket

port_list = [80, 22, 443, 21]

port_scan_dict = {}


def scanned_port():
	for i in port_list:
		sock = socket.socket()
		print(f'Scanning port {i}')
		host = socket.gethostname()
		scan = sock.connect_ex((host, i))
		if scan == 0:
			port_scan_dict[f'Port {i}'] = 'open'
		else:
			port_scan_dict[f'Port {i}'] = 'closed'
		sock.close()
	return port_scan_dict

def main():
	print(scanned_port())

if __name__ == '__main__':
	main() 
