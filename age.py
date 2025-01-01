from datetime import date
from datetime import timedelta


def ageCalculator():
    user_date = input(
        "Please enter a date in the following formate yyyy-mm-dd ")
    converted_date = date.fromisoformat(user_date)
    t_delta = date.today() - converted_date

    years = t_delta.days // 365

    print(f"you are {years} years old!")


ageCalculator()
