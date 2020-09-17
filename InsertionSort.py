def sort(data):
    sorted_size = 1
    while sorted_size < data.size:
        current_element = sorted_size
        while current_element - 1 >= 0 and data.compare(current_element, current_element - 1):
            data.swap(current_element, current_element - 1)
            current_element -= 1
        sorted_size += 1