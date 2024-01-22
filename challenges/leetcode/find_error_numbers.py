def find_error_numbers(numbers: list[int]) -> list[int]:
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(set(numbers))
    miss = expected_sum - actual_sum
    duplicate = sum(numbers) + miss - expected_sum
    return [duplicate, miss]
