def pivot_index(numbers: list[int]) -> int:
    left_sum, right_sum = 0, sum(numbers)
    for i in range(len(numbers)):
        right_sum -= numbers[i]
        if left_sum == right_sum:
            return i
        left_sum += numbers[i]
    return -1
