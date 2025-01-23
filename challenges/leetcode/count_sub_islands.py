from typing import Tuple


def next_cells(row: int, col: int, grid: list[list[int]]) -> list[Tuple[int, int]]:
    m, n = len(grid), len(grid[0])
    cells = []
    if col + 1 < n and grid[row][col + 1] == 1:
        cells.append((row, col + 1))
    if col - 1 >= 0 and grid[row][col - 1] == 1:
        cells.append((row, col - 1))
    if row - 1 >= 0 and grid[row - 1][col] == 1:
        cells.append((row - 1, col))
    if row + 1 < m and grid[row + 1][col] == 1:
        cells.append((row + 1, col))
    return cells


def count_sub_islands(grid_one: list[list[int]], grid_two: list[list[int]]) -> int:
    m, n = len(grid_one), len(grid_one[0])

    result = 0
    for row in range(m):
        for col in range(n):
            if grid_two[row][col] == 1:
                valid = 1
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    grid_two[r][c] = 0
                    valid &= grid_one[r][c]
                    stack.extend(next_cells(r, c, grid_two))

                result += valid

    return result
