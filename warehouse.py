#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

from exceptions import *

class warehouse:
    """A warehouse stores boxes for shipping.  It can read in manifests and export them.  It also has a list of
    trucks assigned to it.  The largest part of the warehouse's job, though, is preparing said trucks for shipping.
    This is where the Knapsack algorithm comes into play.

    Attributes:
        trucks: A set of trucks available for the warehouse to use
        boxes: A dictionary containing all of the possible boxes and their quantities
        capacity: total capacity of all the trucks available
        value: total value of all of the boxes and trucks here
    """

    def __init__(self, capacity):
        self.trucks = []
        self.boxes = {}
        self.capacity = capacity
        self.value = 0

    def add_box(self, box):
        """add the passed box to the warehouse"""
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
        """removes the passed box from the warehouse"""
        if box not in self.boxes:
            raise BoxRemovalError("Box not in warehouse", box)
        elif self.boxes[box] == 0:
            raise BoxRemovalError("No boxes of this type left in warehouse", box)

        self.weight -= box.weight
        self.value -= box.price
        self.boxes[box] -= 1

        # if the removed item was the final one of its type, remove it
        if self.boxes[box] == 0:
            self.boxes.pop(box)