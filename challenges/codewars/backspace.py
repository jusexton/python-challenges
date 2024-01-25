def clean_string(string: str) -> str:
    stack = []
    for character in string:
        if character == "#" and stack:
            stack.pop()
        elif character != "#":
            stack.append(character)

    return "".join(stack)
