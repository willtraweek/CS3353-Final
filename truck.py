from exceptions import *
import json


class Truck:
    """Truck that we'll be filling with Boxes

    Attributes:
        capacity: max weight that the truck can hold
        weight: current weight that the truck holds
        value: the price of the boxes currently in the truck
        boxes: dictionary of all boxes where the key is the box and the value is the quantity
    """

    def __init__(self, capacity):
        """initialize the truck"""
        self.capacity = capacity
        self.weight = 0
        self.value = 0
        self.boxes = {}  # empty dictionary to start

    def __str__(self):
        """returns a string showing how full the truck is"""
        return f"{self.weight} lbs / {self.capacity} lbs"

    def __lt__(self, other):
        if self.capacity < other.capacity:
            return True
        elif self.weight < other.weight:
            return True
        elif self.value < other.value:
            return True
        else:
            return False

    def to_dict(self):
        """returns the items in dictionary format.  helpful for warehouse.to_json"""
        output = {}

        for key, value in self.boxes.items():
            temp = {}
            temp["weight"] = key.weight
            temp["price"] = key.price
            temp["quantity"] = value

            output[key.name] = temp

        return output

    def to_json(self):
        """returns the items in self.boxes in json"""

        return json.dumps(self.to_dict(), indent=4)

    def leftover_space(self):
        return self.capacity - self.weight

    def add_box(self, box):
        """add the passed box to the truck"""
        if self.weight + box.weight <= self.capacity:
            if box in self.boxes:
                self.boxes[box] += 1
            else:
                self.boxes[box] = 1

            self.weight += box.weight
            self.value += box.price
        else:
            # if adding this box would overfill the truck
            raise BoxAdditionError("Box too heavy to fit", self.weight, self.capacity, box)

    def remove_box(self, box):
        """removes the passed box from the truck"""
        if box not in self.boxes:
            raise BoxRemovalError("Box not in Truck", box)
        elif self.boxes[box] == 0:
            raise BoxRemovalError("No boxes of this type left in truck", box)

        self.weight -= box.weight
        self.value -= box.price
        self.boxes[box] -= 1

        # if the removed item was the final one of its type, remove it
        if self.boxes[box] == 0:
            self.boxes.pop(box)
