import pygame
import threading
import sys
import time


class Explode:
    def explode(self):
        global cord_list
        x = self.cord_list[0][0]
        y = self.cord_list[0][1]
        # print(x, y)
        # self.removeCircles(x, y)
        tag = "circle_" + str(x) + "_" + str(y) + "_"

        # Upper Left Corner
        if x == 0 and y == 0 and self.cells[x][y][0] >= 2:
            # print("satisfy")
            self.animate_corner(tag, 1, 0, 0, 1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')

            self.drawCircles(x + 1, y)
            self.drawCircles(x, y + 1)

        # Upper Right Corner
        elif x == self.size - 1 and y == 0 and self.cells[x][y][0] >= 2:

            self.animate_corner(tag, -1, 0, 0, 1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')

            self.drawCircles(x - 1, y)
            self.drawCircles(x, y + 1)
            # explode(x - 1, y)
            # explode(x, y + 1)

        # lower left corner
        elif x == 0 and y == self.size - 1 and self.cells[x][y][0] >= 2:
            self.animate_corner(tag, 1, 0, 0, -1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')

            self.drawCircles(x + 1, y)
            self.drawCircles(x, y - 1)
            # explode(x + 1, y)
            # explode(x, y - 1)
        # lower right corner
        elif x == self.size - 1 and y == self.size - 1 and self.cells[x][y][0] >= 2:
            self.animate_corner(tag, -1, 0, 0, -1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')

            self.drawCircles(x - 1, y)
            self.drawCircles(x, y - 1)
            # explode(x - 1, y)
            # explode(x, y - 1)

        # left edge
        elif x == 0 and y in range(1, self.size - 1) and self.cells[x][y][0] >= 3:
            self.animate_edge(tag, 0, 1, 1, 0, 0, -1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')
            # self.c.delete(tag + '3')

            self.drawCircles(x + 1, y)
            self.drawCircles(x, y - 1)
            self.drawCircles(x, y + 1)
            # explode(x + 1, y)
            # explode(x, y - 1)
            # explode(x, y + 1)

        # right edge
        elif (x == self.size - 1 and y in range(1, self.size - 1) and self.cells[x][y][0] >= 3):
            self.animate_edge(tag, -1, 0, 0, 1, 0, -1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')
            # self.c.delete(tag + '3')

            self.drawCircles(x - 1, y)
            self.drawCircles(x, y - 1)
            self.drawCircles(x, y + 1)
            # explode(x - 1, y)
            # explode(x, y + 1)
            # explode(x, y - 1)

        # upper edge
        elif y == 0 and x in range(1, self.size - 1) and self.cells[x][y][0] >= 3:
            self.animate_edge(tag, -1, 0, 1, 0, 0, 1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')
            # self.c.delete(tag + '3')

            self.drawCircles(x + 1, y)
            self.drawCircles(x - 1, y)
            self.drawCircles(x, y + 1)
            # explode(x + 1, y)
            # explode(x - 1, y)
            # explode(x, y + 1)

        # lower edge
        elif (
            y == self.size - 1
            and x in range(1, self.size - 1)
            and self.cells[x][y][0] >= 3
        ):
            self.animate_edge(tag, -1, 0, 1, 0, 0, -1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')
            # self.c.delete(tag + '3')

            self.drawCircles(x - 1, y)
            self.drawCircles(x + 1, y)
            self.drawCircles(x, y - 1)
            # explode(x - 1, y)
            # explode(x + 1, y)
            # explode(x, y - 1)

        # middle
        elif (
            x in range(1, self.size - 1)
            and y in range(1, self.size - 1)
            and self.cells[x][y][0] >= 4
        ):
            self.animate_middle(tag, -1, 0, 1, 0, 0, -1, 0, 1)
            # self.play_sound()
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

            # self.c.delete(tag + '1')
            # self.c.delete(tag + '2')
            # self.c.delete(tag + '3')
            # self.c.delete(tag + '4')

            self.drawCircles(x + 1, y)
            self.drawCircles(x - 1, y)
            self.drawCircles(x, y - 1)
            self.drawCircles(x, y + 1)
            # explode(x + 1, y)
            # explode(x - 1, y)
            # explode(x, y - 1)
            # explode(x, y + 1)

        self.drawCircles(x, y)
        self.cord_list = self.cord_list[1:]
        # if len(cord_list) != 0:
        #     print("x,y, v = ", x, y, cells[x][y][0])
        #     explode()

    def adjustCell(self):
        # print("inside adjustCell")
        nextGen = []
        for blist in self.blastList:
            x, y, n, d = blist[0], blist[1], blist[2], blist[3]
            tag = "circle_" + str(x) + "_" + str(y) + "_"

            self.cells[x][y][0] = self.cells[x][y][0] - n

            if self.cells[x][y][0] == 0:
                self.cells[x][y][1] = 0
            else:
                self.cells[x][y][1] = self.player

            for i in range(0, n):
                self.cells[(x + d[i][0])][(y + d[i][1])][0] += 1
                self.cells[(x + d[i][0])][(y + d[i][1])][1] = self.player

                if [x + d[i][0], y + d[i][1]] not in nextGen:
                    nextGen.append([x + d[i][0], y + d[i][1]])

                self.c.delete(tag + str(i + 1))
                self.drawCircles(x + d[i][0], y + d[i][1])

            self.drawCircles(x, y)
        if len(nextGen) != 0:
            self.cord_list2.append(nextGen)

    def animate(self):
        self.i = 0
        self.vel = 5
        # print("inside animate")

        def moveCircle():

            for blist in self.blastList:
                x, y, n, d = blist[0], blist[1], blist[2], blist[3]
                tag = "circle_" + str(x) + "_" + str(y) + "_"
                # self.play_sound()
                for i in range(0, n):
                    # print("Inside animate: ",tag + str(i+1))
                    self.c.move(tag + str(i + 1),
                                d[i][0] * self.vel, d[i][1] * self.vel)
                self.c.update()

            self.i += self.vel
            if self.i >= self.xd:
                return
            else:
                # print("sleep")
                # time.sleep(0.1)
                moveCircle()
        if len(self.blastList) != 0:
            moveCircle()

    def explode2(self):

        pygame.mixer.init()

        def play_sound():
            if self.sound_option:
                pygame.mixer.music.load("soundeffects/explode.wav")
                pygame.mixer.music.play()

        #print("inside explode2")
        self.blastList = []  # [x, y, 2 for corners 3 for edge 4 for middle, [direction] ]

        firstGen = self.cord_list2[0]

        for cord in firstGen:
            x, y = cord[0], cord[1]

            # Upper Left Corner
            if x == 0 and y == 0 and self.cells[x][y][0] >= 2:
                # print("satisfy")
                #self.animate_corner(tag, 1, 0, 0, 1)
                self.blastList.append([x, y, 2, [[1, 0], [0, 1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # Upper Right Corner
            elif x == self.size - 1 and y == 0 and self.cells[x][y][0] >= 2:
                # self.animate_corner(tag, -1, 0, 0, 1)
                self.blastList.append([x, y, 2, [[-1, 0], [0, 1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # lower left corner
            elif x == 0 and y == self.size - 1 and self.cells[x][y][0] >= 2:
                # self.animate_corner(tag, 1, 0, 0, -1)
                self.blastList.append([x, y, 2, [[1, 0], [0, -1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # lower right corner
            elif x == self.size - 1 and y == self.size - 1 and self.cells[x][y][0] >= 2:
                # self.animate_corner(tag, -1, 0, 0, -1)
                self.blastList.append([x, y, 2, [[-1, 0], [0, -1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # left edge
            elif x == 0 and y in range(1, self.size - 1) and self.cells[x][y][0] >= 3:
                # self.animate_edge(tag, 0, 1, 1, 0, 0, -1)
                self.blastList.append([x, y, 3, [[0, 1], [1, 0], [0, -1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # right edge
            elif (x == self.size - 1 and y in range(1, self.size - 1) and self.cells[x][y][0] >= 3):
                # self.animate_edge(tag, -1, 0, 0, 1, 0, -1)
                self.blastList.append([x, y, 3, [[-1, 0], [0, 1], [0, -1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # upper edge
            elif y == 0 and x in range(1, self.size - 1) and self.cells[x][y][0] >= 3:
                # self.animate_edge(tag, -1, 0, 1, 0, 0, 1)
                self.blastList.append([x, y, 3, [[-1, 0], [1, 0], [0, 1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # lower edge
            elif (y == self.size - 1 and x in range(1, self.size - 1) and self.cells[x][y][0] >= 3):
                # self.animate_edge(tag, -1, 0, 1, 0, 0, -1)
                self.blastList.append([x, y, 3, [[-1, 0], [1, 0], [0, -1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # middle
            elif (x in range(1, self.size - 1) and y in range(1, self.size - 1) and self.cells[x][y][0] >= 4):
                # self.animate_middle(tag, -1, 0, 1, 0, 0, -1, 0, 1)
                self.blastList.append([x, y, 4, [[-1, 0], [1, 0], [0, -1], [0, 1]]])
                # play_sound()
                sound = threading.Thread(target=play_sound, args=())  # , daemon=True)
                sound.start()

            # else:
            #     print("Else condition")

        self.animate()
        self.adjustCell()
        # print("before: ", len(self.cord_list2))
        self.cord_list2 = self.cord_list2[1:]
        # print("after: ", len(self.cord_list2))
