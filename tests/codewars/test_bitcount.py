import pytest

from challenges.codewars import bitcount


@pytest.mark.parametrize("expected,left,right", [(7, 5, 7), (51, 12, 29)])
def test_(expected: int, left: int, right: int):
    assert expected == bitcount.count_ones(left, right)
