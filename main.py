from box import Box
from truck import Truck
from warehouse import Warehouse
from utilities import set_creation


def main():
    # for i in range(10):
    #     set_creation.create_test_set(numBoxes=i*10, maxWeight=i*10, maxPrice=i*15, test_num=i+1)
    warehouse = Warehouse("./examples/available_boxes.csv")


if __name__ == "__main__":
    main()
