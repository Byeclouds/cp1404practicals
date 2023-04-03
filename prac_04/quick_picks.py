import random


MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_LINE = 6


def main():
    # Get the number of quick picks
    number_quick_picks = int(input("How many quick picks? "))
    while number_quick_picks < 0:
        print("The number is no sense.")
        number_quick_picks = int(input("How many quick picks? "))

    for i in range(number_quick_picks):
        quick_picks = []  # Create a new list for each quick pick
        for j in range(NUMBER_OF_LINE):  # Generate 6 random numbers
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()  # Sort the numbers in ascending order
        print(" ".join(f"{number:2}" for number in quick_picks))


main()
