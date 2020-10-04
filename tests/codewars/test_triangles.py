import pytest

from challenges.codewars import triangles


@pytest.mark.parametrize('number', [
    3, 6, 10, 66
])
def test_is_triangle_number_correctly_identifies_triangle_numbers(number: int):
    assert triangles.is_triangle_number(number) is True
