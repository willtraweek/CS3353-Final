class Truck:
    """Truck that we'll be filling with Boxes

    Attributes:
        capacity: max weight that the truck can hold
        weight: current weight that the truck holds
        value: the price of the boxes currently in the truck
        boxes: dictionary of all boxes where the key is the box and the value is the quantity
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.weight = 0
        self.value = 0
        self.boxes = {} #empty dictionary to start

    def add_box(self, Box):