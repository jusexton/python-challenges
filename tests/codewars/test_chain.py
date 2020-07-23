import pytest

from challenges.codewars import chain


@pytest.mark.parametrize('expected,actual', [
    (0, chain.add(0)),
    (5, chain.add(2)(3)),
    (25, chain.add(2)(3)(20))
])
def test_should_correctly_chain_and_add_given_values(expected, actual):
    assert expected == actual
