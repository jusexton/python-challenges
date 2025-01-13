def highest_altitude(gains: list[int]) -> int:
    curr_alt = 0
    highest = 0
    for gain in gains:
        curr_alt += gain
        highest = max(highest, curr_alt)
    return highest
