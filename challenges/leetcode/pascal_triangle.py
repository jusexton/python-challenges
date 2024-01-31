def generate(num_rows: int) -> list[list[int]]:
    a, b = [1], [1, 1]
    result = []
    for _ in range(0, num_rows):
        result.append(a)
        a, b = b, _next_row(b)
    return result


def _next_row(b: list[int]) -> list[int]:
    result = [1] * (len(b) + 1)
    for i in range(1, len(b)):
        result[i] = b[i - 1] + b[i]
    return result
