from main_screen import *
from Grid import Grid
import tkinter as tk

player = 1

size = 10

#cells = [[[0 for cell in range(2)] for col in range(size)] for row in range(size)]
colors = ["#000000", "red", "#7CFC00", "#0000ff", "#ff00ff"]
#cord_list = []

class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color






player_number = int(mainScreen()) + 1
players = []
for i in range(0, player_number):
    players.append(Player(i, colors[i]))



root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()

cells = Grid(size, c, players, player_number)



c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)

root.mainloop()
