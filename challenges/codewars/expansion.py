from collections import deque


def expand(expression: str) -> str:
    characters = deque()
    for character in expression[::-1]:
        if character.isdigit():
            expanded = int(character) * characters
            characters = deque(expanded)
        elif character.isalpha():
            characters.appendleft(character)

    return "".join(characters)


# import re
#
#
# def expand(expression: str) -> str:
#     regex = re.compile(r'(?P<count>[1-9]+)\((?P<value>[a-z]+)\)|\((?P<non_repeating_value>[a-z]+)\)')
#     while '(' in expression:
#         expression = regex.sub(expander, expression)
#
#     return expression
#
#
# def expander(match) -> str:
#     if match.group('non_repeating_value'):
#         return match.group('non_repeating_value')
#
#     return int(match.group('count')) * match.group('value')
