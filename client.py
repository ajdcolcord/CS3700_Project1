#!/usr/bin/python

import sys
import socket

port = str(sys.argv[1])
sflag = str(sys.argv[2])
hostname = str(sys.argv[3])
neuid = str(sys.argv[4])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
host = socket.gethostname()

ipaddr = socket.gethostbyname(hostname)

print ipaddr

sock.connect((ipaddr, int(port)))

send_message('HELLO' + neuid)

message = sock.recv(1024)

def parse_message(message):
	message_arr = str(message).split()
	if message_arr[0] == 'STATUS':
		result = message_arr[1] #CHANGE THIS
		#parse the function for 1, 2, 3 
		send_message(result)
	elif message_arr[0] == 'BYE':
		print message_arr[1] + '\n'
		sock.close()

def send_message(message):
	sock.send(message + '\n');