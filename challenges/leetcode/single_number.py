def single_number(self, numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total ^= number
    return total
 