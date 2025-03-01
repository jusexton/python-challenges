def apply_operations(numbers: list[int]) -> list[int]:
    n = len(numbers)
    for i in range(1, n):
        if numbers[i - 1] == numbers[i]:
            numbers[i - 1] *= 2
            numbers[i] = 0

    i = 0
    for number in numbers:
        if number != 0:
            numbers[i] = number
            i += 1
    while i < n:
        numbers[i] = 0
        i += 1

    return numbers


print(apply_operations([1, 2, 2, 1, 1, 0]))
