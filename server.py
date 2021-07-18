import socket
from _thread import *
import pickle
import pygame
import sys
def server_run():
    hostname=socket.gethostname()
    ipaddress=socket.gethostbyname(hostname)
    server=ipaddress
    port=5555

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.bind((server,port))
    except socket.error as e:
        print (e)

    s.listen(2)

    global playerindex,x,y,played,playerChange
    playerindex=x=y=-1
    played=False
    playerChange=False
    clock=pygame.time.Clock()
    def threaded_client(conn):
        global playerindex,x,y,played,playerChange
        run=True
        while run:
            # clock.tick(60)
            try:
                Tx,Ty,Tplayed=pickle.loads(conn.recv(2048))
                # print(playerindex,x,y,played)
                # playerChange=False
                if Tplayed==True:
                    x=Tx
                    y=Ty
                conn.sendall(pickle.dumps([x,y]))
            except socket.error as e:
                print("disconnected")
                run=False
        playerindex=x=y=-1
        played=False
        playerChange=False
        conn.close()
        sys.exit() 

    while True:
        conn,addr=s.accept()
        print("connected to: ",addr)
        start_new_thread(threaded_client,(conn,))


if __name__=="__main__":
    server_run()