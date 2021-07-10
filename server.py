import socket
from _thread import *
from tkinter.constants import CHECKBUTTON
from player import *
import pickle
from grid import *

hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
print(ipaddress)
server=ipaddress
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((server,port))

s.listen(2)

current_player=1
players=[Player(1,"red"),Player(2,"green"),Player(1,"yellow"),Player(1,"blue")]


cells = [[[0 for cell in range(2)] for col in range(8)] for row in range(8)]

def threaded_client(conn,player):
    run=True
    conn.send(pickle.dumps([players[player],cells,players]))
    # conn.send(pickle.dumps(cells))
    # conn.send(pickle.dumps(players))    

    while run:       
        global current_player
        data=pickle.loads(conn.recv(8192))
        # if data:
        #     conn.send(pickle.dumps(data))
        if data:
            print("server:Data received")
            current_player+=1
            if (current_player > 2) :
                current_player=1
            conn.send(pickle.dumps([data,current_player]))
            print("server:Data sent")



while True:
    conn,addr=s.accept()  #if connection is done, it return a object and it's ip address
    print("Connected to:",addr)        
    start_new_thread(threaded_client,(conn,current_player))
    current_player+=1
