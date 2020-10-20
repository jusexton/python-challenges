from typing import List

import pytest

from challenges.codewars import cuttheropes


@pytest.mark.parametrize('expected,items', [
    ([5, 4, 2, 1], [3, 3, 2, 9, 7]),
    ([10, 9, 6, 5, 3, 1], [13035, 6618, 13056, 20912, 1119, 13035, 6618, 6618, 8482, 13056])
])
def test_cut_the_ropes_correctly_reduces_ropes_and_returns_correct_list(expected: List[int], items: List[int]):
    assert expected == cuttheropes.cut_the_ropes(items)
