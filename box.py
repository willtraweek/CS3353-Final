class Box:
    """The items that we have to ship

    Attributes:
        name: the name of the item in the box
        weight: the weight of the box and item
        price: the price of the goods in the box
    """

    def __init__(self, name, weight, price):
        """Creates the box, adding name, weight, and value"""
        self.name = name
        self.weight = weight
        self.price = price

    def __str__(self):
        """Formats the box in a readable format:
        name: weight | price
        """
        return f"{self.name}: {self.weight} lbs | {'${:,.2f}'.format(self.price)}"