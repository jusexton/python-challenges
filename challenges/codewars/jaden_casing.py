def to_jaden_case(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split(" "))
