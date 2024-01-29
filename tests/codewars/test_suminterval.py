import pytest

from challenges.codewars import sumintervals


@pytest.mark.parametrize("expected,intervals", [(4, [(1, 5)]), (4, [(1, 5), (2, 3)])])
def test_should_return_correct_sum_of_intervals(expected, intervals):
    assert expected == sumintervals.sum_of_intervals(intervals)
