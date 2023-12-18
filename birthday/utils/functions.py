"""Basic functions"""
import datetime
import random

from .constants import START

def generate_birthdays(amount: int):
    """Returns a randomly generated list of (amount) birthdays.

    Args:
        amount (int): The number of birthdays to generate
    """
    birthdays = [START + datetime.timedelta(days=random.randint(1,364)) for i in range(amount)]
    return birthdays

def check_birthdays(birthdays: list) -> datetime.date or None:
    """Checks a list of birthdays to see if two or more members of the sample are the same.

    Args:
        birthdays (list): The list of birthdays to be checked.

    Returns:
        datetime.date or bool: Date of the first matching birthday; False otherwise.
    """

    if len(birthdays) == set(birthdays):
        return None

    for i, bd in enumerate(birthdays):
        if bd in birthdays[i+1:]:
            return bd

def simulate_birthdays(sims: int, people: int) -> tuple:
    """Runs (sims) simulations and returns the number of sets where two or more people share a birthday and the percentage of matches.

    Args:
        sims (int): The number of simulations to run
        people (int): The number of birthdays to test

    Returns:
        tuple: The total number of simulations with one or more matches and the percentage of sims where there was a match.
    """

    matches = 0

    for i in range(sims):
        if i >= 10_000 and i % 10_000 == 0:
            print(f'{i} simulations run...')

        birthdays = generate_birthdays(people)

        if check_birthdays(birthdays):
            matches += 1

    if matches > 0:
        return (matches, matches/sims)

    return (0,0)

def format_birthdays(birthdays: list or datetime.date):
    """Formats raw birthday date objects into strings. Accepts single dates and lists of dates.

    Args:
        birthdays (list): Raw list of birthday date objects.

    Returns:
        list: The list of birthdays as formatted strings.
    """
    if isinstance(birthdays, list):
        formatted = [x.strftime('%b %d') for x in birthdays]
        return formatted

    return birthdays.strftime('%b %d')
