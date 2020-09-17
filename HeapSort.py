def sort(data):
    sorted_size = 0
    for i in range(data.size // 2, -1, -1):
        organize_node(data, data.size, i)

    while sorted_size < data.size:
        data.swap(0, data.size - sorted_size - 1)
        sorted_size += 1
        organize_node(data, data.size - sorted_size, 0)

def organize_node(data, size, i):
    max_node = i
    left_child = (i * 2) + 1
    right_child = (i * 2) + 2

    if left_child < size and data.compare(max_node, left_child):
        max_node = left_child
    if right_child < size and data.compare(max_node, right_child):
        max_node = right_child

    if max_node != i:
        data.swap(i, max_node)
        organize_node(data, size, max_node)
