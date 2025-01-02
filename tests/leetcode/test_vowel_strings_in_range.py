from challenges.leetcode.vowel_strings_in_range import vowel_strings


def test_correct_count_of_strings_is_contained_within_given_ranges():
    assert [2, 3, 0] == vowel_strings(
        ["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]
    )
