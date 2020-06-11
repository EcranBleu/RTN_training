''' Simple port scan RedTeam nation '''

import socket
from time import sleep
from multiprocessing import Process
import argparse
import sys


# setting up argparse
PARSER = argparse.ArgumentParser()
PARSER.add_argument('-host', help='host ip/domain', dest='ip_address', required=True)
PARSER.add_argument('--min-port', help='minimum port range', type=int, default=1, dest='min_port')
PARSER.add_argument('--max-port', help='maximum port range', type=int, default=1024, dest='max_port')
PARSER.add_argument('--delay', help='time(per seconds) between every connection', type=int, default=0, dest='delay')
PARSER.add_argument('-v', help="verbose mode", default=False, dest='verbose', action='store_true')
ARGS = PARSER.parse_args()

CLOSED_PORT = []
OPENED_PORT = []

def scan_port(port_list, verbose):
    ''' do connect scan '''
    try:
        for port in port_list:
            sock = socket.socket(2, 1)
            scan = sock.connect_ex((ARGS.ip_address, port))
            if scan == 0 and verbose:
                print(f"|    tcp/{port} open")
                OPENED_PORT.append(port)
            if scan == 0 and verbose == False:
                OPENED_PORT.append(port)
            else:
                CLOSED_PORT.append(port)
            sock.close()
            sleep(ARGS.delay)
    except socket.gaierror as error:
        print('ERROR:', error)
    except TypeError:
        sys.exit("Enter an IP or domain")
if ARGS.verbose:
    print("[!] Verbose mode in ON")
PROC = Process(target=scan_port(range(ARGS.min_port, ARGS.max_port), ARGS.verbose))
PROC.start()
print(f'You will scan {ARGS.ip_address}:{ARGS.min_port}-{ARGS.max_port}')
print("Open Ports:", *OPENED_PORT)
for num in OPENED_PORT:
    CLOSED_PORT.remove(num)
print("Closed Ports:", len(CLOSED_PORT))
