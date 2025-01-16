def remove_stars(s: str) -> str:
    buf = []
    for c in s:
        if c == "*":
            buf.pop()
        else:
            buf.append(c)
    return "".join(buf)
