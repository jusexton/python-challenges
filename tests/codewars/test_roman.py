import pytest

from challenges.codewars import roman


class TestFromRoman:
    @pytest.mark.parametrize(
        "expected,roman_string",
        [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (6, "VI"),
            (1776, "MDCCLXXVI"),
            (2014, "MMXIV"),
        ],
    )
    def test_should_correctly_convert_roman_string_to_int(self, expected, roman_string):
        assert expected == roman.from_roman(roman_string)

    @pytest.mark.parametrize("invalid_roman_string", ["abc", "not valid"])
    def test_should_raise_value_error_when_roman_string_is_invalid(
        self, invalid_roman_string
    ):
        with pytest.raises(ValueError):
            roman.from_roman(invalid_roman_string)


class TestToRoman:
    @pytest.mark.parametrize(
        "expected,int_value", [("I", 1), ("V", 5), ("MCMLXXXIX", 1989)]
    )
    def test_should_correctly_convert_roman_string_to_int(self, expected, int_value):
        assert expected == roman.to_roman(int_value)

    @pytest.mark.parametrize(
        "int_value",
        [
            0 - 1,
            -100,
        ],
    )
    def test_should_raise_value_error_when_int_value_is_less_than_one(self, int_value):
        with pytest.raises(ValueError):
            roman.to_roman(int_value)
