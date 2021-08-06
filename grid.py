import explode


class Grid(explode.Explode):
    def __init__(self, size, players, player_number, sound_option=0):
        self.size = size
        self.player = 1
        self.cord_list = []
        self.cord_list2 = []
        self.cells = [[[0 for cell in range(2)] for col in range(size)] for row in range(size)]
        self.players = players
        self.player_number = player_number
        self.playerIndex = 1
        self.firstTime = True
        self.deletedPlayer = 0
        self.played = False
        self.x = -1
        self.y = -1
        self.myid = -1
        self.isOnline = False
        self.sound_option = sound_option
        

    def set_c(self, c):
        self.c = c

    def grid(self, event=None):
        self.w = self.c.winfo_width()  # Get current width of canvas
        self.h = self.c.winfo_height()  # Get current height of canvas

        self.xd = self.w // self.size
        self.yd = self.h // self.size


        # Creates all vertical lines
        for i in range(0, self.w, self.xd):
            verticalLine = self.c.create_line(
                [(i, 0), (i, self.h)],
                tag="grid_line",
                fill=self.players[self.playerIndex].color,
            )
        # Creates all horizontal lines
        for i in range(0, self.h, self.yd):
            horizontalLine = self.c.create_line(
                [(0, i), (self.w, i)],
                tag="grid_line",
                fill=self.players[self.playerIndex].color,
            )


    def drawCircles(self, x, y):
        ballSize = 20 - self.size
        tag = "circle_" + str(x) + "_" + str(y) + "_"
        self.fill_color = self.players[self.cells[x][y][1]].color

        if self.cells[x][y][0] == 1:

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize),
                (self.yd * y + self.yd / 2 - ballSize),
            )
            x2, y2 = (
                (self.xd * x + self.xd / 2 + ballSize),
                (self.yd * y + self.yd / 2 + ballSize),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "1")
            self.c.update()

        elif self.cells[x][y][0] == 2:

            self.c.delete(tag + "1")

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize * 2),
                (self.yd * y + self.yd / 2 - ballSize),
            )
            x2, y2 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2 + ballSize)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "1")
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2 - ballSize)
            x2, y2 = (
                (self.xd * x + self.xd / 2 + ballSize * 2),
                (self.yd * y + self.yd / 2 + ballSize),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "2")
            self.c.update()

        elif self.cells[x][y][0] == 3 and (
            [x, y]
            not in [
                [0, 0],
                [0, self.size - 1],
                [self.size - 1, 0],
                [self.size - 1, self.size - 1],
            ]
        ):

            self.c.delete(tag + "1")
            self.c.delete(tag + "2")

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize * 2),
                (self.yd * y + self.yd / 2),
            )
            x2, y2 = (
                (self.xd * x + self.xd / 2),
                (self.yd * y + self.yd / 2 + ballSize * 2),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "1")
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2)
            x2, y2 = (
                (self.xd * x + self.xd / 2 + ballSize * 2),
                (self.yd * y + self.yd / 2 + ballSize * 2),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "2")
            self.c.update()

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize),
                (self.yd * y + self.yd / 2 - ballSize * 2),
            )
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize), (self.yd * y + self.yd / 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "3")
            self.c.update()

        elif (
            self.cells[x][y][0] == 4
            and x in range(1, self.size - 1)
            and y in range(1, self.size - 1)
        ):

            self.c.delete(tag + "1")
            self.c.delete(tag + "2")
            self.c.delete(tag + "3")

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize * 2),
                (self.yd * y + self.yd / 2),
            )
            x2, y2 = (
                (self.xd * x + self.xd / 2),
                (self.yd * y + self.yd / 2 + ballSize * 2),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "1")
            self.c.update()

            x1, y1 = (self.xd * x + self.xd / 2), (self.yd * y + self.yd / 2)
            x2, y2 = (
                (self.xd * x + self.xd / 2 + ballSize * 2),
                (self.yd * y + self.yd / 2 + ballSize * 2),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "2")
            self.c.update()

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize),
                (self.yd * y + self.yd / 2 - ballSize * 2),
            )
            x2, y2 = (self.xd * x + self.xd / 2 + ballSize), (self.yd * y + self.yd / 2)
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "3")
            self.c.update()

            x1, y1 = (
                (self.xd * x + self.xd / 2 - ballSize),
                (self.yd * y + self.yd / 2 + ballSize * 2),
            )
            x2, y2 = (
                (self.xd * x + self.xd / 2 + ballSize),
                (self.yd * y + self.yd / 2 + ballSize * 4),
            )
            self.c.create_oval(x1, y1, x2, y2, fill=self.fill_color, tag=tag + "4")
            self.c.update()



    def checkstatus(self):
        ballNum = [0 for _ in self.players]
        if not self.firstTime:
            for x in range(0, self.size):
                for y in range(0, self.size):
                    ballNum[self.cells[x][y][1]] = (
                        ballNum[self.cells[x][y][1]] + self.cells[x][y][0]
                    )
            pop_list = []
            for num in range(1, len(ballNum)):
                if ballNum[num] == 0:
                    pop_list.append(num)
                    self.player_number -= 1

                    for i in range(0, self.size):
                        for j in range(0, self.size):
                            if self.cells[i][j][1] >= num:
                                self.cells[i][j][1] -= 1

                    if self.myid == num:
                        self.myid = 99999

                    elif self.myid > num:
                        self.myid -= 1

                    for player in self.players:
                        if player.id >= num:
                            player.id -= 1
            pop_list.reverse()
            for i in pop_list:
                self.players.pop(i)

            if len(self.players) == 2:
                self.c.delete("all")
                string = "Player %a Won the Game !!" % (self.players[1].name)
                self.c.create_text(
                    (self.w + len(string)) // 2,
                    (self.h / 2) - 50,
                    font="Arial 40 bold",
                    fill=self.players[1].color,
                    text=string,
                )

    def numbering(self, event):

        if self.myid == self.playerIndex or not self.isOnline:
            self.x = int(event.x / (self.w // self.size))
            self.y = int(event.y / (self.h // self.size))
            if self.isvalid(self.x, self.y):
                self.played = True
            self.execute()

    def execute(self):
        if self.isvalid(self.x, self.y):
            self.cells[self.x][self.y][0] += 1
            self.cells[self.x][self.y][1] = self.player

            self.cord_list2 = [[[self.x, self.y]]]

            self.drawCircles(self.x, self.y)
            while len(self.cord_list2) != 0:
                self.explode2()

            self.checkstatus()

            self.playerIndex += 1
            if self.playerIndex > (self.player_number - 1):
                self.playerIndex = 1
                self.firstTime = False
            self.player = self.players[self.playerIndex].id
            if len(self.players) != 2:
                self.grid()

    def isvalid(self, x, y):
        global cells
        if self.cells[x][y][1] == 0 or self.cells[x][y][1] == self.player:
            return True
        else:
            return False
