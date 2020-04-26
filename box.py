class Box:
    """The items that we have to ship"""

    def __init__(self, name, weight, value):
        """Creates the box"""
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        """Formats the box in a readable format:
        name: weight | value
        """
        return f"{self.name}: {self.weight} lbs | {'${:,.2f}'.format(self.value)}"