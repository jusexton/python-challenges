def check(numbers: list[int]) -> bool:
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            count += 1

    if numbers[-1] > numbers[0]:
        count += 1

    return count <= 1
