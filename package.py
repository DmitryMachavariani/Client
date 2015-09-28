import socket
import pickle
import threading


def parse(package):
    # result = []
    # if(package[0] == "login"):
    #     if(package[1] == "success"):
    #         result.append("succerr")
    #     else:
    #         result.append("Возможно, вы указали не верные данные")

    return package

def buildpackage(type, data):
    content = [i for i in data]
    presend = [type, content]

    presend = pickle.dumps(presend)

    try:
        sock.send(presend)

        data = sock.recv(1024)

        while 1:
            if not data:
                break
            else:
                result = parse(pickle.loads(data))
                if len(result) > 0:
                    return result
                break
    except ConnectionError as e:
        print(e)


try:
    sock = socket.socket()
    sock.connect(("", 9001))
except:
    print("Не могу подключиться")
    quit()
