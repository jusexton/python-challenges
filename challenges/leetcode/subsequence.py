def is_subsequence(s: str, t: str) -> bool:
    s_ptr, t_ptr = 0, 0
    while s_ptr < len(s) and t_ptr < len(t):
        if t[t_ptr] == s[s_ptr]:
            s_ptr += 1
        t_ptr += 1
    return s_ptr == len(s)
