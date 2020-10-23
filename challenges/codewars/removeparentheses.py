def remove_parentheses(string: str) -> str:
    result = []
    stack = []
    for character in string:
        if character == '(':
            stack.append('(')
        elif character == ')':
            stack.pop()
        elif len(stack) == 0:
            result.append(character)

    return ''.join(result)
