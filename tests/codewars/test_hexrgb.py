from typing import Dict

import pytest

from challenges.codewars import hexrgb


@pytest.mark.parametrize(
    "hex_str,expected",
    [("#FF9933", {"r": 255, "g": 153, "b": 51}), ("#000000", {"r": 0, "g": 0, "b": 0})],
)
def test_rgb_values_are_correctly_extracted_from_hex_string(
    hex_str: str, expected: Dict[str, int]
):
    assert hexrgb.hex_string_to_rgd(hex_str) == expected
