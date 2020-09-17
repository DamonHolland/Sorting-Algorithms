def sort(data):
    sorted_size = 0
    while sorted_size < data.size - 1:
        for i in range(data.size - sorted_size - 1):
            if data.compare(i + 1, i):
                data.swap(i + 1, i)
        sorted_size += 1
