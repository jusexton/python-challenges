from typing import List, Dict


def killer(suspect_info: Dict[str, List[str]], dead: List[str]) -> str:
    is_killer = set(dead).issubset
    return next(person for person, seen in suspect_info.items() if is_killer(seen))
