def search(sorted_array: list[int], value: int) -> int:
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2

        item = sorted_array[mid]
        if item < value:
            low = mid + 1
        elif item > value:
            high = mid - 1
        else:
            return mid

    return -1
