from collections import Counter


def equal_pairs(grid: list[list[int]]) -> int:
    row_counts = Counter(tuple(row) for row in grid)
    res = 0
    n = len(grid)
    for i in range(n):
        col = tuple(grid[j][i] for j in range(n))
        res += row_counts.get(col, 0)
    return res
