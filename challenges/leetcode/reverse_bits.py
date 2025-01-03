def reverse_bits(self, n: int) -> int:
    if n == 0:
        return 0

    result = 0
    for _ in range(32):
        result <<= 1
        if n & 1 == 1:
            result += 1
        n >>= 1
    return result
