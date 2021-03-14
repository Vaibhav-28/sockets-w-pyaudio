import socket
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 4205

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind((HOST, PORT))
srvr.listen()

print(f"Connected to {socket.gethostbyname(socket.gethostname())}")


def broadcast(clnt, data):
    for i in clients:
        if i != clnt:
            i.send(data)


def acceptClients(clnt):
    while True:
        try:
            data = clnt.recv(1024)
            broadcast(clnt, data)
        except:
            print("error")


def receive():
    while True:
        clnt, addr = srvr.accept()
        print(f'client connected to {addr}')
        clients.append(clnt)
        thread = threading.Thread(target=acceptClients, args=(clnt,))
        thread.start()


receive()
