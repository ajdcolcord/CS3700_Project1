# Austin Colcord and Nick Scheuring
import socket
import sys

# set global flag to indicate if the socket is closed or not
closed_flag = False


# this function calculates the result based on the
# two number inputs first and second, and the operator
def calculate(first, second, operator):
    result = ""
    if operator == "+":
            result = int(first) + int(second)
    elif operator == "-":
        result = int(first) - int(second)
    elif operator == "/":
        result = int(first) / int(second)
    elif operator == "*":
        result = int(first) * int(second)
    else:
        print "Did not recognize: " + operator

    print "Result = " + str(result)
    return result


# this function parses the message based on the message type
def parse_message(message, sock):
    message_arr = str(message).split()
    if message_arr[1] == 'STATUS':
        first = message_arr[2]
        operator = message_arr[3]
        second = message_arr[4]

        result = calculate(first, second, operator)

        sock.send("cs3700spring2016 " + str(result) + '\n')
    if message_arr[1] == 'BYE':
        sock.close()
        global closed_flag
        closed_flag = True


# this is the main functions, running all necessary steps
# to open the socket and send and receive messages
def main():

    # get arguments from console
    port = int(sys.argv[1])
    sflag = str(sys.argv[2])
    hostname = str(sys.argv[3])
    neuid = str(sys.argv[4])

    # create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the host
    try:
        s.connect((hostname, port))
    except socket.error:
        print "Failed To Connect Socket to Host"
        sys.exit(1)

    # send the hello message
    try:
        s.send("cs3700spring2016 HELLO " + neuid + "\n")
    except socket.error:
        print "Failed To Send Hello Message"

    # continuously receive and send messages
    while 1:
        global closed_flag
        if closed_flag:
            break
        received = s.recv(1024)
        print received
        parse_message(received, s)


main()
