from box import Box
from truck import Truck
from warehouse import Warehouse
from utilities import set_creation
import knapsack
import time
import matplotlib.pyplot as plt


def main():
    # for i in range(1000):
    #    set_creation.create_test_set(numBoxes=(i+1)*10, maxWeight=100, maxPrice=500, test_num=i+1)

    algorithms_list = [knapsack.dynamic_programming_solution,
                       knapsack.greedy_solution]
    algorithm_names = ["Dynamic Programming",
                       "Greedy Solution"]
    # it took me hours to do a full run on my computer, so I modified the code below to do a shortened version as a
    # proof of concept on github.  If you want to run it with the same settings that I did, you can run it with
    # 0 and 150 as the two numbers in the function below
    evaluate_algorithms(algorithms_list, algorithm_names, 0, 150)


if __name__ == "__main__":
    main()
