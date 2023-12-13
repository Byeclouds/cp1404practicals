"""
Guitar
Estimate: 20 minutes
Actual:   25 minutes
"""

NOW_YEAR = 2017
GUITAR_YEAR = 50


class Guitar:
    """Create a Guitar class to store one guitar with 3 fields"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise the guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the year of guitar"""
        return NOW_YEAR - self.year

    def is_vintage(self):
        """Determine the guitar's year longer then 50 or not"""
        return self.get_age() >= GUITAR_YEAR
