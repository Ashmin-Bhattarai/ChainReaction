import pygame
from grid import Grid
import tkinter as tk
from tkinter import ttk
from network import *
from _thread import *
from server import *
player = 1

# cells = [[[0 for cell in range(2)] for col in range(size)] for row in range(size)]
colors = ["#000000", "#12FF00", "#01AF9D", "#FF0D0D",
          "#0DAFE8", "#82BFDC", "#FFEB78", "#33FFDD", "#444545"]


class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.name=id


def call_this(root, mainScreen, widget_destroy, home_page, image_frame, player_number, grid_size, button_style):
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        widget_destroy(root)
        call_this(root, mainScreen, widget_destroy, home_page, image_frame,
                  player_number - 1, grid_size, button_style)

    def back_function():
        mainScreen(root, home_page, image_frame, button_style)

    button_frame = ttk.Frame(root)
    button_frame.pack(fill='both')
    # button_frame.columnconfigure(0, weight=40)
    newgame_button = ttk.Button(
        button_frame, text='New Game', style='W.TButton', command=newgame_function)
    back_button = ttk.Button(button_frame, text='Back',
                             style='W.TButton', command=back_function)
    newgame_button.grid(column=0, row=0, padx=5, sticky=tk.EW)
    back_button.grid(column=1, row=0, padx=5, sticky=tk.EW)
    # cells = Grid(size, c, players, colors, player_number)

    ttk.Separator(orient='horizontal').pack()

    players = []
    for i in range(0, player_number):
        players.append(Player(i, colors[i]))

    c = tk.Canvas(root, height=root.winfo_height(),
                  width=root.winfo_width(), bg='white')
    c.pack()

    cells = Grid(grid_size, c, players, player_number)
    c.bind('<Configure>', cells.grid)
    c.bind('<Button-1>', cells.numbering)
    root.mainloop()


def call_join_start(root, mainScreen, widget_destroy, home_page, image_frame, player_number, grid_size, button_style,isHost,ipaddress):
       
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        widget_destroy(root)
        call_this(root, mainScreen, widget_destroy, home_page, image_frame,
                  player_number - 1, grid_size, button_style)

    def back_function():
        mainScreen(root, home_page, image_frame, button_style)

    button_frame = ttk.Frame(root)
    button_frame.pack(fill='both')
    # button_frame.columnconfigure(0, weight=40)
    newgame_button = ttk.Button(
        button_frame, text='New Game', style='W.TButton', command=newgame_function)
    back_button = ttk.Button(button_frame, text='Back',
                             style='W.TButton', command=back_function)
    newgame_button.grid(column=0, row=0, padx=5, sticky=tk.EW)
    back_button.grid(column=1, row=0, padx=5, sticky=tk.EW)
    # cells = Grid(size, c, players, colors, player_number)

    ttk.Separator(orient='horizontal').pack()

    players = []
    for i in range(0, 3):
        players.append(Player(i, colors[i]))

    c = tk.Canvas(root, height=root.winfo_height(),
                  width=root.winfo_width(), bg='white')
    c.pack()
    cells = Grid(grid_size, c, players, 3)
    c.bind('<Configure>', cells.grid)
    c.bind('<Button-1>', cells.numbering)

    def client():
        print("Client thread started:")
        tmpx=-1
        tmpy=-1
        n=Network()
        n.server=ipaddress
        n.connect()
        clock=pygame.time.Clock()
        while True:      
            clock.tick(60)      
            x,y=n.send([cells.x,cells.y,cells.played])   
            
            if not (tmpx==x and tmpy==y)and cells.played==False :
                # cells.playerIndex=nextplayer
                print(" x=",x,"y=",y)
                cells.x=x
                cells.y=y
                cells.execute()
            cells.played=False
            tmpx=x
            tmpy=y

    def server_start():
        server_run()


    if isHost==True:
        start_new_thread(server_start,())


    start_new_thread(client,())
    root.mainloop()
