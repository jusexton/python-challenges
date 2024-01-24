def dominant_index(numbers: list[int]) -> int:
    a, b = sorted(numbers)[-2:]
    return numbers.index(b) if b >= a * 2 else -1
