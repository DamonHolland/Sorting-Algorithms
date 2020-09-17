def sort(data):
    organize(data, 0, data.size - 1)

def organize(data, leftmost, rightmost):
    current_found = leftmost
    for i in range(leftmost, rightmost + 1):
        if data.compare(i, rightmost):
            data.swap(i, current_found)
            current_found += 1
    data.swap(current_found, rightmost)
    pivot = current_found

    if pivot - 1 > leftmost:
        organize(data, leftmost, pivot - 1)
    if pivot + 1 < rightmost:
        organize(data, pivot + 1, rightmost)
    return pivot