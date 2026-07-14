import socket
import subprocess #The library we added allows us to execute the commands that the client requests from the server.

host = "127.0.0.1"
port = 50001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_TEAM)
server_socket.bind((host,port))
server_socket.listen()  #listen and get message

conn, addr = server_socket.accept()
print("connected from : "+str(addr))

while True:
    data = conn.recv(1024).decode()
    print(data)

    result = subprocess.run(data, stdout=subprocess.PIPE, shell=True)  
    # ! subprocess.run() runs command terminal.
    # stdout=subprocess.PIPE >> Get the output of the command but don't print it.

    # shell=True >>  Run commands through the shell.

    if(result.stdout.decode()!=""):
        response_data = result.stdout #output
    else:
        response_data = ("Komut Calıstırıldı").encode()

    response_data = "Mesaj Alindi"
    conn.send(response_data.encode())
conn.close()
