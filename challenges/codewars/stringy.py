import math


def stringy(size: int) -> str:
    return ("10" * math.ceil(size / 2))[:size]
