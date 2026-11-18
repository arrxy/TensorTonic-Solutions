import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.array(data, dtype = 'float64')
    if operation == "flatten":
        return data.flatten()
    elif operation == "transpose":
        return data.T
    else:
        return data.reshape(1, *data.shape)
    
