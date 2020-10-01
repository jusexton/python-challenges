import re


def domain_name(url: str) -> str:
    result = re.search(r'(https?://)?(www\.)?(?P<domain>[\w-]+)\.', url)
    return result.group('domain') if result else None
