import socket
import threading
import pyaudio
# import time

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

HOST = input("Enter host ip: ")
PORT = 4205

clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clnt.connect((HOST, PORT))


def receive():
    # time.sleep(.5)
    while True:
        try:
            data = clnt.recv(1024)
            stream2.write(data)
        except:
            pass


def send():
    # time.sleep(.5)
    while True:
        try:
            data = stream.read(CHUNK)
            clnt.send(data)
        except:
            pass


def main():
    recv_thread = threading.Thread(target=receive)
    recv_thread.start()

    write_thread = threading.Thread(target=send)
    write_thread.start()


audio = pyaudio.PyAudio()
# input stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# output stream
stream2 = audio.open(format=FORMAT, channels=CHANNELS,
                     rate=RATE, output=True, frames_per_buffer=CHUNK
                     )

main()
