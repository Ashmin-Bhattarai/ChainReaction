from winsound import *
import _thread
import sys


class Explode:
    def play_sound(self, filename):
        PlaySound(filename, SND_FILENAME)

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
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
        elif (
            x == self.size - 1
            and y in range(1, self.size - 1)
            and self.cells[x][y][0] >= 3
        ):
            self.animate_edge(tag, -1, 0, 0, 1, 0, -1)
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
            self.play_sound("soundeffects/explode.wav")
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
