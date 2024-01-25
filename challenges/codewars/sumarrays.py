def sum_arrays(array_one, array_two):
    # Need this special check because unlike other cases, if both array
    # are empty the result is also empty
    if not array_one and not array_two:
        return []

    def array_to_int(array) -> int:
        return int("".join(map(str, array))) if array else 0

    int_one = array_to_int(array_one)
    int_two = array_to_int(array_two)
    summation = int_one + int_two
    digits = list(map(int, str(abs(summation))))
    if summation < 0:
        digits[0] = -digits[0]
    return digits
