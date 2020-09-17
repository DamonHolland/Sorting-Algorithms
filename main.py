from graphics import *
from Data import Data
import Bogosort

def main():
    # Window Settings
    width = 640
    height = 640

    #Sorting Settings - Delay in ms
    data_size = 5
    swap_delay = 10
    compare_delay = 50

    window = GraphWin("Algorithms", width, height)
    window.setBackground('black')

    data = Data(data_size, window, swap_delay, compare_delay)

    Bogosort.sort(data)

    while window.isOpen():
        window.getMouse()


main()