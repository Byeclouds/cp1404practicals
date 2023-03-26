MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    score = float(input("Enter score: "))
    print(get_score(score))


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


main()
