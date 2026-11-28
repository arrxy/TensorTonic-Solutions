import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """
    vectors = np.array(vectors, dtype=np.float64)
    coefficients = np.array(coefficients, dtype=np.float64)
    coefficients = coefficients.reshape(-1, 1)
    print(vectors)
    print(coefficients)
    print(vectors * coefficients)
    vectors = vectors * coefficients
    res = np.sum(vectors, axis=0)
    print(res)
    return np.sum(vectors, axis=0)