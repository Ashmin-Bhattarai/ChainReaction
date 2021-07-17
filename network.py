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

    def initial_data(self):
        try:

            print("Fetching initial data...")
            return pickle.loads(self.client.recv(8192))
        except socket.error as e:
            print (e)
            


    def send(self,data):
        try:            
            self.client.sendall(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
