"""
MIN_LENRTH = 10
user_password = str(input("Enter password:"))
while len(user_password) < MIN_LENRTH:
    print("Invalid password")
    user_password = str(input("Enter password:"))
else:
    print("*" * len(user_password))
"""

MIN_LENGTH = 10


def main():
    """Display password or stars."""
    password = get_password()
    display_stars(password)


def get_password():
    """Get user's password print stars."""
    user_password = input("Enter password: ")
    while len(user_password) < MIN_LENGTH:
        print(f"Invalid password, at least {MIN_LENGTH} words.")
        user_password = input("Enter password: ")
    return user_password


def display_stars(user_password):
    """Print stars."""
    print('*' * len(user_password))


main()
