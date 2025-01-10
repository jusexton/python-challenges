from collections import Counter


def word_subsets(words_one: list[str], words_two: list[str]) -> list[str]:
    count_acc = Counter()
    for word in words_two:
        char_counts = Counter(word)
        for c, count in char_counts.items():
            count_acc[c] = max(count, count_acc.get(c, 0))
    return [word for word in words_one if Counter(word) >= count_acc]
