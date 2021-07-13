import socket
from _thread import *
from tkinter.constants import CHECKBUTTON
from player import *
import pickle
from grid import *
import sys
import pygame
import time

hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
print(ipaddress)
server=ipaddress
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((server,port))
maxplayer=3
s.listen(maxplayer)

current_player=-1
cells = [[[0 for cell in range(2)] for col in range(8)] for row in range(8)]
# players=[Grid(1,"red",cells,2),Grid(2,"blue",cells,2)]
players=[Grid(1,"red",cells,2),Grid(2,"blue",cells,2),Grid(3,"green",cells,2),Grid(4,"yellow",cells,2)]
print("server is online. Ready to connect...")
clock=pygame.time.Clock()
def threaded_client(conn):
    global players,current_player
    run=True
    conn.sendall(pickle.dumps(players[current_player]))
    # conn.send(pickle.dumps(cells))
    # conn.send(pickle.dumps(players))    
    while run:     
        clock.tick(60) 
        try: 
            cell,playerid,played=pickle.loads(conn.recv(2048))
            color=players[current_player].color
            print("SERVER:playerid=",current_player+1,"played=",played,"color=",color)
            if played==True:
                current_player+=1
                if current_player>maxplayer-1:
                    current_player=0
                played= False  
                color=players[current_player].color
                  
            else:
                cell=0  
                 
            conn.sendall(pickle.dumps([cell,current_player+1,played,color]))

        except socket.error as e:
            print("Disconnected")
            print("server error: ",e)
            current_player-=1
            break

    run=False
    conn.close()
    sys.exit()

while True:
    conn,addr=s.accept()  #if connection is done, it return a object and it's ip address
    print("Connected to:",addr)        
    start_new_thread(threaded_client,(conn,))
    current_player+=1
