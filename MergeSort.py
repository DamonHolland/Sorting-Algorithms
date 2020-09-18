def sort(data):
    merge_sort(data, 0, data.size - 1)

def merge_sort(data, low, high):
    if high > low:
        mid = low + ((high - low) // 2)

        # Break into two sides
        left = merge_sort(data, low, mid)
        right = merge_sort(data, mid + 1, high)

        new_values = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                new_values.append(left[0])
                left.pop(0)
            else:
                new_values.append(right[0])
                right.pop(0)
        while len(left) > 0:
            new_values.append(left[0])
            left.pop(0)
        while len(right) > 0:
            new_values.append(right[0])
            right.pop(0)
        for i in range(len(new_values)):
            data.override(low + i, new_values[i])
    else:
        new_values = [data.data[low][0]]

    return new_values