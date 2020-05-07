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


def setup_graph(algorithm, file_num):
    """This creates the data for us to graph

    Attributes:
        algorithm: The function that we're going to be running
        file_num: this helps predict the size of the truck that we'll need and helps us scale to match the size of the
            input file
    """
    start = time.process_time()
    warehouse = Warehouse(f"./available_boxes_{file_num}.csv")
    original_value = warehouse.value
    trucks = []
    for i in range(file_num):
        # if i % 10 == 1 or i == 0:
        if i == 0:
            trucks.append(Truck((file_num + 1) * 10))
            warehouse.add_truck(trucks[-1])
            algorithm(warehouse, trucks[-1])
    loaded_value = original_value - warehouse.value

    return loaded_value, time.process_time() - start


def graph_algorithms(x, names, *args, **kwargs):
    """Graphs all of the different tracked values through matplotlib

    Attributes:
        x: keeps track of the x values.  These are the iterations that the previous algorithm went through
        names: the names (in the same order as each of the args), of each of the algorithms
        *args: These are the lists of lists of x values as defined by kwargs
        **kwargs: These are the names that each list will be defined by
    """
    labels = []
    for kwarg in kwargs.values():
        labels.append(kwarg)

    for i in range(len(args)):
        # graph = plt.()
        # graph.set_xdata(args[i])
        for j in range(len(args[i])):
            plt.plot(x, args[i][j], label=names[j])

        plt.legend()
        plt.title(labels[i])

        plt.savefig(f"./graphs/{labels[i]}")
        plt.close()


def save_to_csv(x, names, *args, **kwargs):
    """This saves the values we found to CSV for further analysis"""
    output = open("./output.csv", "w+")

    # create header
    output.write(f"X,")
    for kwarg in kwargs.values():
        for i in range(len(names)):
            output.write(f"{names[i]} {kwarg},")
    output.write("\n")

    # create rest of table
    for i in range(len(args[0][0])):
        output.write(f"{x[i]},")
        for k in range(len(args[0])):
            for j in range(len(args)):
                output.write(f"{args[k][j][i]},")
        output.write("\n")
    output.close()


if __name__ == "__main__":
    main()
