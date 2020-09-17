from graphics import *
from Data import Data
import Bogosort
import SelectionSort
import BubbleSort
import InsertionSort
import HeapSort
import QuickSort

def main():
    #Data Settings
    data_size = 100

    #Visual Settings - Delay in ms
    show_visuals = True
    window_width = 1280
    window_height = 1280
    swap_delay = 0
    compare_delay = 0
    access_delay = 0

    #Select Algorithm
    # 0 - Bogosort
    # 1 - Bubble Sort
    # 2 - Selection Sort
    # 3 - Insertion Sort
    # 4 - Heap Sort
    # 5 - Quick Sort
    # 6 - Merge Sort
    # 7 - Bucket Sort
    # 8 - Radix Sort
    algorithm_selection = 4

    if algorithm_selection == 1:
        algorithm = BubbleSort
    elif algorithm_selection == 2:
        algorithm = SelectionSort
    elif algorithm_selection == 3:
        algorithm = InsertionSort
    elif algorithm_selection == 4:
        algorithm = HeapSort
    elif algorithm_selection == 5:
        algorithm = QuickSort
    else:
        algorithm = Bogosort


    if show_visuals:
        window = GraphWin("Algorithms", window_width, window_height)
        window.setBackground('black')
    else:
        window = 0

    data = Data(data_size, window, swap_delay, compare_delay, access_delay, show_visuals)

    timer = time.time()

    algorithm.sort(data)

    print(algorithm.__name__ + " sorted data in " + str(time.time() - timer) + " seconds.")

    if window != 0:
        while window.isOpen():
            window.getMouse()


main()