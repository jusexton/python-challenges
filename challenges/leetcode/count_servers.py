def count_servers(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    row_counts = [0] * m
    col_counts = [0] * n
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                row_counts[row] += 1
                col_counts[col] += 1

    result = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1 and (row_counts[row] > 1 or col_counts[col] > 1):
                result += 1

    return result
