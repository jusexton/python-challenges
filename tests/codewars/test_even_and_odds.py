import pytest

from challenges.codewars import even_and_odds


@pytest.mark.parametrize("expected,number", [("-10", -2), ("0", 0), ("110", 6)])
def test_correct_binary_representation_is_returned_when_number_is_even(
    expected: str, number: int
):
    assert even_and_odds.evens_and_odds(number) == expected


@pytest.mark.parametrize(
    "expected,number", [("-5", -5), ("1", 1), ("5", 5), ("d", 13), ("4d3", 1235)]
)
def test_correct_hex_representation_is_returned_when_number_is_odd(
    expected: str, number: int
):
    assert even_and_odds.evens_and_odds(number) == expected
