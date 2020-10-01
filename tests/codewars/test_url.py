import pytest

from challenges.codewars import url


@pytest.mark.parametrize("url_str,domain", [
    ('http://google.com', 'google'),
    ('http://google.co.jp', 'google'),
    ('www.xakep.ru', 'xakep')
])
def test_domain_name_correctly_extracts_domain_names_from_url(url_str, domain):
    assert url.domain_name(url_str) == domain
