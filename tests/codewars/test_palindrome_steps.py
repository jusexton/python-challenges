import pytest

from challenges.codewars import palindrome_steps


@pytest.mark.parametrize(
    "expected,number",
    [
        (0, 131),
        (4, 87),
        (24, 89),
        (1, 10),
    ],
)
def test_correct_number_of_steps_is_return_to_achieve_palindrome(
    expected: int, number: int
):
    assert expected == palindrome_steps.palindrome_chain_length(number)
