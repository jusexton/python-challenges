import pytest

from challenges.leetcode.minimum_penalty import minimum_penalty


@pytest.mark.parametrize("expected,customers", [(2, "YYNY"), (0, "NNNNN"), (4, "YYYY")])
def test_minimum_penalty(expected: int, customers: str):
    actual = minimum_penalty(customers)
    assert actual == expected
