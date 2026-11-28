import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    if np.linalg.norm(a) * np.linalg.norm(b) == 0:
        return 0
    return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
    