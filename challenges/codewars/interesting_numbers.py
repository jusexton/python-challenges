from typing import List


def is_interesting(number: int, awesome_phrases: List[int]) -> int:
    def is_at_least_three_len(n: str) -> bool:
        return len(n) >= 3

    def all_same_characters(string: str, expected=None) -> bool:
        character = string[0]
        is_expected_character = True if expected is None else string[0] == expected
        return string == len(string) * character and is_expected_character

    def is_digit_followed_by_zeroes(n: str) -> bool:
        return n[0] != '0' and all_same_characters(n[1:], expected='0')

    def all_same(n: str) -> bool:
        return all_same_characters(n)

    def is_palindrome(n: str) -> bool:
        return n[::-1] == n

    def is_sequential_incrementing(n: str) -> bool:
        return n in '1234567890'

    def is_sequential_decrementing(n: str) -> bool:
        return n in '9876543210'

    def is_awesome_phrase(n: str) -> bool:
        return int(n) in awesome_phrases

    interesting_criteria = {
        'is_digit_followed_by_zeroes': is_digit_followed_by_zeroes,
        'all_same': all_same,
        'is_palindrome': is_palindrome,
        'is_sequential_incrementing': is_sequential_incrementing,
        'is_sequential_decrementing': is_sequential_decrementing,
        'is_awesome_phrase': is_awesome_phrase
    }
    criteria = interesting_criteria.values()

    number_as_string = str(number)
    if is_at_least_three_len(number_as_string):
        for criterion in criteria:
            interesting = criterion(number_as_string)
            if interesting is True:
                return 2

    look_ahead = [str(number + 1), str(number + 2)]
    for name, criterion in interesting_criteria.items():
        for ahead in look_ahead:
            if not is_at_least_three_len(ahead):
                continue
            almost_interesting = criterion(ahead)
            if almost_interesting:
                return 1

    return 0
