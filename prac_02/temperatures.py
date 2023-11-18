MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Temperature change program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = change_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = change_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {fahrenheit:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def change_celsius_to_fahrenheit(celsius):
    """Change celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def change_fahrenheit_to_celsius(fahrenheit):
    """Change fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
