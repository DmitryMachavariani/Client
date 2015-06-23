import socket
import pickle

try:
    sock = socket.socket()
    sock.connect(("", 9001))
except:
    print("Не могу подключиться")
    quit()

def buildpackage(type, data):
    content = [i for i in data]
    presend = [type, content]

    presend = pickle.dumps(presend)

    try:
        sock.send(presend)
    except ConnectionError as e:
        print(e)
