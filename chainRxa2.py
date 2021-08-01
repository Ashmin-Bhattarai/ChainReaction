import pygame
from grid import Grid
import tkinter as tk
from tkinter import ttk
from network import *
from _thread import *
from server import *
from player import *

player = 1
cells = 0
game_start = False


def call_this(root, mainScreen, widget_destroy, home_page, image_frame, player_number, grid_size, button_style, sound_option):
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    # print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        widget_destroy(root)
        call_this(root, mainScreen, widget_destroy, home_page, image_frame,
                  player_number - 1, grid_size, button_style, sound_option)

    def back_function():
        mainScreen(root, home_page, image_frame, button_style, sound_option)

    button_frame = ttk.Frame(root)
    button_frame.pack(fill='both')

    newgame_button = ttk.Button(
        button_frame, text='New Game', style='W.TButton', command=newgame_function)
    back_button = ttk.Button(button_frame, text='Back',
                             style='W.TButton', command=back_function)
    newgame_button.grid(column=0, row=0, padx=5, sticky=tk.EW)
    back_button.grid(column=1, row=0, padx=5, sticky=tk.EW)

    ttk.Separator(orient='horizontal').pack()

    players = []
    for i in range(0, player_number):
        players.append(Player(i, colors[i]))

    c = tk.Canvas(root, height=root.winfo_height(),
                  width=root.winfo_width(), bg='white')
    c.pack()

    cells = Grid(grid_size, players, player_number, sound_option)
    cells.set_c(c)
    c.bind('<Configure>', cells.grid)
    c.bind('<Button-1>', cells.numbering)
    root.mainloop()


def call_join_start(root, local_page, call_join, widget_destroy, home_page, image_frame, player_number, grid_size, button_style, isHost, ipaddress, sound_option):
    global cells, game_start
    # print("call_join_start ip address=",ipaddress)
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    # print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        widget_destroy(root)
        call_join_start(root, local_page, call_join, widget_destroy, home_page, image_frame, player_number - 1, grid_size, button_style, isHost, ipaddress, sound_option)

    def back_function():
        call_join(root, local_page, widget_destroy, image_frame, button_style, home_page, isHost, sound_option)

    def call_again():
        button_frame = ttk.Frame(root)
        button_frame.pack(fill='both')

        newgame_button = ttk.Button(button_frame, text='New Game', style='W.TButton', command=newgame_function)
        back_button = ttk.Button(button_frame, text='Back', style='W.TButton', command=back_function)
        newgame_button.grid(column=0, row=0, padx=5, sticky=tk.N)
        back_button.grid(column=1, row=0, padx=5, sticky=tk.N)

        ttk.Separator(orient='horizontal').pack()
        c = tk.Canvas(root, height=root.winfo_height(),
                      width=root.winfo_width(), bg='white')
        c.pack()

        cells.set_c(c)

        c.bind('<Configure>', cells.grid)
        c.bind('<Button-1>', cells.numbering)
        # print("Client thread started:")

        root.mainloop()

    def waiting_page():
        global game_start
        widget_destroy(root)
        image_frame()
        new_frame = ttk.Frame(root, relief='raised', borderwidth=2)
        new_frame.place(x=210, y=512.5)

        if not isHost:
            text = f'Waiting other to join'
            # ip_label = ttk.Label(new_frame, style='W.TLabel', text=text)
            # ip_label.grid(column=0, row=0, padx=5, sticky=tk.N)

        else:
            text = f'Your IP Address is: {ipaddress}'

        ip_label = ttk.Label(new_frame, style='W.TLabel', text=text)
        ip_label.grid(column=0, row=0, padx=5, sticky=tk.N)

        def cancel():
            global game_start
            print(f'inside cancel game_start = {game_start}')
            if game_start:
                call_again()
            root.after(1000, cancel)

        root.after(1000, cancel)
        root.mainloop()

    def server_start():
        server_run(sound_option)

    if isHost == True:
        start_new_thread(server_start, ())

    # cells = Grid(grid_size, c, players, 3)
    n = Network()
    n.server = ipaddress
    n.connect()
    if not isHost:
        server_get = n.send([isHost])
    else:
        server_get = n.send([isHost, player_number - 1, grid_size])
    cells = server_get[0]
    cells.myid = server_get[1]
    cells.isOnline = True
    # print(cells.myid)

    def client():
        global cells, game_start
        tmpx = -1
        tmpy = -1

        clock = pygame.time.Clock()

        while True:
            clock.tick(10)
            x, y, game_start = n.send([cells.x, cells.y, cells.played])
            # print (game_start)

            if not (tmpx == x and tmpy == y) and cells.played == False:
                # cells.playerIndex=nextplayer
                # print(" x=", x, "y=", y)
                cells.x = x
                cells.y = y
                cells.execute()
            cells.played = False
            tmpx = x
            tmpy = y

    start_new_thread(client, ())

    waiting_page()
    # while not game_start:
    #     print(f'waiting, gamestart = {game_start}')
    # widget_destroy(root)
