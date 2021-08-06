import socket
from _thread import *
import pickle
import pygame
import sys
from grid import Grid
from player import *

player_count = 0
max_player = 2
cells = 0
grid_size = 8
direct_run = False
p = -1


def server_run(sound_option):
    global player_count, p

    game_start = False

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    server = ipaddress
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        print(e)

    s.listen()

    global playerindex, x, y, played, p
    playerindex = x = y = -1
    clock = pygame.time.Clock()
    players = []

    def host_initialize():
        global cells
        for i in range(0, max_player + 1):
            players.append(Player(i, colors[i]))
        cells = Grid(grid_size, players, max_player + 1, sound_option)

    def threaded_client(conn):
        global playerindex, x, y, player_count, max_player, cells, grid_size, p
        run = True
        isHost = pickle.loads(conn.recv(2048))
        if direct_run == True:
            isHost[1] = True
            isHost.append(max_player)
            isHost.append(grid_size)
        if isHost[1]:
            max_player = isHost[2]
            grid_size = isHost[3]

            host_initialize()

        conn.sendall(pickle.dumps([cells, player_count]))
        if isHost[0]:
            player_count -= 1
            conn.close()
            sys.exit()
        cord_list = []
        first_time = True
        while run:
            print("Player_count",player_count,"max_player",max_player)
            try:
                Tx, Ty, TI = pickle.loads(conn.recv(2048))

                if first_time:
                    cord_list.insert(0, [Tx, Ty, TI])

                else:
                    cord_list.insert(0, [Tx, Ty, TI])
                    if len(cord_list) > 2:
                        cord_list.pop()

                if not first_time:
                    if cord_list[0] != cord_list[1]:
                        x = Tx
                        y = Ty
                        p = TI

                first_time = False

                if player_count != max_player:
                    game_start = False
                else:
                    game_start = True
                conn.sendall(pickle.dumps([x, y, game_start, p]))
            except socket.error as e:
                print("disconnected")
                run = False
        player_count -= 1
        conn.close()
        sys.exit()

    print("Server is online")
    while True:        
        conn, addr = s.accept()
        print("connected to: ", addr)
        player_count += 1
        start_new_thread(threaded_client, (conn,))
