import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    data = np.array(data, dtype = np.float64)
    ele_mask = (data > threshold).astype(np.float64)
    any_mask = (data > threshold).any(axis = 1, keepdims = True)
    all_mask = (data > threshold).all(axis = 1, keepdims = True)
    result = [ele_mask, np.where(any_mask, data, 0.0), np.where(all_mask, data, 0.0)]
    return np.array(result)
