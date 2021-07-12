import socket
from _thread import *
from tkinter.constants import CHECKBUTTON
from player import *
import pickle
from grid import *
import sys

hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
print(ipaddress)
server=ipaddress
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((server,port))

s.listen(2)

current_player=-1
cells = [[[0 for cell in range(2)] for col in range(8)] for row in range(8)]
players=[Grid(1,"red",cells,2),Grid(1,"blue",cells,2)]
print("server is online. Ready to connect...")
def threaded_client(conn):
    global players,current_player
    run=True
    conn.sendall(pickle.dumps(players[current_player]))
    # conn.send(pickle.dumps(cells))
    # conn.send(pickle.dumps(players))    
    
    while run:       
        try:       
            data=pickle.loads(conn.recv(8192))
            print("1")
            print(data)
            if data:
                print("Data received...")
                if data.playerid==1:
                    data.playerid=2
                    print("Player 2's turn:")
                else:
                    data.playerid=1
                    print("Player 1's turn:")
            conn.sendall(pickle.dumps(data))
        except:
            print("Disconnected")
            current_player-=1
            # run=False
            conn.close()
            sys.exit()

        

        # if data:
        #     conn.send(pickle.dumps(data))
        # if data:
        #     print("server:Data received")
        #     current_player+=1
        #     if (current_player > 2) :
        #         current_player=1
        #     conn.send(pickle.dumps([data,current_player]))
        #     print("server:Data sent")




while True:
    conn,addr=s.accept()  #if connection is done, it return a object and it's ip address
    print("Connected to:",addr)        
    start_new_thread(threaded_client,(conn,))
    current_player+=1
