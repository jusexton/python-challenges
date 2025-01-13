def find_max_average(numbers: list[int], k: int) -> float:
    curr_sum = max_sum = sum(numbers[:k])
    for i in range(k, len(numbers)):
        curr_sum += numbers[i] - numbers[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k
