from graphics import *
import random

def main():
    # Window Settings
    width = 640
    height = 640

    #Sorting Settings
    sorting_size = 64

    data = []
    for i in range(sorting_size):
        data.append(i + 1)
    shuffle(data)

    window = GraphWin("Algorithms", width, height)
    window.setBackground('black')

    draw_data(window, data)

    while window.isOpen():
        print("main loop running")

def draw_data(window, data):
    for i in range(len(data)):
        data_rect = Rectangle(Point(i * (window.getWidth() / len(data)), window.getHeight()),
                             Point((i + 1) * (window.getWidth() / len(data)),window.getHeight() -
                                  ((data[i]) * (window.getHeight() / len(data)))))
        data_rect.setFill('white')
        data_rect.draw(window)

def shuffle(data):
    n = len(data) - 1
    while n > 0:
        rand = random.randint(0, n - 1)
        temp = data[rand]
        data[rand] = data[n]
        data[n] = temp
        n = n-1


main()