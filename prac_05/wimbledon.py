"""
Wimbledon
Estimate: 30 minutes
Actual:   25 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read the CSV file, process the data and display processed information"""
    data = get_data(FILENAME)
    champions = get_champions(data)
    countries = list(get_countries(data))
    countries.sort()

    print("Wimbledon Champions: ")

    for champions, count in champions.items():
        print(f"{champions} {count}")
    print()
    print(f"These are {len(countries)} countries have won Wimbledon: ")
    print(",".join(countries))


def get_data(filename):
    """Reads the CSV file and change its data to the lists"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            row = line.strip().split(",")
            data.append(row)
    return data


def get_champions(data):
    """Get every player's number of championships"""
    champions = {}
    for row in data:
        champion = row[CHAMPION_INDEX]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """Get countries from the CSV file."""
    countries = set()
    for row in data:
        countries.add(row[COUNTRY_INDEX])
    return countries


main()
