#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

import os
import random
from box import Box


def create_test_set(numBoxes=10, maxWeight=50, maxPrice=100, test_num=0):
    """creates a test set based off of the NAPCS list
    randomizes prices and weights

    Attributes:
        numBoxes: the number of boxes to generate
        maxWeight: weight will be randomly generated between [0,maxWeight)
        maxPrice: price will be randomly generated between [0,maxPrice)
        test_num: a number that you can append to the test
            this is useful if you want to create multiple tests
    """

    input_file = open("./NAPCS.txt", "r").readlines()
    if test_num != 0:
        output_file = open(f"./examples/available_boxes_{test_num}.csv", "w+")
    else:
        output_file = open(f"./examples/available_boxes.csv", "w+")

    output_file.write("name,weight,price\n")

    generated_items = {}

    for i in range(numBoxes):
        item_name = input_file[random.randrange(len(input_file))]
        item_name = item_name.strip()

        if item_name in generated_items.keys():
            box = generated_items[item_name]
        else:
            box = Box(item_name, random.randrange(maxWeight), random.randrange(maxPrice))
            generated_items[item_name] = box
        output_file.write(f"{box.name},{box.weight},{box.price}\n")


if __name__ == "__main__":
    create_test_set()
