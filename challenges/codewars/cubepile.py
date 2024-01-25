def find_nb(m: int) -> int:
    n = 1
    m -= 1
    while m > 0:
        n += 1
        m -= n**3

    if m != 0:
        return -1

    return n
