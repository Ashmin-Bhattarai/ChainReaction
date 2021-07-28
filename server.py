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


def server_run():
    global player_count

    game_start = False

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    server = ipaddress
    port = 5555
    # port = 5555
    # print(server)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        print(e)

    s.listen()

    global playerindex, x, y, played, playerChange
    playerindex = x = y = -1
    played = False
    playerChange = False
    clock = pygame.time.Clock()
    players = []

    def host_initialize():
        global cells
        for i in range(0, max_player + 1):
            players.append(Player(i, colors[i]))
        # print("inside function=",grid_size)
        cells = Grid(grid_size, players, max_player + 1)

    def threaded_client(conn):
        global playerindex, x, y, played, playerChange, player_count, max_player, cells, grid_size
        run = True
        isHost = pickle.loads(conn.recv(2048))
        if direct_run == True:
            isHost[0] = True
            isHost.append(max_player)
            isHost.append(grid_size)
        print("is host=", isHost)
        if isHost[0]:
            max_player = isHost[1]
            grid_size = isHost[2]
            # print("inside if=",grid_size)
            # max_player=isHost[1]
            # max_player=isHost[1]
            # print("max_player=",max_player)
            # cells.size=isHost[2]
            host_initialize()
        # print("grid size=",cells.size)
        conn.sendall(pickle.dumps([cells, player_count]))
        while run:
            # clock.tick(60)
            try:
                Tx, Ty, Tplayed = pickle.loads(conn.recv(2048))
                print("x=", Tx, "y=", Ty, "played=", Tplayed)
                # print(playerindex,x,y,played)
                # playerChange=False
                if Tplayed == True:
                    x = Tx
                    y = Ty
                if player_count != max_player:
                    game_start = False
                else:
                    game_start = True
                conn.sendall(pickle.dumps([x, y, game_start]))
                Tplayed = False
            except socket.error as e:
                print("disconnected")
                run = False
        # playerindex = x = y = -1
        played = False
        playerChange = False
        player_count -= 1
        conn.close()
        sys.exit()

    while True:
        conn, addr = s.accept()
        # print("connected to: ", addr)
        player_count += 1
        start_new_thread(threaded_client, (conn,))


if __name__ == "__main__":
    max_player = 2
    grid_size = 8
    direct_run = True
    server_run()
