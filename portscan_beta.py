''' Simple port scan RedTeam nation '''
# FIXME: there is an error in line process, i couldn't pass args like normal

import socket
from time import sleep, ctime
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
# New
PARSER.add_argument('-p', help='select ports', dest='ports')
PARSER.add_argument('-P', help='select single port', dest='port')
ARGS = PARSER.parse_args()
print(f'Network Scanner started at:{ctime()}')


class NetworkScanner:
    ''' Scanner class '''
    def __init__(self):
        self.CLOSED_PORT = []
        self.OPENED_PORT = []

    def scan_port(self, port_list, verbose):
        ''' do connect scan '''
        try:
            for port in port_list:
                sock = socket.socket(2, 1)
                scan = sock.connect_ex((ARGS.ip_address, port))
                if scan == 0:
                    if verbose:
                        print(f"|____tcp/{port} open")
                    else:
                        pass
                    self.OPENED_PORT.append(port)
                else:
                    self.CLOSED_PORT.append(port)
                sock.close()
                sleep(ARGS.delay)
        except socket.gaierror as error:
            print('ERROR:', error)
        except TypeError:
            sys.exit("Enter an IP or domain")

    def banner_analyzer(self):
        pass


def output(args, ports_range, comment=''):
    print(f'[!] You will scan {ARGS.ip_address}:{ports_range}. {comment}')
    PROC = Process(target=Scanner.scan_port(args, ARGS.verbose))
    PROC.start()
    print('[+] Opened Ports:', *Scanner.OPENED_PORT)
    print('[-] Closed Ports:', len(Scanner.CLOSED_PORT)-1)


if ARGS.verbose:
    print("[!] Verbose mode in ON")

Scanner = NetworkScanner()
if not ARGS.ports and not ARGS.port:
    output(range(ARGS.min_port, (1+ARGS.max_port)), ports_range=f'{ARGS.min_port}-{ARGS.max_port}')

if ARGS.port:
    output([int(ARGS.port)], ports_range=ARGS.port)

else:
    # setting up port list
    if ARGS.ports == '-':
        output(range(1,65536), ports_range='1, 65535', comment=' this will take time...')

    if ',' in ARGS.ports:
        ports_list = list(map(lambda x: int(x), ARGS.ports.split(',')))
        output(ports_list, ports_range=ARGS.ports)

    if '-' in ARGS.ports and '':
        ports_list = list(map(lambda x: int(x), ARGS.ports.split('-')))
        if ports_list[0] > ports_list[1]:
            output(range(ports_list[1], (1+ports_list[0])), ports_range=ARGS.ports)
        else:
            output(range(ports_list[0], (1+ports_list[1])), ports_range=ARGS.ports)
