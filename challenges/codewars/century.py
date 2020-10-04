def get_century(year: str) -> str:
    century = (int(year) - 1) // 100 + 1
    return str(century) + ("th" if 4 <= century % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(century % 10, "th"))
