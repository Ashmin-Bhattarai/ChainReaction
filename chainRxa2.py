from main_screen import *
import tkinter as tk
from grid import *
from player import *
from network import *
from _thread import *
import pygame

player = 1

size = 8

colors = ["#000000", "red", "#7CFC00", "#0000ff", "#ff00ff"]
cord_list = []
n=Network()
player,cell,players=n.initial_data()

player_number = int(mainScreen()) + 1
# players=[Player(1,"red"),Player(2,"green"),Player(1,"yellow"),Player(1,"blue")]
# cell = [[[0 for cell in range(2)] for col in range(8)] for row in range(8)]


root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()

cells = Grid(size, c, players, 2,cell,n)

c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)

# def mainloop():

def get_cells():
    clock = pygame.time.Clock()
    while True:
        #
        # clock.tick(60)
        try:
            cell,curr_player=n.receive()
        except:
            pass
        if len(cell) != 0:
            print("client:Data received")
        cells.set_cells(cell)
        cells.set_curr_player(curr_player)
        print("Current player:",curr_player)
        root.after(100, get_cells)


start_new_thread(get_cells,())
root.mainloop()

