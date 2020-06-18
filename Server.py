import time
from Ports import *
from threading import Thread

#Calling the classes defined in the Ports.py file

p80 = Port80(80)
p22 = Port22(22)
p443 = Port443(443)
p21 = Port21(21)

#Defining the threads

def pto80(thread_1):
	p80.openport()
def pto22(thread_2):
	p22.openport()
def pto443(thread_3):
	p443.openport()
def pto21(thread_4):
	p21.openport()

#Defining main: print a sentence which states the open ports, then create a loop to launch the threads

def main():
	print('Ports {0}, {1}, {2}, {3} are open, awaiting connections...'.format(p80.port80, p22.port22, p443.port443, p21.port21))


	for i in range(1):


		t80 = Thread(target=pto80, args=(i,))

		t80.start()


		t22 = Thread(target=pto22, args=(i,))

		t22.start()


		t443 = Thread(target=pto443, args=(i,))

		t443.start()


		t21 = Thread(target=pto21, args=(i,))

		t21.start()




	
	
	



if __name__ == '__main__':
	main() 

	


