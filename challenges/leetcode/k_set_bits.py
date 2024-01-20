def k_set_bits(numbers: list[int], k: int) -> int:
    return sum(
        number
        for index, number in enumerate(numbers)
        if index.bit_count() == k
    )
