import pytest

from challenges.codewars import sumparts


@pytest.mark.parametrize(
    "expected,values",
    [
        ([20, 20, 19, 16, 10, 0], [0, 1, 3, 6, 10]),
        ([21, 20, 18, 15, 11, 6, 0], [1, 2, 3, 4, 5, 6]),
        (
            [
                10037855,
                9293730,
                9292795,
                9292388,
                9291934,
                9291504,
                9291414,
                9291270,
                2581057,
                2580168,
                2579358,
                0,
            ],
            [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358],
        ),
    ],
)
def test_should_return_the_sum_of_all_parts(expected, values):
    assert expected == sumparts.parts_sums(values)
