import pytest

from challenges.other import stepcount


@pytest.mark.parametrize('stair_count, expected_step_count', [
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 7),
    (5, 13),
    (6, 24),
    (7, 44),
    # I have no idea if this is correct or not
    (100, 180396380815100901214157639)
])
def test_should_return_number_of_step_combinations_that_can_be_used_to_reach_the_top(
        stair_count: int, expected_step_count: int):
    assert stepcount.step_count(stair_count) == expected_step_count
