def nb_year(p0, percent, aug, p) -> int:
    percent = percent / 100
    count = 0
    while p0 < p:
        count += 1
        p0 = p0 + (p0 * percent) + aug

    return count
