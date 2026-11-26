import numpy as np

def row_extremes(data: list) -> np.ndarray:
    """
    Returns float64 rows of maxima, maximum indices, minima, and minimum indices.
    """
    data = np.array(data, dtype=np.float64)
    max_ = np.max(data, axis=1)
    argmax_ = np.argmax(data, axis=1)
    min_ = np.min(data, axis=1)
    argmin_ = np.argmin(data, axis=1)
    return np.stack([
        max_,
        argmax_,
        min_,
        argmin_
    ])
