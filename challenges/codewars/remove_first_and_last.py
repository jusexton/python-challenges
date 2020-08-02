def remove_first_and_last(original: str) -> str:
    return '' if len(original) <= 2 else original[1:-1]
