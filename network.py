import socket
import pickle
from tkinter.constants import FIRST
from grid import *

class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        hostname=socket.gethostname()
        ipaddress=socket.gethostbyname(hostname)
        print(ipaddress)
        self.server=ipaddress
        self.port=5555
        self.addr=(self.server,self.port)
        self.first=True
        
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
            self.client.connect(self.addr)
            print("Fetching initial data...")
            return pickle.loads(self.client.recv(2048))
        except:
            pass


    def send(self,data):
        try:         
            self.client.send(pickle.dumps(data))
            print("Client receiving data...")
            return pickle.loads(self.client.recv(2048*10))
        except socket.error as e:
            print(e)

    # def receive(self):
    #     try:
    #         print("Clinet receiving data...")
    #         # self.client.connect(self.addr)
    #         return pickle.loads(self.client.recv(8192))
    #     except socket.error as e:
    #         print(e)

