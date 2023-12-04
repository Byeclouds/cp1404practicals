"""
Guitars
Estimate: 30 minutes
Actual:   36 minutes
"""

from prac_06.guitar import Guitar


def main():
    """By using the guitar class to create this function"""
    guitars = []
    print("My guitars")

    name = input("Name:")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add} added.")
        name = input("Name:")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        """do something with i (the index) and guitar (the element)"""
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
