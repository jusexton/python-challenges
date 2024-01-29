import pytest

from challenges.codewars import tally


@pytest.mark.parametrize(
    "score,expected",
    [
        (3, "c"),
        (4, "d"),
        (5, "e <br>"),
        (10, "e <br>e <br>"),
        (28, "e <br>e <br>e <br>e <br>e <br>c"),
        (15, "e <br>e <br>e <br>"),
    ],
)
def test_score_is_converted_to_tally_representation(score: int, expected: str):
    assert tally.score_to_tally(score) == expected
