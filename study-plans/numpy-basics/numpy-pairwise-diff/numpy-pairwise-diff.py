import numpy as np

def pairwise_diff(a: list) -> np.ndarray:
    """
    Returns an (n, n) float64 array of signed pairwise differences.
    """
    a_1 = np.array(a, dtype=np.float64).reshape(-1, 1)
    a_2 = np.array(a, dtype=np.float64).reshape(1, -1)
    return a_1 - a_2
