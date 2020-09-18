def sort(data):
    b_is_sorted = False

    while not b_is_sorted:
        b_is_sorted = True
        for i in range(data.size - 1):
            if b_is_sorted and not data.compare(i, i + 1):
                b_is_sorted = False
        if not b_is_sorted:
            data.shuffle()