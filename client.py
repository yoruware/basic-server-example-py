import socket

host = "127.0.0.1" 
# 127.0.0.1 is a loopback address reserved for local communication. It means the connection is made with your own computer.
# "There is no place like 127.0.0.1" 

port = 50001
# When using TCP or UDP, you can define your own port number.
# Ports between 0-1023 are known as "well-known ports" (80 = HTTP, 22 = SSH, 443 = HTTPS).
# Ports between 1024-49151 are registered ports and may be reserved for specific applications.
# Higher ports (such as 50000+) are commonly used for custom applications to avoid conflicts.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Creates a socket object.
# AF_INET specifies IPv4 communication.
# SOCK_STREAM specifies TCP protocol usage.

client_socket.connect((host, port))
# Connects the client to the server.
# connect() requires a tuple containing the host and port information.

message = input(">> ")


while message.lower().strip() != "quit":
    if message != "":
        client_socket.send(message.encode())
        # encode() converts the string message into bytes (UTF-8 by default).
        # Sockets communicate using bytes, not regular strings.

        data = client_socket.recv(1024).decode()
        # Receives up to 1024 bytes of data from the server.
        # decode() converts received bytes back into a readable string.

        print("Response from server : " + str(data))
        # Prints the response received from the server.

    message = input(">> ")

client_socket.close()
# Closes the socket connection.
