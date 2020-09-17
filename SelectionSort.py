def sort(data):
    sorted_size = 0
    while sorted_size < data.size - 1:
        current_min = data.get_value(sorted_size)
        min_index = sorted_size
        for i in range(sorted_size + 1, data.size):
            if data.compare(i, min_index):
                min_index = i
        data.swap(sorted_size, min_index)
        sorted_size += 1
