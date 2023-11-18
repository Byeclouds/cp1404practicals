MIN_LENGTH = 10


def main():
    """The program should then print asterisks as long as the word."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get password and its length at least MIN_LENGTH."""
    password = input(f"Enter your password at least {MIN_LENGTH}: ")
    while len(password) < min_length:
        print(f"Your password is too short.")
        password = input(f"Enter your password at least {MIN_LENGTH}: ")
    return password


def print_asterisks(password):
    """Change the password to asterisks."""
    print("*" * len(password))


main()
