import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 25565
        # self.port = 5555

    def connect(self):
        try:
            self.addr = (self.server, self.port)
            self.client.connect(self.addr)
        except ConnectionRefusedError:
            print("Server is OFFLINE !!!")

    def send(self, data):
        try:
            self.client.sendall(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    # def initail_connnect(self):
    #     try:

    #         return pickle.loads(self.client.recv(2048))
    #     except socket.error as e:
    #         print(e)
