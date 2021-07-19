import tkinter as tk
import time
import explode
import threading


class Grid(explode.Explode):
    def __init__(self, size, c, players, player_number):
        self.size = size
        self.c = c
        self.player = 1
        self.cord_list = []
        self.cells = [[[0 for cell in range(2)] for col in range(size)] for row in range(size)]
        self.players = players
        self.player_number = player_number
        self.playerIndex = 1
        self.firstTime = True
        self.deletedPlayer = 0
        self.played = False
        self.x = -1
        self.y = -1

    def grid(self, event=None):
        #global player, colors, cells
        self.w = self.c.winfo_width()  # Get current width of canvas
        self.h = self.c.winfo_height()  # Get current height of canvas

        self.xd = self.w // self.size
        self.yd = self.h // self.size

        # self.c.delete('all')

        # Creates all vertical lines
        for i in range(0, self.w, self.xd):
            verticalLine = self.c.create_line([(i, 0), (i, self.h)], tag='grid_line', fill=self.players[self.playerIndex].color)
        # Creates all horizontal lines
        for i in range(0, self.h, self.yd):
            horizontalLine = self.c.create_line([(0, i), (self.w, i)], tag='grid_line', fill=self.players[self.playerIndex].color)

        # display text
        # for i in range(self.size):
        #     for j in range(self.size):
        #         x = i * self.xd + self.xd//2
        #         y = j * self.yd + self.yd//2

        #         self.c.create_text(x, y, fill=self.fill_color, text=str(self.cells[i][j][0]))
        #         #self.drawCircles(i, j)

    def drawCircles(self, x, y):
        ballSize = 20 - self.size
        tag = "circle_" + str(x) + "_" + str(y) + "_"
        self.fill_color = self.players[self.cells[x][y][1]].color

        if self.cells[x][y][0] == 1:

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize), (self.yd * y + self.yd / 2 - ballSize)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize), (self.yd * y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "1")
            self.c.update()

        elif self.cells[x][y][0] == 2:

            self.c.delete(tag + "1")

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize * 2), (self.yd * y + self.yd / 2 - ballSize)
            x2, y2 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '1')
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2 - ballSize)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize * 2), (self.yd * y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '2')
            self.c.update()

        elif self.cells[x][y][0] == 3:

            self.c.delete(tag + "1")
            self.c.delete(tag + "2")

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize * 2), (self.yd * y + self.yd / 2)
            x2, y2 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2 + ballSize * 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '1')
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize * 2), (self.yd * y + self.yd / 2 + ballSize * 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '2')
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize), (self.yd * y + self.yd / 2 - ballSize * 2)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize), (self.yd * y + self.yd / 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '3')
            self.c.update()

        elif self.cells[x][y][0] == 4:

            self.c.delete(tag + "1")
            self.c.delete(tag + "2")
            self.c.delete(tag + "3")

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize * 2), (self.yd * y + self.yd / 2)
            x2, y2 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2 + ballSize * 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '1')
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize * 2), (self.yd * y + self.yd / 2 + ballSize * 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '2')
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize), (self.yd * y + self.yd / 2 - ballSize * 2)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize), (self.yd * y + self.yd / 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '3')
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2 - ballSize), (self.yd * y + self.yd / 2 + ballSize * 2)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize), (self.yd * y + self.yd / 2 + ballSize * 4)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + '4')
            self.c.update()

    def animate_corner(self, tag, x1, y1, x2, y2):
        print("Inside animate")
        #tag = "circle_" + str(x) + "_" + str(y) + "_"
        self.i = 0

        def move_circle():
            print("Inside move")
            self.c.move(tag + "1", x1, y1)
            self.c.move(tag + "2", x2, y2)
            self.c.update()
            self.i += 1
            print(self.i)
            if self.i >= self.xd:
                return
            else:
                # time.sleep(0.001)
                move_circle()
            #self.c.after(2, move_circle)
        move_circle()

    def animate_edge(self, tag, x1, y1, x2, y2, x3, y3):
        print("Inside animate")
        #tag = "circle_" + str(x) + "_" + str(y) + "_"
        self.i = 0

        def move_circle():
            print("Inside move")
            self.c.move(tag + "1", x1, y1)
            self.c.move(tag + "2", x2, y2)
            self.c.move(tag + "3", x3, y3)
            self.c.update()
            self.i += 1
            print(self.i)
            if self.i >= self.xd:
                return
            else:
                # time.sleep(0.001)
                move_circle()
            #self.c.after(2, move_circle)
        move_circle()

    def animate_middle(self, tag, x1, y1, x2, y2, x3, y3, x4, y4):
        print("Inside animate")
        #tag = "circle_" + str(x) + "_" + str(y) + "_"
        self.i = 0

        def move_circle():
            print("Inside move")
            self.c.move(tag + "1", x1, y1)
            self.c.move(tag + "2", x2, y2)
            self.c.move(tag + "3", x3, y3)
            self.c.move(tag + "4", x4, y4)
            self.c.update()
            self.i += 1
            print(self.i)
            if self.i >= self.xd:
                return
            else:
                # time.sleep(0.001)
                move_circle()
            #self.c.after(2, move_circle)
        move_circle()

    def checkstatus(self):
        ballNum = [0 for _ in self.players]
        if not self.firstTime:
            for x in range(0, self.size):
                for y in range(0, self.size):
                    ballNum[self.cells[x][y][1]] = ballNum[self.cells[x][y][1]] + self.cells[x][y][0]
                    #print(ballNum[self.cells[x][y][1]], self.cells[x][y][1], self.cells[x][y][0])
            print(ballNum)

            for num in range(1, len(ballNum)):
                print(num)
                if ballNum[num] == 0:
                    self.players.pop(num)
                    print("chekpoint checkstatus")
                    self.player_number -= 1

                    for i in range(0, self.size):
                        for j in range(0, self.size):
                            if self.cells[i][j][1] >= num:
                                self.cells[i][j][1] -= 1

                    for player in self.players:
                        if player.id >= num:
                            player.id -= 1

            if len(self.players) == 2:
                print("Win By: ", self.players[1].color)
                self.c.delete("all")
                string = "Player %a Won the Game !!" % (self.players[1].name)
                self.c.create_text((self.w + len(string)) // 2, (self.h / 2) - 50, font="Arial 40 bold", fill=self.players[1].color, text=string)

    def numbering(self, event):
        #global player, cells, cord_list
        self.x = int(event.x / (self.w // self.size))
        self.y = int(event.y / (self.h // self.size))
        self.execute()
        #print(self.x, self.y)

    def execute(self):
        if self.isvalid(self.x, self.y):
            self.played = True
            self.cells[self.x][self.y][0] += 1
            self.cells[self.x][self.y][1] = self.player
            self.cord_list = [[self.x, self.y]]
            # print(self.cells[self.x][self.y])
            #print("x,y, v = ", self.x, self.y, self.cells[self.x][self.y][0])

            self.drawCircles(self.x, self.y)

            # def test():
            #     self.explode()

            # thread = []
            # i=0
            while len(self.cord_list) != 0:
                # thread.append(threading.Thread(target = test))
                # thread[i].start()
                # i += 1
                self.explode()
                # self.play_sound('soundeffects/explode.wav')
            # for t in thread:
            #     t.join()

            self.checkstatus()
            print("before")
            self.playerIndex += 1
            print("player index=", self.playerIndex, "player number=", self.player_number)
            print("after")
            if self.playerIndex > (self.player_number - 1):
                self.playerIndex = 1
                self.firstTime = False
            self.player = self.players[self.playerIndex].id
            print("player=", self.player, "player index=", self.playerIndex)
            if len(self.players) != 2:
                self.grid()

    def isvalid(self, x, y):
        global cells
        if self.cells[x][y][1] == 0 or self.cells[x][y][1] == self.player:
            return True
        else:
            return False
