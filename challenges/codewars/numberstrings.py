import re


def solve(string: str) -> int:
    return max(map(int, re.findall(r"[\d]+", string)))
