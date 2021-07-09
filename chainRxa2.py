from main_screen import *
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



class Grid:
    def __init__(self, size, c, players, colors):
        self.size = size
        self.c = c
        self.player = 1
        self.cord_list = []
        self.cells = [[[0 for cell in range(2)] for col in range(size)] for row in range(size)]
        self.players = players
        self.colors = colors




    def grid(self, event=None):
        #global player, colors, cells
        self.w = self.c.winfo_width()  # Get current width of canvas
        self.h = self.c.winfo_height()  # Get current height of canvas

        self.xd = self.w//self.size
        self.yd = self.h//self.size

        self.c.delete('all')

        # Creates all vertical lines
        for i in range(0, self.w, self.xd):
            verticalLine = self.c.create_line([(i, 0), (i, self.h)], tag='grid_line', fill=self.players[self.player].color)
        # Creates all horizontal lines
        for i in range(0, self.h, self.yd):
            horizontalLine = self.c.create_line([(0, i), (self.w, i)], tag='grid_line', fill=self.players[self.player].color)
        


        # display text
        for i in range(self.size):
            for j in range(self.size):
                x = i * self.xd + self.xd//2
                y = j * self.yd + self.yd//2
                self.fill_color = self.players[self.cells[i][j][1]].color

                self.c.create_text(x, y, fill=self.fill_color, text=str(self.cells[i][j][0]))
                self.drawCircles(i, j)



    
    def drawCircles(self, x, y):
        ballSize = 20 - self.size

        if self.cells[x][y][0] == 1:
            x1, y1 = (self.xd * x + self.xd/2 - ballSize), (self.yd * y + self.yd/2 - ballSize)
            x2, y2 = (self.xd * x + self.xd/2 + ballSize), (self.yd * y + self.yd/2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

        elif self.cells[x][y][0] == 2:
            x1, y1 = (self.xd * x + self.xd/2 - ballSize*2), (self.yd * y + self.yd/2 - ballSize)
            x2, y2 = (self.xd * x + self.xd/2), (self.yd * y + self.yd/2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

            x1, y1 = (self.xd * x + self.xd/2), (self.yd * y + self.yd/2 - ballSize)
            x2, y2 = (self.xd * x + self.xd/2 + ballSize*2), (self.yd * y + self.yd/2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

        elif self.cells[x][y][0] == 3:
            x1, y1 = (self.xd * x + self.xd/2 - ballSize*2), (self.yd * y + self.yd/2)
            x2, y2 = (self.xd * x + self.xd/2), (self.yd * y + self.yd/2 + ballSize*2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

            x1, y1 = (self.xd * x + self.xd/2), (self.yd * y + self.yd/2)
            x2, y2 = (self.xd * x + self.xd/2 + ballSize*2), (self.yd * y + self.yd/2 + ballSize*2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color)
            self.c.update()

            x1, y1 = (self.xd * x + self.xd/2 - ballSize), (self.yd * y + self.yd/2 - ballSize*2)
            x2, y2 = (self.xd * x + self.xd/2 + ballSize), (self.yd * y + self.yd/2)
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
        #global player, cells, cord_list
        self.x = int(event.x / (self.w//self.size))
        self.y = int(event.y / (self.h//self.size))

        #print(self.x, self.y)

        if self.isvalid(self.x, self.y):
            self.cells[self.x][self.y][0] += 1
            self.cells[self.x][self.y][1] = self.player
            #print(self.cells[self.x][self.y])
            self.cord_list = [[self.x, self.y]]

            #print("x,y, v = ", x, y, cells[x][y][0])
            self.explode()

            while len(self.cord_list) != 0:
                self.explode()

            self.player += 1

            if self.player > player_number-1:
                self.player = 1
            self.grid()

    def isvalid(self, x, y):
        global cells
        if self.cells[x][y][1] == 0 or self.cells[x][y][1] == self.player:
            return True
        else:
            return False



player_number = int(mainScreen()) + 1
players = []
for i in range(0, player_number):
    players.append(Player(i, colors[i]))



root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg='white')
c.pack()

cells = Grid(size, c, players, colors)



c.bind('<Configure>', cells.grid)
c.bind('<Button-1>', cells.numbering)

root.mainloop()
