import random
from graphics import *


class Data:
    def __init__(self, size, window, swap_delay, compare_delay):
        self.window = window
        self.data = []
        self.swap_delay = swap_delay
        self.compare_delay = compare_delay
        self.size = size
        for i in range(size):
            value = i + 1
            bl_x = i * (window.getWidth()/ size)
            bl_y = window.getHeight()
            tr_x = (i + 1) * (window.getWidth()/ size)
            tr_y = window.getHeight() - ((i + 1) * (window.getWidth()/ size))
            rect = Rectangle(Point(bl_x, bl_y), Point(tr_x, tr_y))
            rect.setFill('white')
            self.data.append([value, rect])
        self.draw_data()
        self.shuffle()

    def shuffle(self):
        n = len(self.data) - 1
        while n > 0:
            rand = random.randint(0, n - 1)
            self.swap(n, rand)
            n = n - 1

    def swap(self, n, m):
        # Swap Data
        temp = self.data[m]
        self.data[m] = self.data[n]
        self.data[n] = temp
        # Show Visual Change
        swap_dx = self.data[m][1].getP1().x - self.data[n][1].getP1().x
        self.data[n][1].move(swap_dx, 0)
        self.data[m][1].move(-swap_dx, 0)
        self.data[n][1].setFill('blue')
        self.data[m][1].setFill('blue')
        time.sleep(self.swap_delay / 1000.0)
        self.data[n][1].setFill('white')
        self.data[m][1].setFill('white')

    def compare(self, n, m):
        b_is_less = False
        if self.data[n][0] < self.data[m][0]:
            b_is_less = True
        # Show Visual Comparison
        self.data[n][1].setFill('green')
        self.data[m][1].setFill('green')
        time.sleep(self.compare_delay / 1000.0)
        self.data[n][1].setFill('white')
        self.data[m][1].setFill('white')
        return b_is_less

    def draw_data(self):
        for i in range(len(self.data)):
            self.data[i][1].draw(self.window)