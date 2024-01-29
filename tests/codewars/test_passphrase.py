import pytest

from challenges.codewars import passphrase


@pytest.mark.parametrize(
    "expected,string,offset",
    [
        ("!!!vPz fWpM J", "I LOVE YOU!!!", 1),
        (
            "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO",
            "MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015",
            2,
        ),
    ],
)
def test_should_return_correct_passphrase_from_given_string(expected, string, offset):
    assert expected == passphrase.convert(string, offset)
