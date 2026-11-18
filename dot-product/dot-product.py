import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    ans = 0.0
    for i in range(len(x)):
        ans += (x[i] * y[i])
    return ans