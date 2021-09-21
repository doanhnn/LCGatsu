import socket
import sys

#HOST, PORT = "46.101.23.188", 30858
HOST, PORT = "0.0.0.0", 23333

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket()
sock.connect((HOST, PORT))
print "Connected to server..."

# Receive string "Where is LCGatsu?"
received = str(sock.recv(32))
print("Received: {}".format(received))

# Real = 1 or random numbers, strings, etc...
real = 1

# received = str(sock.recv(1024))
# print("Received: {}".format(received))

while(1):
	# Receive string "Choose a rock:"
	# Maybe get some error when you run this program with local server
	# Try to run several times or receive this string outside while loop
	received = str(sock.recv(1024))
	print("Received : {}".format(received))

	# Send real's value to server
	sock.sendall(bytes(real))
	print "Send     :{}".format(real)

	# Receive results from server
	received = str(sock.recv(1024))
	print("Received :{}".format(received))

	# Manipulate data to get the value of real
	if 'position' in received:
		real = received.split("0x")[1].split("L")[0]
		print("Real     :{}".format(real))
	elif 'god' in received:
		# Got the flag, so exit the loop
		exit(1)