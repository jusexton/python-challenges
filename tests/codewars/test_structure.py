import pytest

from challenges.codewars import structure


@pytest.mark.parametrize('expected,original,other', [
    (True, 1, 1),
    (True, [1, [1, 1]], [2, [2, 2]]),
    (False, [1, [1, 1]], [[2, 2], 2]),
    (True, [[[], []]], [[[], []]]),
    (False, [[[], []]], [[1, 1]]),
    (False, [1, [1, 1]], [[2], 2]),
    (False, [1], [2, [2, 2]]),
    (False, [1, [1, 1]], [2, [2]])
])
def test_should_correctly_whether_given_arrays_are_same_structure(expected, original, other):
    assert structure.same_structure_as(original, other) == expected
