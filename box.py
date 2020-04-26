class Box:
    """The items that we have to ship"""

    def __init__(self, name, weight, value):
        """Creates the box"""
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return(f"{self.name}: {self.weight}lbs | ${self.value}")

    def print(self):
        print(self)