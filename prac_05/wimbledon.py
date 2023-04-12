FILENAME = "wimbledon.csv"
CHAMPIONS = 2
COUNTRY = 1


def main():
    #  Create the main function of the program
    data = read_data(FILENAME)
    champions = display_champions(data)
    countries = list(display_countries(data))
    countries.sort()

    print("Wimbledon Champions: ")
    for champions, count in champions.items():  # for each champion and count in the dictionary
        print(f"{champions} {count}")
    print()
    print(f"These are {len(countries)} countries have won Wimbledon: ")
    print(",".join(countries))


def read_data(filename):
    # Get the CSV file and read its data
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            row = line.strip().split(',')
            data.append(row)
    return data


def display_champions(data):
    # Counts the numbers for each champion
    champions = {}
    for row in data:
        champion = row[CHAMPIONS]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def display_countries(data):
    # Use the CSV data to get the countries
    countries = set()
    for row in data:
        countries.add(row[COUNTRY])
    return countries


main()
