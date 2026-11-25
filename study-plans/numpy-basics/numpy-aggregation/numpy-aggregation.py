import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    data = np.array(data, dtype = np.float64)
    mean = np.mean(data, axis = axis)
    std = np.std(data, axis = axis)
    min_ = np.min(data, axis = axis)
    max_ = np.max(data, axis = axis)
    return np.stack([mean, std, min_, max_])
