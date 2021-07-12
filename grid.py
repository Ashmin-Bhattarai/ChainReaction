from network import *
import pickle
import tkinter as tk


class Grid:
    def __init__(self,playerid,color,cells,player_number):
        self.size = 8
        self.playerid = playerid
        self.cord_list = []
        self.cells = cells
        self.color = color
        self.player_number=player_number
        self.mouse=False
        self.clicked=False
        self.played=False
    
    def set_c(self,c):
        self.c=c
    
    def set_cells(self,cells):
        self.cells=cells

    def get_cells(self):
        return self.cells

    def grid(self, event=None):
        #global player, colors, cells
        self.w = self.c.winfo_width()  # Get current width of canvas
        self.h = self.c.winfo_height()  # Get current height of canvas

        self.xd = self.w//self.size
        self.yd = self.h//self.size

        self.c.delete('all')

        # Creates all vertical lines
        for i in range(0, self.w, self.xd):
            verticalLine = self.c.create_line([(i, 0), (i, self.h)], tag='grid_line', fill=self.color)
        # Creates all horizontal lines
        for i in range(0, self.h, self.yd):
            horizontalLine = self.c.create_line([(0, i), (self.w, i)], tag='grid_line', fill=self.color)
        

        # display text
        for i in range(self.size):
            for j in range(self.size):
                x = i * self.xd + self.xd//2
                y = j * self.yd + self.yd//2
                self.fill_color = self.color

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
    

    def numbering(self, event):
        print(self.mouse)
        if self.mouse==True:
            self.clicked=True
            self.x = int(event.x / (self.w//self.size))
            self.y = int(event.y / (self.h//self.size))
            
            #print(self.x, self.y)
                

    def exec(self):
        if self.isvalid():
            self.clicked=False
            self.cells[self.x][self.y][0] += 1
            self.cells[self.x][self.y][1] = self.playerid

            # self.n.send(self.cells)
            # print("client:Data sent")

            # self.playerid += 1

            # if self.player > self.player_number:
            #     self.player =1
                
            self.grid()

    def isvalid(self):

        if self.cells[self.x][self.y][1] == 0 or self.cells[self.x][self.y][1] == self.playerid:
            print("is valid true")
            self.played=True
            return True
        else:
            print("is valid false")
            return False