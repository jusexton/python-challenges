import pytest
from challenges.leetcode.reverse_polish_notation import reverse_polish_notation


@pytest.mark.parametrize(
    "expected,tokens",
    [
        (9, ["2", "1", "+", "3", "*"]),
        (6, ["4", "13", "5", "/", "+"]),
        (22, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
    ],
)
def test_reverse_polish_notation(expected: int, tokens: list[str]):
    actual = reverse_polish_notation(tokens)
    assert actual == expected
