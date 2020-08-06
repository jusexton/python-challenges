import pytest

from challenges.codewars import lastdigit


@pytest.mark.parametrize('expected,base,exponent', [
    (7,
     3715290469715693021198967285016729344580685479654510946723,
     68819615221552997273737174557165657483427362207517952651)
])
def test_last_of_large_produces_the_correct_last_digit_from_given_values(expected, base, exponent):
    assert expected == lastdigit.last_of_large(base, exponent)


@pytest.mark.parametrize('expected,values', [
    (1, []),
    (1, [0, 0]),
    (0, [0, 0, 0]),
    (1, [1, 2]),
    (1, [3, 4, 5]),
    (4, [4, 3, 6]),
    (1, [7, 6, 21]),
    (6, [12, 30, 21]),
    (4, [2, 2, 2, 0]),
    (0, [937640, 767456, 981242]),
    (6, [123232, 694022, 140249]),
    (6, [499942, 898102, 846073])
])
def test_last_of_huge_produces_the_correct_last_digit_from_given_values(expected, values):
    assert expected == lastdigit.last_of_huge(values)
