import re


def is_a_valid_message(message: str) -> bool:
    matches = re.finditer(r'(?P<count>[1-9][0-9]?)(?P<characters>[a-zA-Z]*)', message)
    return all(valid_match(match) for match in matches)


def valid_match(match) -> bool:
    match_count = match.group('count')
    match_characters = match.group('characters')
    return int(match_count) == len(match_characters)
