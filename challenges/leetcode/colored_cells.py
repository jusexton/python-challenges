def colored_cells(n: int) -> int:
    return 1 if n == 1 else sum(i * 4 for i in range(n)) + 1
