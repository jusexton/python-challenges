from typing import Dict


def hex_string_to_rgd(hex_str: str) -> Dict[str, int]:
    return {
        'r': int(hex_str[1:3], 16),
        'g': int(hex_str[3:5], 16),
        'b': int(hex_str[5:7], 16)
    }
