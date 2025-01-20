def first_complete_index(arr: list[int], matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    coords = {}
    for i in range(m):
        for j in range(n):
            val = matrix[i][j]
            coords[val] = (i, j)

    rows = [0] * m
    cols = [0] * n
    for index, number in enumerate(arr):
        row, col = coords[number]

        rows[row] += 1
        if rows[row] == n:
            return index
        cols[col] += 1
        if cols[col] == m:
            return index

    return -1
