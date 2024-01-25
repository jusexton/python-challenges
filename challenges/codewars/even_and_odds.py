def evens_and_odds(number: int) -> str:
    return f"{number:b}" if number % 2 == 0 else f"{number:x}"
