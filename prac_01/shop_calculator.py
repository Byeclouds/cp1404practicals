total = 0
items_number = int(input("Enter number of items: "))

while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Enter number of items: "))

for i in range(items_number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9
print(f"{items_number} items, total price is ${total:.2f}")
