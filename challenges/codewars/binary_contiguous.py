def bin_contiguous(array: list[int]) -> int:
    sum_to_index = {0: -1}
    summation = 0
    max_length = 0
    for index, bit in enumerate(array):
        summation += 1 if bit else -1
        if summation in sum_to_index:
            max_length = max(max_length, index - sum_to_index[summation])
        else:
            sum_to_index[summation] = index

    return max_length
