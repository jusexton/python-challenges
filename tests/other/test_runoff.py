import pytest

from challenges.other import runoff


@pytest.mark.parametrize('votes, expected_winners', [
    ([
         ['Alice', 'Bob', 'Charlie'],
         ['Alice', 'Charlie', 'Bob'],
         ['Bob', 'Charlie', 'Alice'],
         ['Bob', 'Alice', 'Charlie'],
         ['Charlie', 'Alice', 'Bob']
     ],
     ['Alice']),
    ([
         ['Alice', 'Bob'],
         ['Bob', 'Alice'],
     ],
     ['Alice', 'Bob']
    )
])
def test_winners_are_correctly_determined(votes: list[list[str]], expected_winners: list[str]):
    assert runoff.conduct_instant_runoff(votes) == expected_winners
