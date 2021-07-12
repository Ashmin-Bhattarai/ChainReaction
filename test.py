from network import *
import tkinter as tk
import time
from _thread import *

n=Network()
root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()
cells=n.initial_data()

cells.set_c(c)
c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)
print(cells.playerid)

def run():
    print("running")
    while True:
        global cells,c    
        cells.cells,cells.playerid=n.send([cells.get_cells(),cells.playerid])
        cells.set_c(c)
        print(cells.playerid)

start_new_thread(run,())
root.mainloop()
