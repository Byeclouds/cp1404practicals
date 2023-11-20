"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError in Python typically occurs when a function receives an argument of the correct data type but with an
inappropriate value.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when you try to divide a number by zero.
"""
"""
3. Change the code to avoid the possibility of a ZeroDivisionError:
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
