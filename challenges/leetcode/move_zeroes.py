def move_zeroes(numbers: list[int]):
    zero_count = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            zero_count += 1
        elif zero_count > 0:
            numbers[i], numbers[i - zero_count] = 0, numbers[i]
