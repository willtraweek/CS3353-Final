#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

from exceptions import *
from truck import Truck
from box import Box
from sortedcontainers import SortedList


class Warehouse:
    """A warehouse stores boxes for shipping.  It can read in manifests and export them.  It also has a list of
    trucks assigned to it.  The largest part of the warehouse's job, though, is preparing said trucks for shipping.
    This is where the Knapsack algorithm comes into play.

    Attributes:
        trucks: A set of trucks available for the warehouse to use
        boxes: A dictionary containing all of the possible boxes and their quantities
        capacity: total capacity of all the trucks available
        value: total value of all of the boxes and trucks here
    """

    def __init__(self):
        self.trucks = SortedList()
        self.boxes = {}
        self.capacity = 0
        self.value = 0

    def __init__(self, input_file_path):
        self.trucks = SortedList()
        self.boxes = {}
        self.capacity = 0
        self.value = 0
        self.import_boxes(input_file_path)

    def import_boxes(self, input_file_path):
        """reads in boxes from a file and adds them to the dictionary"""
        input_file = open(input_file_path, "r")

        for line in input_file.readlines():
            name, weight, price = line.split(",")

            #prevents the first line from being read in
            if name == "name":
                continue

            self.add_box(Box(name, int(weight), int(price)))

    def add_truck(self, capacity):
        """Creates a new truck and adds it to the list"""
        self.trucks.add(Truck(capacity))
        self.capacity += capacity


    def add_box(self, box):
        """add the passed box to the warehouse"""
        if box in self.boxes:
            self.boxes[box] += 1
        else:
            self.boxes[box] = 1

        self.value += box.price

    def remove_box(self, box):
        """removes the passed box from the warehouse"""
        if box not in self.boxes:
            raise BoxRemovalError("Box not in warehouse", box)
        elif self.boxes[box] == 0:
            raise BoxRemovalError("No boxes of this type left in warehouse", box)

        self.value -= box.price
        self.boxes[box] -= 1

        # if the removed item was the final one of its type, remove it
        if self.boxes[box] == 0:
            self.boxes.pop(box)
