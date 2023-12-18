'''Main entrypoint'''
from utils import constants, functions

def main():
    """Runs through the core logic of the Birthday Paradox simulator"""
    amount = input(f'How many birthdays shall I generate? (Max {constants.MAX_BIRTHDAYS}): ')

    while amount.isdigit() is False or int(amount) <= 0 or int(amount) > 100:
        amount = input(f'Please input a number from 1 to {constants.MAX_BIRTHDAYS}: ')

    amount = int(amount)
    birthday_list = functions.generate_birthdays(amount)

    print(f'Here are {amount} birthdays:')
    print(*functions.format_birthdays(birthday_list), sep=", ")
    bd_check = functions.check_birthdays(birthday_list)

    if bd_check:
        print(f"In this simulation, multiple people have a birthday on {functions.format_birthdays(bd_check)}")
    else:
        print("There are no matching birthdays in this simulation")

    print(f"Generating {amount} random birthdays {constants.MAX_BIRTHDAYS} times.")
    input("Press Enter to begin...")
    sims = functions.simulate_birthdays(constants.SIMULATIONS, amount)

    if sims[0] != 0:
        print(f'Out of {constants.SIMULATIONS:,} simulations of {amount} people, there was at least one matching birthday in that group {sims[0]:,} times. This means that {amount} people have a {sims[1]:.2%} chance of having a matching birthday in their group.')

if __name__ == "__main__":
    main()
