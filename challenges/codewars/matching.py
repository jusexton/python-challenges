import re


def is_match(pattern: str, s: str) -> bool:
    return re.match(f'^{pattern.replace("*", ".*")}$', s) is not None
