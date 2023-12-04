"""
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""

email_names = {}


def main():
    """Store users' emails (unique keys) and names (values) in a dictionary"""
    user_email = input("Email:")
    while user_email != "":
        get_name = get_email_name(user_email)
        message = input(f"Is your name {get_name}? (Y/n)")
        if message.upper() != "Y" and user_email != "":
            name = input("Name:")
        else:
            name = get_name

        email_names[user_email] = name
        user_email = input("Email:")

        for user_email, get_name in email_names.items():
            print(f"{get_name}({user_email})")


def get_email_name(user_email):
    """Get the name from the user Email"""
    mark = user_email.split("@")[0]
    parts = mark.split(".")
    whole_name = "".join(parts).title()
    return whole_name


main()
