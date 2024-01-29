import pytest

from challenges.codewars import towels


@pytest.mark.parametrize(
    "towel_pile,used,expected",
    [
        (
            ["blue", "red", "blue", "red", "blue"],
            [3],
            ["blue", "red", "red", "blue", "blue"],
        ),
        (
            ["blue", "red", "blue", "red", "blue"],
            [2, 1, 4, 2],
            ["blue", "red", "red", "blue", "blue"],
        ),
    ],
)
def test_towel_pile_should_be_correctly_produced_given_starting_pile_and_usage(
    towel_pile: list[str], used: list[int], expected: list[str]
):
    assert towels.sort_the_pile(towel_pile, used) == expected
