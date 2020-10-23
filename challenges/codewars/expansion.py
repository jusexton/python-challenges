from collections import deque


def expand(expression: str) -> str:
    characters = deque()
    for character in expression[::-1]:
        if character.isdigit():
            expanded = int(character) * characters
            characters = deque(expanded)
        elif character.isalpha():
            characters.appendleft(character)

    return ''.join(characters)

# Regex solution. Very slow :(
# import re
# from re import Match
#
#
# def expand(expression: str) -> str:
#     while '(' in expression:
#         expression = re.sub(r'(?P<count>[1-9]+)\((?P<value>[a-z]+)\)', expander, expression)
#
#     return expression
#
#
# def expander(match: Match) -> str:
#     return int(match.group('count')) * match.group('value')
