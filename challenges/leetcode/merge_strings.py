def merge_alternately(word_one: str, word_two: str) -> str:
    count = min(len(word_one), len(word_two))
    res = []
    for i in range(count):
        res.append(word_one[i])
        res.append(word_two[i])

    if len(word_one) > count:
        res.append(word_one[count:])
    elif len(word_two) > count:
        res.append(word_two[count:])
    return "".join(res)
