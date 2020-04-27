#  Copyright (c) 2020, Will Traweek, All Rights Reserved.

class warehouse:
    """A warehouse stores boxes for shipping.  It can read in manifests and export them.  It also has a list of
    trucks assigned to it.  The largest part of the warehouse's job, though, is preparing said trucks for shipping.
    This is where the Knapsack algorithm comes into play.

    Attributes:
        trucks: A set of trucks available for the warehouse to use
        boxes: A dictionary containing all of the possible boxes and their quantities
        capacity: total capacity of all the trucks available
        value: total value of all of the boxes and trucks here
    """