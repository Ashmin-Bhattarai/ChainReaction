import tkinter as tk
from grid import *
from player import *
from network import *
from _thread import *
import pygame

n=Network()
root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()

cells=n.initial_data()
cells.set_n(n)
c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)
cells.set_c(c)

def get_cells():
    print("Entering get_cells")
    global cells,n,root
    clock = pygame.time.Clock()
    player=cells.playerid
    while True:
        print("playerid=",cells.playerid,"player=",player)
        if cells.playerid==player:
            cells.mouse=True
        else:
            cells.mouse=False

        if cells.clicked==True and cells.isvalid:
            n.send(cells)
            cells.exec()
        cells=n.receive()
        


start_new_thread(get_cells,())
root.mainloop()

