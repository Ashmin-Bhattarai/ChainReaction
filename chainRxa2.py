import tkinter as tk
from grid import *
from player import *
from network import *
from _thread import *
import pygame
import sys

n=Network()
root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()

cells=n.initial_data()

c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)
player=cells.playerid
clock=pygame.time.Clock()
def get_cells():
    
    global cells,c
    while True:
        clock.tick(60)
        cells.cells,cells.playerid,cells.played=n.send([cells.get_cells(),cells.playerid,cells.played])
        cells.set_c(c)
        print("playerid=",cells.playerid,"player=",player,"played=",cells.played)
        if cells.playerid==player:
            cells.mouse=True
        else:
            cells.mouse=False
        # print(cells.mouse)

        if cells.clicked==True and cells.isvalid():
            cells.exec()
            cells.mouse=False 

start_new_thread(get_cells,())
root.mainloop()

