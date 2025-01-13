def product_except_self(numbers: list[int]) -> list[int]:
    n = len(numbers)
    result = [1] * n

    prefix_product = 1
    for i in range(n):
        result[i] *= prefix_product
        prefix_product *= numbers[i]

    suffix_product = 1
    for i in reversed(range(n)):
        result[i] *= suffix_product
        suffix_product *= numbers[i]

    return result
