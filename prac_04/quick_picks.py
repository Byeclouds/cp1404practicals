import random

NUMBERS_EACH_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Asks the user how many "quick picks" they wish to generate"""
    number_quick_picks = int(input("How many quick picks? "))
    while number_quick_picks < 0:
        print("Invalid")
        number_quick_picks = int(input("How many quick picks? "))

    for i in range(number_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_EACH_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print("". join(f"{number:2}" for number in quick_pick))


main()
