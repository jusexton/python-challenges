from collections import defaultdict
from typing import List


def loneliest(string: str) -> List[str]:
    count = 0
    space_dict = defaultdict(int)
    last_character = None
    for character in string.strip():
        if character == " ":
            count += 1
        else:
            space_dict[character] = count

            if last_character:
                space_dict[last_character] = space_dict[last_character] + count

            last_character = character
            count = 0

    highest = max(space_dict.values())
    return [
        character
        for character, space_count in space_dict.items()
        if space_count == highest
    ]
