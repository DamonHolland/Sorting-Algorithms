import random
from graphics import *


class Data:
    def __init__(self, size, window, swap_delay, compare_delay, override_delay, access_delay):
        self.window = window
        self.data = []
        self.swap_delay = swap_delay
        self.compare_delay = compare_delay
        self.override_delay = override_delay
        self.access_delay = access_delay
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
        self.shuffle(skip_delay=True)
        self.draw_data()

    def shuffle(self, skip_delay=False):
        n = len(self.data) - 1
        while n > 0:
            rand = random.randint(0, n - 1)
            self.swap(n, rand, skip_delay)
            n = n - 1

    def swap(self, n, m, skip_delay=False):
        # Swap Data
        temp = self.data[m]
        self.data[m] = self.data[n]
        self.data[n] = temp
        swap_dx = self.data[m][1].getP1().x - self.data[n][1].getP1().x
        num_transitions = 10
        self.data[n][1].setFill('blue')
        self.data[m][1].setFill('blue')
        for i in range(num_transitions):
            self.data[n][1].move(swap_dx / num_transitions, 0)
            self.data[m][1].move(-swap_dx / num_transitions, 0)
            if not skip_delay:
                time.sleep(self.swap_delay / 1000.0 / num_transitions)
        self.data[n][1].setFill('white')
        self.data[m][1].setFill('white')

    def override(self, i, new_value):
        self.data[i][1].setFill('red')
        time.sleep(self.override_delay / 1000.0)
        self.data[i][1].undraw()
        bl_x = i * (self.window.getWidth() / self.size)
        bl_y = self.window.getHeight()
        tr_x = (i + 1) * (self.window.getWidth() / self.size)
        tr_y = self.window.getHeight() - (new_value * (self.window.getWidth() / self.size))
        rect = Rectangle(Point(bl_x, bl_y), Point(tr_x, tr_y))
        rect.setFill('white')
        self.data[i] = ([new_value + 1, rect])
        self.data[i][1].draw(self.window)

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

    def get_value(self, i):
        self.data[i][1].setFill('purple')
        time.sleep(self.access_delay / 1000.0)
        self.data[i][1].setFill('white')
        return self.data[i][0]

    def draw_data(self):
        for i in range(len(self.data)):
            self.data[i][1].draw(self.window)
