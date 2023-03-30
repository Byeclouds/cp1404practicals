"""
MENU =
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 1.8 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print(f"Result: {celsius:.2f} F")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
"""


def main():
    menu = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(menu)

    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            print(f"Result: {convert_celsius_to_fahrenheit():.2f} F")
        elif user_choice == "F":
            print(f"Result: {convert_fahrenheit_to_celsius():.2f} c")
        else:
            print("Invalid option")

        print(menu)
        user_choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    return celsius


main()
