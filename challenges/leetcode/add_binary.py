def add_binary(a: str, b: str) -> str:
    res = int(a, 2) + int(b, 2)
    return f"{res:b}"
