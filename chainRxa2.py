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


def call_this(
    root,
    mainScreen,
    widget_destroy,
    home_page,
    image_frame,
    player_number,
    grid_size,
    button_style,
    sound_option,
):
    player_number, grid_size = int(player_number) + 1, int(grid_size)

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
            sound_option,
        )

    def back_function():
        mainScreen(root, home_page, image_frame, button_style, sound_option)

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

    cells = Grid(grid_size, players, player_number, sound_option)
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
    isHostOnly,
    ipaddress,
    sound_option,
):
    global cells, game_start
    player_number, grid_size = int(player_number) + 1, int(grid_size)

    # def newgame_function():
    #     global player_count

    #     if isHost:
    #         player_count = 1

    #     widget_destroy(root)
    #     call_join_start(
    #         root,
    #         local_page,
    #         call_join,
    #         widget_destroy,
    #         home_page,
    #         image_frame,
    #         player_number - 1,
    #         grid_size,
    #         button_style,
    #         isHost,
    #         isHostOnly,
    #         ipaddress,
    #         sound_option,
    #     )

    def back_function():
        call_join(
            root,
            local_page,
            widget_destroy,
            image_frame,
            button_style,
            home_page,
            isHost,
            sound_option,
        )

    def call_again():
        button_frame = ttk.Frame(root)
        button_frame.pack(fill="both")

        # newgame_button = ttk.Button(
        #     button_frame, text="New Game", style="W.TButton", command=newgame_function
        # )
        back_button = ttk.Button(
            button_frame, text="Back", style="W.TButton", command=back_function
        )
        # newgame_button.grid(column=0, row=0, padx=5, sticky=tk.N)
        back_button.grid(column=1, row=0, padx=5, sticky=tk.N)

        ttk.Separator(orient="horizontal").pack()
        c = tk.Canvas(
            root, height=root.winfo_height(), width=root.winfo_width(), bg="white"
        )
        c.pack()

        cells.set_c(c)

        c.bind("<Configure>", cells.grid)
        c.bind("<Button-1>", cells.numbering)

        root.mainloop()

    def waiting_page():
        global game_start
        widget_destroy(root)
        image_frame()
        new_frame = ttk.Frame(root, relief="raised", borderwidth=2)

        if not isHost:
            new_frame.place(x=228, y=390)
            text = f"Waiting other to join"

        else:
            text = f"Your IP Address is: {ipaddress}"
            new_frame.place(x=185, y=390)

        ip_label = ttk.Label(new_frame, style="W.TLabel", text=text)
        ip_label.grid(column=0, row=0, padx=5, sticky=tk.N)
        if not isHostOnly:
            def cancel():
                global game_start
                if game_start:
                    call_again()
                root.after(1000, cancel)

            root.after(1000, cancel)
        root.mainloop()

    def server_start():
        server_run(sound_option)

    if isHost == True:
        start_new_thread(server_start, ())

    n = Network()
    n.server = ipaddress
    n.connect()

    if not isHostOnly:
        if not isHost:
            server_get = n.send([isHostOnly, isHost])
        else:
            server_get = n.send([isHostOnly, isHost, player_number - 1, grid_size])
        cells = server_get[0]
        cells.myid = server_get[1]
        cells.isOnline = True

        def client():
            global cells, game_start
            tmpx = -1
            tmpy = -1

            clock = pygame.time.Clock()
            cord_list = []
            first_time = True

            while True:
                clock.tick(60)
                x, y, game_start, I = n.send([cells.x, cells.y, cells.playerIndex])

                if first_time:
                    cord_list.insert(0, [x, y, I])

                else:
                    cord_list.insert(0, [x, y, I])
                    if len(cord_list) > 2:
                        cord_list.pop()

                if not first_time:
                    if (
                        cord_list[0][2] != cord_list[1][2]
                        and cord_list[0][2] != cells.player
                    ):

                        cells.x = x
                        cells.y = y
                        cells.execute()

                first_time = False

        start_new_thread(client, ())

    else:
        if not isHost:
            server_get = n.send([isHostOnly, isHost])
        else:

            server_get = n.send([isHostOnly, isHost, player_number - 1, grid_size])

    waiting_page()
