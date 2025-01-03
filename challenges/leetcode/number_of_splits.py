def ways_to_split_array(numbers: list[int]) -> int:
    ps = [numbers[0]]
    for number in numbers[1:]:
        ps.append(ps[-1] + number)

    n = len(numbers)
    count = 0
    for i in range(n - 1):
        if ps[i] >= ps[n - 1] - ps[i]:
            count += 1
    return count
