import calendar
from datetime import date, timedelta
from typing import List


def most_frequent_days(year: int) -> List[str]:
    chosen_date = date(year, 1, 1)
    if calendar.isleap(year):
        favorites = sorted([chosen_date.weekday(), (chosen_date + timedelta(1)).weekday()])
        return list(map(lambda x: calendar.day_name[x], favorites))
    else:
        return [f'{chosen_date:%A}']

# def date_range(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)
#
#
# def most_frequent_days(year: int) -> List[str]:
#     start_date = date(year, 1, 1)
#     # Add an extra day to the end date because the range function is exclusive and
#     # would not actually iterate over the last day on the year
#     end_date = date(year, 12, 31) + timedelta(days=1)
#
#     counter = Counter(f'{d:%A}' for d in date_range(start_date, end_date))
#     max_count = max(counter.values())
#     return sorted([day for day, count in counter.items() if count == max_count])
