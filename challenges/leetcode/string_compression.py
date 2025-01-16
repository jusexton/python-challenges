def compress(chars: list[str]) -> int:
    char_idx, res_idx = 0, 0
    while char_idx < len(chars):
        curr_char = chars[char_idx]
        count = 0
        while char_idx < len(chars) and chars[char_idx] == curr_char:
            char_idx += 1
            count += 1

        chars[res_idx] = curr_char
        res_idx += 1
        if count != 1:
            for digit in str(count):
                chars[res_idx] = digit
                res_idx += 1
    return res_idx
