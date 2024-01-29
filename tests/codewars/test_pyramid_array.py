import pytest

from challenges.codewars import pyramid_array


@pytest.mark.parametrize("expected,n", [([], 0), ([[1]], 1), ([[1], [1, 1]], 2)])
def test_should_return_arrays_that_form_a_pyramid(expected, n):
    assert pyramid_array.pyramid(n) == expected
