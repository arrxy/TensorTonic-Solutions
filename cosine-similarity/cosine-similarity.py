import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    if np.linalg.norm(b) == 0 or np.linalg.norm(a) == 0:
        return 0.0
    cosine_similarity = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return cosine_similarity.item()