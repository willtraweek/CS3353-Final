class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class BoxRemovalError(Error):
    """Error that occurs when a truck cannot remove a box

    Attributes:
        message: explanation of the error
    """
    def __init__(self, message):
        self.message = message