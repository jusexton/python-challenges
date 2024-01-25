from collections import Counter


def character_freq(value: str) -> str:
    value = value.replace(" ", "").lower()
    counter = Counter(value)
    return ",".join(f'{key}:{"*" * value}' for key, value in counter.items())
