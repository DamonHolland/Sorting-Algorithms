def sort(data):
    buckets = []
    for i in range(data.size):
        buckets.append([])
    for i in range(data.size):
        buckets[data.get_value(i) - 1].append(data.get_value(i) - 1)

    for i in range(len(buckets)):
        if len(buckets[i]) > 0:
            insertion_sort(buckets[i])
        for j in range(len(buckets[i])):
            data.override(i, buckets[i][j] + 1)

def insertion_sort(array):
    sorted_size = 1
    while sorted_size < len(array):
        current_element = sorted_size
        while current_element - 1 >= 0 and array[current_element] < array[current_element - 1]:
            temp = array[current_element]
            array[current_element] = array[current_element - 1]
            array[current_element - 1] = temp
            current_element -= 1
        sorted_size += 1