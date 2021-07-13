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
cells.set_c(c)
print(cells.gridcolor)
c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)
player=cells.playerid
clock=pygame.time.Clock()
def get_cells():
    
    global cells,c
    foo=True
    tempcolor=cells.gridcolor
    while True:
        clock.tick(60)
        
        Tcells,Tplayerid,Tplayed,Tcolor=n.send([cells.get_cells(),cells.playerid,cells.played])
        
        if Tcells !=0:
            cells.cells=Tcells
        cells.gridcolor=Tcolor
        # cells.grid()
        if Tcolor != tempcolor:
            cells.grid()
            tempcolor=Tcolor
        
        print("Tcolor=",Tcolor,"tempcolor",tempcolor)
        cells.played=Tplayed
        cells.playerid=Tplayerid
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

