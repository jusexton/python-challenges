from typing import List


# Both functions are two different challenges. Links are included

# https://www.codewars.com/kata/5511b2f550906349a70004e1
def last_of_large(base, exponent) -> int:
    return pow(base, exponent, 10)


# https://www.codewars.com/kata/5518a860a73e708c0a000027
def last_of_huge(values: List[int]) -> int:
    n = 1
    for x in reversed(values):
        if n >= 4:
            n = n % 4 + 4

        n = x ** n
    return n % 10

# NOTE: Runs fairly quick locally but timing out when submitting
# TODO: Make optimizations so that solution can be submitted and not timeout
# def last_digit(values: List[int]) -> int:
#     if len(values) == 0:
#         return 1
#
#     def simplify_exponents(v: List[int]) -> (int, int):
#         exponent = v[-1]
#         for value in values[-2:0:-1]:
#             exponent = value ** exponent
#
#         return v[0], exponent
#
#     a, b = simplify_exponents(values)
#     return pow(a, b, 10)
