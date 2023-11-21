# 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# 3
in_file = open("numbers.txt", "r")
numbers_first = int(in_file.readline())
numbers_second = int(in_file.readline())
in_file.close()
print(numbers_first + numbers_second)

# 4
in_file = open("name.txt", "r")
total = 0
for line in in_file:
    numbers = int(line)
    total += numbers
in_file.close()
print(total)
