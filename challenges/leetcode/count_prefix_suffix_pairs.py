def count_prefix_suffix_pairs(self, words: list[str]) -> int:
    count = 0
    for i in range(0, len(words)):
        curr = words[i]
        for word in words[i + 1 :]:
            if word.startswith(curr) and word.endswith(curr):
                count += 1
    return count
