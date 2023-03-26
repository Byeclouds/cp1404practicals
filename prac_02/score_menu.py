MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50

MENU = "(G)et a valid score\n(P)rint result \n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    score = float(input("Please enter your score first: "))
    get_a_valid_score(score)
    choice = input("<<< Your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Please enter your score: "))
            get_a_valid_score(score)
        elif choice == "P":
            print(get_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid message.")
        print(MENU)
        choice = input("<<< Your choice: ").upper()
    else:
        print("Farewell.")


def get_a_valid_score(score):
    while score <= 0 or score >= MAX_SCORE:
        print("Invalid score.")
        score = float(input("Please enter your score: "))
    return score


def get_score(score):
    if score < 0 or score > MAX_SCORE:
        message = "Invalid score"
    elif score >= EXCELLENT_SCORE:
        message = "Excellent"
    elif score >= PASS_SCORE:
        message = "Passable"
    else:
        message = "Bad"
    return message


def show_stars(score):
    print('*' * int(score))


main()
