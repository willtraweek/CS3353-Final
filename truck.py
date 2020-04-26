from exceptions import *

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

    def add_box(self, box):
        if self.weight + box.weight <= self.capacity:
            if box in self.boxes:
                self.boxes[box] += 1
            else:
                self.boxes.add(box)

            self.weight += box.weight
            self.value += box.value
        else:
            print(f"Box too big to fit.  Weight: {self.weight} Capacity: {self.capacity}\n{box}")

    def remove_box(self, box):
        if box not in self.boxes:
            raise BoxRemovalError("Box not in Truck")
        elif self.boxes[box] == 0:
            raise BoxRemovalError("No boxes of this type left in truck")
