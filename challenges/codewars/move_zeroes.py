def move_zeroes(arr: list) -> list:
    new_arr = []
    zero_count = 0
    for item in arr:
        if not isinstance(item, bool) and item == 0:
            zero_count += 1
            continue

        new_arr.append(item)

    return new_arr + ([0] * zero_count)
