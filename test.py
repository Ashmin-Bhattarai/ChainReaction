from tkinter.constants import NE
from network import *
n=Network()
p=Network()
msg="get cells"
msg="set cells"
data=67
n.send(67)
c=0
for i in range (50000):
    c+=1
print(p.receive())
