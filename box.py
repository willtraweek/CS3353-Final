class Box:
    """The items that we have to ship

    Attributes:
        name: the name of the item in the box
        weight: the weight of the box and item
        value: the price of the goods in the box
    """

    def __init__(self, name, weight, value):
        """Creates the box, adding name, weight, and value"""
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        """Formats the box in a readable format:
        name: weight | value
        """
        return f"{self.name}: {self.weight} lbs | {'${:,.2f}'.format(self.value)}"