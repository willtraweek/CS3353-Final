#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

from box import Box
from truck import Truck
from exceptions import *
import sys


def greedy_algorithm(warehouse, truck):
    while len(warehouse.boxes) > 0 and truck.leftover_space() > 0:
        try:
            box = most_expensive_box(truck.leftover_space(), warehouse.boxes)
            warehouse.load_box(box, truck)
        except IncompatibleBoxError:
            # if there are no compatible boxes left, then return
            return


def most_expensive_box(max_weight, boxes):
    # create a temporary box with maximum weight and minimum price to start
    output_box = Box("temp", sys.maxsize, 0)
    for box in boxes:
        if box.weight < max_weight:
            if box.price > output_box.price:
                output_box = box
    if output_box.price == 0:
        raise IncompatibleBoxError("No compatible boxes left")
    return output_box
