import socket
import pickle   # Python pickle module is used for serializing and de-serializing python object structures.
                # The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called pickling


class Network(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.43.227"
        self.port = 5555
        self.addr = (self.server,self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))         #load byte data
        except:
            pass

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))

