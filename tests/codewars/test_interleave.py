import pytest

from challenges.codewars import interleave


@pytest.mark.parametrize('expected,args', [
    ([], [[]]),
    ([1, 2, 3], [[1, 2, 3]]),
    ([1, 2], [[1], [2]]),
    ([1, 2, 3], [[1], [2], [3]]),
    ([1, "c", 2, "d", 3, "e"], [[1, 2, 3], ["c", "d", "e"]]),
    ([1, 2, 3, 4, None, None], [[1, 4], [2], [3]])
])
def test_should_return_values_from_each_arg_correctly_interleaved(expected, args):
    assert expected == interleave.interleave_lists(*args)
    assert expected == interleave.interleave_lists_optimized(*args)
