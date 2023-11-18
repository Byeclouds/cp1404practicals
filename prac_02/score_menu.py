MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """The function should select four separate options in menu"""
    print(MENU)
    score = float(input("Enter score: "))
    get_score_value(score)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Please enter your score: "))
            get_score_value(score)
        elif choice == "P":
            print(get_score(score))
        elif choice == "S":
            get_stars(score)
        else:
            print("Invalid message.")
        print(MENU)
        choice = input("<<< Your choice: ").upper()
    else:
        print("Farewell.")


def get_score_value(score):
    """Determine the value of score."""
    while score <= 0 or score >= MAX_SCORE:
        print("Invalid score.")
        score = float(input("Enter score: "))
    return score


def get_score(score):
    if score < 0 or score > MAX_SCORE:
        result = "Invalid score"
    elif score >= EXCELLENT_SCORE:
        result = "Excellent"
    elif score >= PASS_SCORE:
        result = "Passable"
    else:
        result = "Bad"
    return result


def get_stars(score):
    print('*' * int(score))


main()
