from collections import deque


def nearest_exit(maze: list[list[str]], entrance: list[int]) -> int:
    m, n = len(maze), len(maze[0])

    start = (entrance[0], entrance[1])
    queue = deque([start])
    moves = 1

    maze[entrance[0]][entrance[1]] = "+"
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while queue:
        neighbor_count = len(queue)
        for _ in range(neighbor_count):
            curr_row, curr_col = queue.popleft()

            for row_change, col_change in directions:
                new_row, new_col = curr_row + row_change, curr_col + col_change

                if (
                    new_row < 0
                    or new_row >= m
                    or new_col < 0
                    or new_col >= n
                    or maze[new_row][new_col] == "+"
                ):
                    continue

                if new_row == 0 or new_row == m - 1 or new_col == 0 or new_col == n - 1:
                    return moves

                queue.append((new_row, new_col))
                maze[new_row][new_col] = "+"

        moves += 1

    return -1
