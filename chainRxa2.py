from Grid import Grid
import tkinter as tk
from tkinter import ttk

player = 1

# cells = [[[0 for cell in range(2)] for col in range(size)] for row in range(size)]
colors = ["#000000", "#12FF00", "#01AF9D", "#FF0D0D",
          "#0DAFE8", "#82BFDC", "#FFEB78", "#33FFDD", "#444545"]


class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color




def call_this(root, mainScreen, home_page, image_frame, player_number, grid_size):
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        pass


    def back_function():
        mainScreen(root, home_page, image_frame)

    button_frame = ttk.Frame(root)
    button_frame.pack()
    newgame_button = ttk.Button(
        button_frame, text='New Game', command=newgame_function)
    back_button = ttk.Button(button_frame, text='Back', command=back_function)
    newgame_button.grid(column=0, row=0, padx=5, sticky=tk.W)
    back_button.grid(column=1, row=0, padx=5, sticky=tk.W)
    # cells = Grid(size, c, players, colors, player_number)

    ttk.Separator(orient='horizontal').pack()

    players = []
    for i in range(0, player_number):
        players.append(Player(i, colors[i]))

    c = tk.Canvas(root, height=root.winfo_height(),
                  width=root.winfo_width(), bg='white')
    c.pack()

    cells = Grid(grid_size, c, players, colors, player_number)
    c.bind('<Configure>', cells.grid)
    c.bind('<Button-1>', cells.numbering)
    root.mainloop()
