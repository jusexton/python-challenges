from typing import List

import pytest

from challenges.leetcode import richest


@pytest.mark.parametrize('expected,accounts', [
    (3, [[1, 2], [1]]),
    (17, [[2, 8, 7], [7, 1, 3], [1, 9, 5]])
])
def test_returns_maximum_account_value(expected: int, accounts: List[List[int]]):
    assert richest.richest_customer(accounts) == expected
