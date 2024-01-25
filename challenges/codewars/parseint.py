import re

WORD_DICT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

MULTIPLE_WORD_DICT = {"hundred": 100, "thousand": 1000, "million": 1000000}


def parse_int(number: str) -> int:
    parsed_number = 0
    words = re.split(r"\s|-", number)
    for word in words:
        if word in WORD_DICT:
            parsed_number += WORD_DICT[word]

        if word in MULTIPLE_WORD_DICT:
            number_value = MULTIPLE_WORD_DICT[word]
            # Make sure to subtract the previously parsed and added number
            parsed_number += number_value * (parsed_number % number_value) - (
                parsed_number % number_value
            )

    return parsed_number
