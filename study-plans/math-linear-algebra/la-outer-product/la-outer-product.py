import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """
    u = (np.array(u, dtype = 'float64')).reshape(len(u), 1)
    v = (np.array(v, dtype = 'float64')).reshape(len(v), 1)
    ans = u @ v.T
    return ans