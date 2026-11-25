import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a = np.array(a)
    b = np.array(b)
    c = np.abs((np.clip(a, lo, hi) - np.clip(b, lo, hi))) / (hi - lo)
    return c
    
