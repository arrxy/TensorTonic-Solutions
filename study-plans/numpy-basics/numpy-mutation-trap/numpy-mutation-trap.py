import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -> np.ndarray:
    """
    Returns a (2, n) float64 array: original row, then clipped row.
    """
    data = np.array(data, dtype = np.float64)
    reqd_row = data[row_idx]
    updated_row = np.clip(reqd_row, lo, hi)
    return np.stack((reqd_row, updated_row), axis = 0)
