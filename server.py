import socket
from _thread import *
import pickle
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


    def threaded_client(conn):
        pass

    while True:
        conn,addr=s.accept()
        print("connected to: ",addr)
        start_new_thread(threaded_client,(conn,))


if __name__=="__main__":
    server_run()