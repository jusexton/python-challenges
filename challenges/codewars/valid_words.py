import re


def valid_word_count(s: str) -> int:
    return sum(
        bool(re.match(r"^[a-z]*([a-z]-[a-z])?[a-z]*[!.,]?$", token))
        for token in s.split(" ")
        if token != ""
    )
