import socket
import pickle

class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        hostname=socket.gethostname()
        ipaddress=socket.gethostbyname(hostname)
        print(ipaddress)
        self.server=ipaddress
        self.port=5555
        self.addr=(self.server,self.port)
        self.client.connect(self.addr)
    #     self.connect()
    #     
    # def getP(self):
    #     return self.p

    # def connect(self):
    #     try:
    #         self.client.connect(self.addr)
    #     except:
    #         pass


    def initial_data(self):
        try:
            # self.client.connect(self.addr)
            print("Fetching initial data...")
            return pickle.loads(self.client.recv(8192))
        except:
            pass


    def send(self,data):
        try:            
            print("client sending data...")
            self.client.send(pickle.dumps(data))
            # return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            print("Clinet receiving data...")
            # self.client.connect(self.addr)
            return pickle.loads(self.client.recv(8192))
        except socket.error as e:
            print(e)

