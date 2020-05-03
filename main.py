from box import Box
from truck import Truck
from warehouse import Warehouse
from utilities import set_creation
import knapsack

def main():
    # for i in range(10):
    #     set_creation.create_test_set(numBoxes=i*10, maxWeight=i*10, maxPrice=i*15, test_num=i+1)
    warehouse = Warehouse("./examples/available_boxes_10.csv")
    truck = Truck(1000)
    warehouse.add_truck(truck)
    knapsack.dynamic_programming_solution(warehouse, truck) # 2252
    #knapsack.greedy_solution(warehouse, truck) # 1798, 2877
    print(truck.value)

if __name__ == "__main__":
    main()
