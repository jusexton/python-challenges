from typing import List


def valid(golf_schedule: List[List[str]]) -> bool:
    """
    :return: Whether the given golf schedule was valid
    """
    player_schedule = dict()
    day_length = len(golf_schedule[0])
    group_size = len(golf_schedule[0][0])
    players = {g for p in golf_schedule[0] for g in p}
    for day in golf_schedule:
        if len(day) != day_length:
            return False

        for group in day:
            if len(group) != group_size:
                return False

            for player in group:
                if player not in players:
                    return False

                if player not in player_schedule:
                    player_schedule[player] = set(group)
                else:
                    # Fun fact, & is overloaded to use the intersection method for sets
                    if len(player_schedule[player] & set(group)) > 1:
                        return False
                    else:
                        player_schedule[player].add(group)

    return True
