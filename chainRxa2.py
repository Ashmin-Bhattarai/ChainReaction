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


class Grid:
    def __init__(self, size, c, players, colors, player_number):
        self.size = size
        self.c = c
        self.player = 1
        self.cord_list = []
        self.cells = [
            [[0 for cell in range(2)] for col in range(size)] for row in range(size)]
        self.players = players
        self.colors = colors
        self.player_number = player_number

    def grid(self, event=None):
        # global player, colors, cells
        self.w = self.c.winfo_width()  # Get current width of canvas
        self.h = self.c.winfo_height()  # Get current height of canvas

        self.xd = self.w // self.size
        self.yd = self.h // self.size

        self.c.delete('all')

        # Creates all vertical lines
        for i in range(0, self.w, self.xd):
            verticalLine = self.c.create_line(
                [(i, 0), (i, self.h)], tag='grid_line', fill=self.players[self.player].color)
        # Creates all horizontal lines
        for i in range(0, self.h, self.yd):
            horizontalLine = self.c.create_line(
                [(0, i), (self.w, i)], tag='grid_line', fill=self.players[self.player].color)

        # display text
        for i in range(self.size):
            for j in range(self.size):
                x = i * self.xd + self.xd // 2
                y = j * self.yd + self.yd // 2
                self.fill_color = self.players[self.cells[i][j][1]].color

                self.c.create_text(x, y, fill=self.fill_color,
                                   text=str(self.cells[i][j][0]))
                self.drawCircles(i, j)

    def drawCircles(self, x, y):
        ballSize = 20 - self.size

        if self.cells[x][y][0] == 1:
            x1, y1 = (self.xd * x + self.xd / 2 -
                      ballSize), (self.yd * y + self.yd / 2 - ballSize)
            x2, y2 = (self.xd * x + self.xd / 2 +
                      ballSize), (self.yd * y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

        elif self.cells[x][y][0] == 2:
            x1, y1 = (self.xd * x + self.xd / 2 - ballSize *
                      2), (self.yd * y + self.yd / 2 - ballSize)
            x2, y2 = (self.xd * x + self.xd / 2), (self.yd *
                                                   y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd *
                                                   y + self.yd / 2 - ballSize)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize *
                      2), (self.yd * y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

        elif self.cells[x][y][0] == 3:
            x1, y1 = (self.xd * x + self.xd / 2 - ballSize *
                      2), (self.yd * y + self.yd / 2)
            x2, y2 = (self.xd * x + self.xd / 2), (self.yd *
                                                   y + self.yd / 2 + ballSize * 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2)
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize *
                      2), (self.yd * y + self.yd / 2 + ballSize * 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2 -
                      ballSize), (self.yd * y + self.yd / 2 - ballSize * 2)
            x2, y2 = (self.xd * x + self.xd / 2 +
                      ballSize), (self.yd * y + self.yd / 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

    def explode(self):
        global cord_list
        x = self.cord_list[0][0]
        y = self.cord_list[0][1]
        if x == 0 and y == 0 and self.cells[x][y][0] >= 2:
            self.cells[x][y][0] = self.cells[x][y][0] - 2
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            self.cells[x + 1][y][0] += 1
            self.cells[x + 1][y][1] = self.player

            self.cells[x][y + 1][0] += 1
            self.cells[x][y + 1][1] = self.player

            self.cord_list.append([x + 1, y])
            self.cord_list.append([x, y + 1])

        elif x == 7 and y == 0 and self.cells[x][y][0] >= 2:
            self.cells[x][y][0] = self.cells[x][y][0] - 2
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            self.cells[x - 1][y][0] += 1
            self.cells[x - 1][y][1] = self.player

            self.cells[x][y + 1][0] += 1
            self.cells[x][y + 1][1] = self.player

            self.cord_list.append([x - 1, y])
            self.cord_list.append([x, y + 1])
            # explode(x - 1, y)
            # explode(x, y + 1)

        elif x == 0 and y == 7 and self.cells[x][y][0] >= 2:
            self.cells[x][y][0] = self.cells[x][y][0] - 2
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            self.cells[x + 1][y][0] += 1
            self.cells[x + 1][y][1] = self.player

            self.cells[x][y - 1][0] += 1
            self.cells[x][y - 1][1] = self.player

            self.cord_list.append([x + 1, y])
            self.cord_list.append([x, y - 1])
            # explode(x + 1, y)
            # explode(x, y - 1)

        elif x == 7 and y == 7 and self.cells[x][y][0] >= 2:
            self.cells[x][y][0] = self.cells[x][y][0] - 2
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            self.cells[x - 1][y][0] += 1
            self.cells[x - 1][y][1] = self.player

            self.cells[x][y - 1][0] += 1
            self.cells[x][y - 1][1] = self.player

            self.cord_list.append([x - 1, y])
            self.cord_list.append([x, y - 1])
            # explode(x - 1, y)
            # explode(x, y - 1)

        elif x == 0 and y in [1, 2, 3, 4, 5, 6] and self.cells[x][y][0] >= 3:
            self.cells[x][y][0] = self.cells[x][y][0] - 3
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            # right cell
            self.cells[x + 1][y][0] += 1
            self.cells[x + 1][y][1] = self.player

            # up cell
            self.cells[x][y - 1][0] += 1
            self.cells[x][y - 1][1] = self.player

            # down cell
            self.cells[x][y + 1][0] += 1
            self.cells[x][y + 1][1] = self.player

            self.cord_list.append([x + 1, y])
            self.cord_list.append([x, y - 1])
            self.cord_list.append([x, y + 1])
            # explode(x + 1, y)
            # explode(x, y - 1)
            # explode(x, y + 1)

        elif x == 7 and y in [1, 2, 3, 4, 5, 6] and self.cells[x][y][0] >= 3:
            self.cells[x][y][0] = self.cells[x][y][0] - 3
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            # left cell
            self.cells[x - 1][y][0] += 1
            self.cells[x - 1][y][1] = self.player

            # up cell
            self.cells[x][y - 1][0] += 1
            self.cells[x][y - 1][1] = self.player

            # down cell
            self.cells[x][y + 1][0] += 1
            self.cells[x][y + 1][1] = self.player

            self.cord_list.append([x - 1, y])
            self.cord_list.append([x, y - 1])
            self.cord_list.append([x, y + 1])
            # explode(x - 1, y)
            # explode(x, y + 1)
            # explode(x, y - 1)

        elif y == 0 and x in [1, 2, 3, 4, 5, 6] and self.cells[x][y][0] >= 3:
            self.cells[x][y][0] = self.cells[x][y][0] - 3
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            # right cell
            self.cells[x + 1][y][0] += 1
            self.cells[x + 1][y][1] = self.player

            # left cell
            self.cells[x - 1][y][0] += 1
            self.cells[x - 1][y][1] = self.player

            # down cell
            self.cells[x][y + 1][0] += 1
            self.cells[x][y + 1][1] = self.player

            self.cord_list.append([x + 1, y])
            self.cord_list.append([x - 1, y])
            self.cord_list.append([x, y + 1])
            # explode(x + 1, y)
            # explode(x - 1, y)
            # explode(x, y + 1)

        elif y == 7 and x in [1, 2, 3, 4, 5, 6] and self.cells[x][y][0] >= 3:
            self.cells[x][y][0] = self.cells[x][y][0] - 3
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            # left cell
            self.cells[x - 1][y][0] += 1
            self.cells[x - 1][y][1] = self.player

            # up cell
            self.cells[x][y - 1][0] += 1
            self.cells[x][y - 1][1] = self.player

            # right cell
            self.cells[x + 1][y][0] += 1
            self.cells[x + 1][y][1] = self.player

            self.cord_list.append([x - 1, y])
            self.cord_list.append([x + 1, y])
            self.cord_list.append([x, y - 1])
            # explode(x - 1, y)
            # explode(x + 1, y)
            # explode(x, y - 1)

        elif x in [1, 2, 3, 4, 5, 6] and y in [1, 2, 3, 4, 5, 6] and self.cells[x][y][0] >= 4:
            self.cells[x][y][0] = self.cells[x][y][0] - 4
            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            # right cell
            self.cells[x + 1][y][0] += 1
            self.cells[x + 1][y][1] = self.player

            # left cell
            self.cells[x - 1][y][0] += 1
            self.cells[x - 1][y][1] = self.player

            # up cell
            self.cells[x][y - 1][0] += 1
            self.cells[x][y - 1][1] = self.player

            # down cell
            self.cells[x][y + 1][0] += 1
            self.cells[x][y + 1][1] = self.player

            self.cord_list.append([x + 1, y])
            self.cord_list.append([x - 1, y])
            self.cord_list.append([x, y - 1])
            self.cord_list.append([x, y + 1])
            # explode(x + 1, y)
            # explode(x - 1, y)
            # explode(x, y - 1)
            # explode(x, y + 1)

        self.cord_list = self.cord_list[1:]
        # if len(cord_list) != 0:
        #     print("x,y, v = ", x, y, cells[x][y][0])
        #     explode()

    def numbering(self, event):

        # global player, cells, cord_list
        self.x = int(event.x / (self.w // self.size))
        self.y = int(event.y / (self.h // self.size))

        # print(self.x, self.y)

        if self.isvalid(self.x, self.y):
            self.cells[self.x][self.y][0] += 1
            self.cells[self.x][self.y][1] = self.player
            # print(self.cells[self.x][self.y])
            self.cord_list = [[self.x, self.y]]

            # print("x,y, v = ", x, y, cells[x][y][0])
            self.explode()

            while len(self.cord_list) != 0:
                self.explode()

            self.player += 1

            if self.player > self.player_number - 1:
                self.player = 1
            self.grid()

    def isvalid(self, x, y):
        global cells
        if self.cells[x][y][1] == 0 or self.cells[x][y][1] == self.player:
            return True
        else:
            return False


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
