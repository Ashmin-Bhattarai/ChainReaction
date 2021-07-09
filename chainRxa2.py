from main_screen import *
import tkinter as tk
from grid import *
from player import *
from network import *
player = 1

size = 10

colors = ["#000000", "red", "#7CFC00", "#0000ff", "#ff00ff"]
cord_list = []
n=Network()

player_number = int(mainScreen()) + 1
player,cell,players=n.connect()
print(player.id)
print(player.color)
print(len(cell))
print(players)


root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()

cells = Grid(size, c, players, 2,cell)

c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)

root.mainloop()
