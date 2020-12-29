def shared_bits(a: int, b: int) -> bool:
    and_bits = a & b

    if and_bits == 0:
        return False

    power_of_two = (and_bits & (and_bits - 1)) == 0
    return not power_of_two
