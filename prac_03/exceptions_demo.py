"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    The numerator or denominator is invalid.
2. When will a ZeroDivisionError occur?
    The denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Of course, as follows:
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
