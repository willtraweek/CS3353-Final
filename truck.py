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
        self.capacity = capacity
        self.weight = 0
        self.value = 0
        self.boxes = {}  # empty dictionary to start

    def __str__(self):
        return f"{self.weight} lbs / {self.capacity} lbs"

    def to_json(self):
        output = {}

        for key, value in self.boxes.items():
            temp = {}
            temp["weight"] = key.weight
            temp["price"] = key.price
            temp["quantity"] = value

            output[key.name] = temp

        return json.dumps(output, indent=4)

    def add_box(self, box):
        if self.weight + box.weight <= self.capacity:
            if box in self.boxes:
                self.boxes[box] += 1
            else:
                self.boxes[box] = 1

            self.weight += box.weight
            self.value += box.price
        else:
            raise BoxAdditionError("Box too big to fit", self.weight, self.capacity, box)

    def remove_box(self, box):
        """removes a box from the truck"""
        if box not in self.boxes:
            raise BoxRemovalError("Box not in Truck", box)
        elif self.boxes[box] == 0:
            raise BoxRemovalError("No boxes of this type left in truck", box)

        self.weight -= box.weight
        self.value -= box.price
        self.boxes[box] -= 1

        if self.boxes[box] == 0:
            self.boxes.pop(box)
