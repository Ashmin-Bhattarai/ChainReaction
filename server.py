import socket
from _thread import *
from tkinter.constants import CHECKBUTTON
from player import *
import pickle
from grid import *
import sys
import pygame

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
players=[Grid(1,"red",cells,2),Grid(2,"blue",cells,2)]

print("server is online. Ready to connect...")

def threaded_client(conn):
    global players,current_player
    run=True
    conn.sendall(pickle.dumps(players[current_player]))
    # conn.send(pickle.dumps(cells))
    # conn.send(pickle.dumps(players)) 
    foo=True   
    while run:      
        try:       
            cell,playerid,played=pickle.loads(conn.recv(2048))
            
            print("SERVER:playerid=",playerid,"played=",played)
            foo=False
            if (playerid==1 and played==True):
                foo=True
                playerid=2
                played=False
                print("Player 2's turn:")
                # conn.sendall(pickle.dumps([cell,playerid,played]))
            elif (playerid==2 and played==True):
                foo=True
                playerid=1
                played=False
                print("Player 1's turn:")
                # conn.sendall(pickle.dumps([cell,playerid,played]))
            # print("Size of sent data",sys.getsizeof([cell,playerid]))  
            conn.sendall(pickle.dumps([cell,playerid,played]))
        except socket.error as e:
            print("Disconnected")
            print("server error: ",e)
            current_player-=1
            break

    run=False
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
