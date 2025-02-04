def is_array_special(numbers: list[int]) -> bool:
    for i in range(1, len(numbers)):
        if (numbers[i - 1] + numbers[i]) % 2 == 0:
            return False
    return True
