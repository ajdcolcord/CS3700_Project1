#!/usr/bin/python

import sys
import socket

port = str(sys.argv[1])
sflag = str(sys.argv[2])
hostname = str(sys.argv[3])
neuid = str(sys.argv[4])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

ipaddr = socket.gethostbyname(hostname)

def get_message():
    mess = sock.recv(1024)
    parse_message(mess)
    
def parse_message(message):
    message_arr = str(message).split()
    if message_arr[0] == 'STATUS':
        problem = message_arr[1] #CHANGE THIS
        print result
        result = ""
        send_message(result)
    elif message_arr[0] == 'BYE':
        print message_arr[1] + '\n'
        sock.close()
    else:
        print "NO MESSAGE"

def send_message(message):
    sock.send(message + '\n');

print ipaddr

try:
    sock.connect((ipaddr, int(port)))
except:
    alert("FAILED TO CONNECT")

#send hello
try:
    send_message('HELLO' + neuid)
except:
    "Failed to send HELLO"
#get initial message
message = True

while message:
    print message
    message = sock.recv(1024)
    if message:
        print message
        parse_message(message)

sock.close()
