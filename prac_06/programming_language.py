"""
Programming language
Estimate: 30 minutes
Actual:   20 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object"""
    def __int__(self, name, typing, reflection, year):
        """Put the given data into class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return the string of the programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine the dynamic type of the programming language"""
        return self.typing == "Dynamic"
