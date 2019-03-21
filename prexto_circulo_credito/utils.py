import os
import socket

def shell_exec(cmd):
    return os.popen(cmd).read()

def guzzle(host, port, data, callback=None):
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((host, port))
        clientsocket.send(data.encode())
        response = b''

        while True:
            chunk = clientsocket.recv(1024)
            if not chunk:
                break
            response += chunk

        if callable(callback):
            callback(response)
    except Exception as e:
        raise e
