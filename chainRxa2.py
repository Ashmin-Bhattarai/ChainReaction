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


def call_this(
    root,
    mainScreen,
    widget_destroy,
    home_page,
    image_frame,
    player_number,
    grid_size,
    button_style,
):
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    # print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        widget_destroy(root)
        call_this(
            root,
            mainScreen,
            widget_destroy,
            home_page,
            image_frame,
            player_number - 1,
            grid_size,
            button_style,
        )

    def back_function():
        mainScreen(root, home_page, image_frame, button_style)

    button_frame = ttk.Frame(root)
    button_frame.pack(fill="both")

    newgame_button = ttk.Button(
        button_frame, text="New Game", style="W.TButton", command=newgame_function
    )
    back_button = ttk.Button(
        button_frame, text="Back", style="W.TButton", command=back_function
    )
    newgame_button.grid(column=0, row=0, padx=5, sticky=tk.EW)
    back_button.grid(column=1, row=0, padx=5, sticky=tk.EW)

    ttk.Separator(orient="horizontal").pack()

    players = []
    for i in range(0, player_number):
        players.append(Player(i, colors[i]))

    c = tk.Canvas(
        root, height=root.winfo_height(), width=root.winfo_width(), bg="white"
    )
    c.pack()

    cells = Grid(grid_size, players, player_number)
    cells.set_c(c)
    c.bind("<Configure>", cells.grid)
    c.bind("<Button-1>", cells.numbering)
    root.mainloop()


def call_join_start(
    root,
    local_page,
    call_join,
    widget_destroy,
    home_page,
    image_frame,
    player_number,
    grid_size,
    button_style,
    isHost,
    ipaddress,
):
    global cells
    # print("call_join_start ip address=",ipaddress)
    player_number, grid_size = int(player_number) + 1, int(grid_size)
    # print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    def newgame_function():
        widget_destroy(root)
        call_join_start(
            root,
            local_page,
            call_join,
            widget_destroy,
            home_page,
            image_frame,
            player_number - 1,
            grid_size,
            button_style,
            isHost,
            ipaddress,
        )

    def back_function():
        call_join(
            root,
            local_page,
            widget_destroy,
            image_frame,
            button_style,
            home_page,
            isHost,
        )

    button_frame = ttk.Frame(root)
    button_frame.pack(fill="both")

    newgame_button = ttk.Button(
        button_frame, text="New Game", style="W.TButton", command=newgame_function
    )
    back_button = ttk.Button(
        button_frame, text="Back", style="W.TButton", command=back_function
    )
    newgame_button.grid(column=0, row=0, padx=5, sticky=tk.N)
    back_button.grid(column=1, row=0, padx=5, sticky=tk.N)

    ttk.Separator(orient="horizontal").pack()

    # players = []
    # for i in range(0, player_number):
    #     players.append(Player(i, colors[i]))
    def server_start():
        server_run()

    if isHost == True:
        start_new_thread(server_start, ())

    c = tk.Canvas(
        root, height=root.winfo_height(), width=root.winfo_width(), bg="white"
    )
    c.pack()
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

    cells.set_c(c)
    c.bind("<Configure>", cells.grid)
    c.bind("<Button-1>", cells.numbering)
    # print("Client thread started:")

    def client():
        global cells
        tmpx = -1
        tmpy = -1

        clock = pygame.time.Clock()
        cord_list = []
        first_time = True

        while True:
            clock.tick(1)
            x, y, gamestart = n.send([cells.x, cells.y, cells.played])
            print("x=", x, "y=", y)
            # print (gamestart)
            if first_time:
                cord_list.insert(0, [x, y])
            else:
                cord_list.insert(0, [x, y])
                if len(cord_list) > 2:
                    cord_list.pop()
                print("cordlist 0 , 1=", cord_list[0], cord_list[1])

            if not first_time:
                if cord_list[0] != cord_list[1]:
                    cells.x = x
                    cells.y = y
                    cells.execute()
            cells.played = False
            first_time = False

    start_new_thread(client, ())
    root.mainloop()
