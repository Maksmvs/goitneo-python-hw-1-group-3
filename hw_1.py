from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_by_day = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            birthday_day = today + timedelta(days=delta_days)
            birthdays_by_day[birthday_day.strftime("%A")].append(name)

    for day, users in birthdays_by_day.items():
        print(f"{day}: {', '.join(users)}")


if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
        {"name": "Jill Valentine", "birthday": datetime(1985, 11, 30)},
        {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)}
    ]

    get_birthdays_per_week(users)