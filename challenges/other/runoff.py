from collections import Counter


class InstantRunoffBallot:
    def __init__(self, votes: list[str]):
        self.votes = votes
        self.__preference = 0

    def get_vote(self):
        return self.votes[self.__preference]

    def update_preference(self, eliminations: set[str]):
        for index, vote in enumerate(self.votes):
            if vote not in eliminations:
                self.__preference = index
                break


class InstantRunoffRound:
    def __init__(self, results: dict[str, int]):
        self.results = results
        self.winners = self.__calculate_winners()
        self.eliminations = self.__calculate_eliminations()

    def __calculate_winners(self) -> list[str]:
        total_votes = sum(self.results.values())

        for name, vote_count in self.results.items():
            if vote_count > total_votes / 2:
                return [name]

        is_tie = len(set(self.results.values())) == 1
        if is_tie:
            return list(self.results.keys())

        return []

    def __calculate_eliminations(self) -> list[str]:
        vote_count_min = min(vote_count for name, vote_count in self.results.items())
        eliminations = [name for name, vote_count in self.results.items() if vote_count == vote_count_min]
        return [] if len(eliminations) == len(self.results) else eliminations


def conduct_instant_runoff(ballot_votes: list[list[str]]) -> list[str]:
    ballots = [InstantRunoffBallot(votes) for votes in ballot_votes]
    eliminations = set()

    while True:
        runoff_round = conduct_round(ballots)
        if runoff_round.winners:
            return runoff_round.winners
        else:
            eliminations.update(runoff_round.eliminations)
            for ballot in ballots:
                ballot.update_preference(eliminations)


def conduct_round(ballots: list[InstantRunoffBallot]) -> InstantRunoffRound:
    results = Counter(ballot.get_vote() for ballot in ballots)
    return InstantRunoffRound(results)
