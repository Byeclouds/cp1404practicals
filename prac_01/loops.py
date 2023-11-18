# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# c.
stars_number = int(input("Enter stars number: "))
for i in range(stars_number):
    print("*", end=' ')
print()
# d.
stars_number = int(input("Enter stars number: "))
for i in range(1, stars_number + 1):
    print("*" * i)
print()
