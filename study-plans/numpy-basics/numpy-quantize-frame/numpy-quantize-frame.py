import numpy as np

def quantize_and_frame(data: list, decimals: int, pad_width: int) -> np.ndarray:
    """
    Returns float64 slices of rounded, floored, and ceiling-rounded values with zero borders.
    """
    data = np.pad(np.array(data, dtype=np.float64), pad_width)
    round = np.round(data, decimals)
    floor = np.floor(data)
    ceil = np.ceil(data)
    return np.stack([
        round,
        floor,
        ceil
    ])
    
