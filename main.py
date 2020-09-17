from graphics import *
from Data import Data
import Bogosort
import SelectionSort
import BubbleSort
import InsertionSort

def main():
    # Window Settings
    width = 1280
    height = 1280

    #Sorting Settings - Delay in ms
    data_size = 64
    swap_delay = 5
    compare_delay = 5
    access_delay = 5

    #Select Algorithm
    # 0 - Bogosort
    # 1 - Selection Sort
    # 2 - Bubble Sort
    # 3 - Insertion Sort
    # 4 - Heap Sort
    # 5 - Quick Sort
    # 6 - Merge Sort
    # 7 - Bucket Sort
    # 8 - Radix Sort
    algorithm_selection = 3

    if algorithm_selection == 1:
        algorithm = SelectionSort
    elif algorithm_selection == 2:
        algorithm = BubbleSort
    elif algorithm_selection == 3:
        algorithm = InsertionSort
    else:
        algorithm = Bogosort


    window = GraphWin("Algorithms", width, height)
    window.setBackground('black')

    data = Data(data_size, window, swap_delay, compare_delay, access_delay)

    algorithm.sort(data)

    while window.isOpen():
        window.getMouse()


main()