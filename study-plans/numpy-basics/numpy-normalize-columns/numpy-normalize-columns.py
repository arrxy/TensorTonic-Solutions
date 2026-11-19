import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    data = np.array(data, dtype=np.float64)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    data = data - mean
    data = data / std
    return data
