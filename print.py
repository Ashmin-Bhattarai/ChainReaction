import pickle
from network import *

n = Network()
n.server = "192.168.1.17"
n.connect()
server_get = n.send([False])

cells = server_get[0]
cells.myid = server_get[1]
cells.isOnline = True
# print(cells.myid)
while True:
    x, y, gamestart = n.send([cells.x, cells.y, cells.played])
    print("x=", x, "y=", y)
