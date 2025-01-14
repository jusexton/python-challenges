def find_Difference(numbers_one: list[int], numbers_two: list[int]) -> list[list[int]]:
    a = set(numbers_one)
    b = set(numbers_two)
    return [list(a.difference(b)), list(b.difference(a))]
