def main():
    # Create a dictionary of emails and names
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_email_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        # for each email and name in the dictionary
        print(f"{name} ({email})")


def get_email_name(email):
    #  Get the name from the email
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
