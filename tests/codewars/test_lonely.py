from typing import List

import pytest

from challenges.codewars import lonely


@pytest.mark.parametrize("expected,string", [
    (['g'], 'abc d   ef  g   h i j      '),
    (['a', 'b', 'c'], 'abc'),
    (['a', 'b'], ' a bc '),
    (['a', 'b', 'c', 'e'], ' a bc e      ')
])
def test_is_matching_correctly_identifies_strings_that_do_not_match_given_pattern(expected: List[str], string: str):
    assert lonely.loneliest(string) == expected
