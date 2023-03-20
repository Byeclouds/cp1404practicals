"""
Create the file shop_calculator.py and write this program.
Note: start with the main logic, then adjust your program to improve the formatting if you need to.
Note that the example output above uses string formatting to set the currency to 2 decimal places.
"""

DISCOUNT_RATE = 0.9
DISCOUNT_PRICE = 100
total = 0

numbers_items = int(input("Number of items: "))
while numbers_items < 0:
    print("Invalid")
    numbers_items = int(input("Number of items: "))

for i in range(numbers_items):
    price_items = float(input("Price of item: "))
    total += price_items

if total > DISCOUNT_PRICE:
    total *= DISCOUNT_RATE

print(f"Total price for {numbers_items} items is {total:.2f}")
