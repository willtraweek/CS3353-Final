#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

from box import Box
from truck import Truck
from exceptions import *
import sys
import numpy as np


def dynamic_programming_solution(warehouse, truck):
    """This solution finds out the correct answer, but takes a long time to do so.  The Knapsack problem is NP Hard,
    and this solution finds every possible answer for every capacity smaller than the capacity of the truck.

    Attributes:
        warehouse: This is the location of all of the stored boxes that need to be loaded
        truck: The truck that the algorithm is attempting to fill
    """
    solution = []

    for i in range(warehouse.num_boxes()):
        for j in range(truck.capacity):
            return


def greedy_solution(warehouse, truck):
    """This is the trivial implementation.  It finds the most expensive item that will still fit in the truck and loads
    it into the truck.

    Attributes:
        warehouse: This is the location of all of the stored boxes that need to be loaded
        truck: The truck that the algorithm is attempting to fill
    """
    while len(warehouse.boxes) > 0 and truck.leftover_space() > 0:
        try:
            box = most_expensive_box(truck.leftover_space(), warehouse.boxes)
            warehouse.load_box(box, truck)
        except IncompatibleBoxError:
            # if there are no compatible boxes left, then return
            return


def most_expensive_box(max_weight, boxes):
    """This finds the most expensive box that still falls under the maximum weight requirements given.

    Attributes:
        max_weight: The maximum amount of weight that the box can be
        boxes: a dictionary containing many boxes to iterate through
    """
    # create a temporary box with maximum weight and minimum price to start
    output_box = Box("temp", sys.maxsize, 0)
    for box in boxes:
        if box.weight < max_weight:
            if box.price > output_box.price:
                output_box = box
    if output_box.price == 0:
        raise IncompatibleBoxError("No compatible boxes left")
    return output_box
