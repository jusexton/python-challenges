def string_matching(words: list[str]) -> list[str]:
    n = len(words)
    result = []
    for i in range(n):
        word = words[i]
        for j in range(n): 
            if i == j:
                continue
            if word in words[j]:
                result.append(word)
                break
    return result
