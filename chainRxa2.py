import tkinter as tk
from grid import *
from player import *
from network import *
from _thread import *
import pygame
import sys
import time

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
    foo=True
    while True:
        clock.tick(60)
        cells.set_c(c)
        cells.cells,cells.playerid,cells.played=n.send([cells.get_cells(),cells.playerid,cells.played])
        
        # if foo:
        #print("Before IF:playerid=",cells.playerid,"player=",player,"played=",cells.played)
        foo=False

        if cells.playerid==player:
            cells.mouse=True
        else:
            cells.mouse=False
        

        if cells.clicked==True:
            cells.exec()
            #print("After Clicked: playerid=",cells.playerid,"player=",player,"played=",cells.played)
            foo=True
            cells.mouse=False 
            print("cells.played=",cells.played)

start_new_thread(get_cells,())
root.mainloop()

