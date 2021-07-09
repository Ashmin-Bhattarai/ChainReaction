import socket
from _thread import *
from player import *
import pickle

hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
print(ipaddress)
server=ipaddress
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((server,port))

s.listen(2)

current_player=0
players=[Player(1,"red"),Player(2,"green")]


cells = [[[0 for cell in range(2)] for col in range(8)] for row in range(8)]

def threaded_client(conn,player):
    conn.sendall(pickle.dumps(players[player]))
    conn.sendall(pickle.dumps(cells))
    conn.sendall(pickle.dumps(players))


while True:
    conn,addr=s.accept()  #if connection is done, it return a object and it's ip address
    print("Connected to:",addr)        
    start_new_thread(threaded_client,(conn,current_player))
    current_player+=1
