def count_bits(n: int) -> list[int]:
    return [i.bit_count() for i in range(0, n + 1)]
