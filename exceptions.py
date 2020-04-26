class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class BoxRemovalError(Error):
    """Error that occurs when a truck cannot remove a box

    Attributes:
        message: explanation of the error
    """

    def __init__(self, message, box):
        print(message)
        print(box)

class BoxAdditionError(Error):
    """Error that occurs when a truck cannot add a box

    Attributes:
        message: explanation of the error
        capacity: capacity
        box: copy of the box that couldn't be added
    """

    def __init__(self, message, weight, capacity, box):
        print(message)
        print(f"Weight: {weight} Capacity: {capacity}\n{box}")
