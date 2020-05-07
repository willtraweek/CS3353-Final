from box import Box
from truck import Truck
from warehouse import Warehouse
from utilities import set_creation
import knapsack
import time
import matplotlib.pyplot as plt


def main():
    for i in range(10):
        set_creation.create_test_set(numBoxes=(i + 1) * 10, maxWeight=100, maxPrice=500, test_num=i + 1)

    algorithms_list = [knapsack.dynamic_programming_solution,
                       knapsack.greedy_solution]
    algorithm_names = ["Dynamic Programming",
                       "Greedy Solution"]
    # it took me hours to do a full run on my computer, so I modified the code below to do a shortened version as a
    # proof of concept on github.  If you want to run it with the same settings that I did, you can run it with
    # 0 and 150 as the two numbers in the function below
    evaluate_algorithms(algorithms_list, algorithm_names, 0, 10)


def evaluate_algorithms(algorithm_list, algorithm_names, x_min, x_max):
    """This sets up the collection and management of the rest of the data"""
    x = range(x_min + 1, x_max + 1)

    y_value = []
    y_time = []

    for j in range(len(algorithm_list)):
        temp_value_list = []
        temp_time_list = []
        algorithm = algorithm_list[j]

        for i in x:
            value, temp_time = setup_graph(algorithm, i)
            temp_value_list.append(value)
            temp_time_list.append(temp_time)

        y_value.append(temp_value_list)
        y_time.append(temp_time_list)

    graph_algorithms(x, algorithm_names, y_value, y_time, y_value="Value", y_time="Time")
    save_to_csv(x, algorithm_names, y_value, y_time, y_value="Value", y_time="Time")

if __name__ == "__main__":
    main()
