import pytest
from challenges.leetcode import pascal_triangle


@pytest.mark.parametrize(
    "expected,row_count",
    [
        ([[1]], 1),
        ([[1], [1, 1]], 2),
        ([[1], [1, 1], [1, 2, 1]], 3),
        ([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]], 4),
        ([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], 5),
    ],
)
def test_pascal_triangle(expected: list[list[int]], row_count: int):
    actual = pascal_triangle.generate(row_count)
    assert actual == expected
