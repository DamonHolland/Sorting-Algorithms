from graphics import *
from Data import Data
import Bogosort
import SelectionSort
import BubbleSort
import InsertionSort
import HeapSort
import QuickSort
import MergeSort
import BucketSort

def run():
    alg_options = {1: BubbleSort, 2: SelectionSort, 3: InsertionSort, 4: HeapSort, 5: QuickSort,
                   6: MergeSort, 7: BucketSort, 8: Bogosort}



    timer = time.time()

    print("---------- Select an algorithm ----------")
    [print(f"{alg_op}: {alg_name.__name__}") for alg_op, alg_name in alg_options.items()]
    selection = int(input("Selection: "))
    algorithm = alg_options[selection] if selection in alg_options else Bogosort

    window = GraphWin("Sorting Algorithms", 1024, 1024)
    window.setBackground('black')
    data = Data(32, window, 50, 50, 50, 0)

    algorithm.sort(data)
    print(algorithm.__name__ + " sorted data in " + str(time.time() - timer) + " seconds.")

if __name__ == "__main__":
    run()
