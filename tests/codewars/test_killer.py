import pytest

from challenges.codewars import killer


@pytest.mark.parametrize(
    "expected,suspect_info,dead",
    [
        (
            "James",
            {
                "James": ["Jacob", "Bill", "Lucas"],
                "Johnny": ["David", "Kyle", "Lucas"],
                "Peter": ["Lucy", "Kyle"],
            },
            ["Bill", "Lucas"],
        )
    ],
)
def test_should_return_who_saw_both_dead(expected, suspect_info, dead):
    assert expected == killer.killer(suspect_info, dead)
