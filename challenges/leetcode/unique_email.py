from typing import List
import re


def unique_email_count(emails: List[str]) -> int:
    return len(set(normalize_email(email) for email in emails))


def normalize_email(email: str) -> str:
    local_name, domain_name = email.split('@')
    local_name = re.sub(r'\.|\+.+', '', local_name)
    return f'{local_name}@{domain_name}'
