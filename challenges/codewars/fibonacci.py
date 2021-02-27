def fibonacci(n: int) -> list[int]:
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result
