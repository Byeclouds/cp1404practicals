# 1.Ask name
out_file = open("name.txt", 'w')
name = input("Name:")
print(name, file=out_file)
out_file.close()

# 2.Get name
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()

# 3.Read the first two numbers and adds them together then prints the result
total = 0
with open("numbers.txt", 'r') as in_file:

    for i in range(2):
        number = int(in_file.readline())
        total += number

print(total)

# 4. A file with any number of numbers.
total = 0
with open("numbers.txt", 'r') as in_file:

    for i in in_file:
        total += int(i)

print(total)
