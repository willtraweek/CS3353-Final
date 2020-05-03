#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

from box import Box
from truck import Truck
from exceptions import *
import sys
import numpy as np


def dynamic_programming_solution(warehouse, truck):
    """This solution finds out the correct answer, but takes a long time to do so.  The Knapsack problem is NP Hard,
    and this solution finds every possible answer for every capacity smaller than the capacity of the truck.

    We use trucks as items inside of the 2d array, because they were built to manage boxes, so they serve as an
    efficient way of managing them here.  Furthermore, we can just go ahead and copy the trucks instead of having to
    iterate back through the boxes

    Attributes:
        warehouse: This is the location of all of the stored boxes that need to be loaded
        truck: The truck that the algorithm is attempting to fill
    """
    # create 2d array to store values.  Each row represents an item and each column a capacity.  Each cell is the
    # optimal solution for the items above it and the capacity that it currently represents.  By the time the bottom
    # of the table has been reached, the optimal solutions for (0, capacity] will have been found.

    solution = np.zeros((warehouse.num_boxes(), truck.capacity), dtype=Truck)
    boxes = warehouse.to_list()

    for x in range(solution.shape[0]):
        for y in range(solution.shape[1]):
            # this is made slightly more complicated by the fact that numpy allows negative indexes.  Hence, the odd
            # way of going about both indexing and the top two if statements.  However without these, there is no way
            # to properly check for edge cases
            if y < boxes[x].weight:
                solution[x, y] = Truck(truck.capacity)
                continue
            if x == 0:
                # this means there is no previous data on the row above, so we'll have to assume that the current item
                # is the highest value for now
                temp = Truck(truck.capacity)
                temp.add_box(boxes[x])
                solution[x, y] = temp
                continue

            prev_max = solution[x-1, y]

            # make a copy of the best possible truck that we could add the current item to
            temp_truck = solution[x-1, y-boxes[x].weight]
            curr_max = Truck(truck.capacity)
            for key in temp_truck.boxes.keys():
                # the reason we can't simply copy the dictionary over, is that the other values (like weight and value)
                # would not stay the same.  We could copy those over individually as well, but this helps future-proof
                # at the cost of a small amount of run-time
                curr_max.add_box(key)
            # add the current item to that truck
            curr_max.add_box(boxes[x])

            if prev_max == None:
                solution[x, y] = curr_max
            elif prev_max.value < curr_max.value:
                solution[x, y] = curr_max
            else:
                solution[x, y] = prev_max

    for box, quantity in solution[-1, -1].boxes.items():
        for i in range(quantity):
            # this loads the found optimal solution into the given truck
            warehouse.load_box(box, truck)




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
