import datetime


def day_of_the_week(day: int, month: int, year: int) -> str:
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    index = datetime.date(year, month, day).weekday()
    return weekdays[index]
