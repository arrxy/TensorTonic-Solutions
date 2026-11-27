import numpy as np

def compare_correlations(a: list, b: list) -> np.ndarray:
    """
    Returns float64 correlation matrices for a, b, and their combined rows.
    """
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    comb = np.concatenate([a,b], axis=0)
    corr_a = np.corrcoef(a.T)
    corr_b = np.corrcoef(b.T)
    corr_both = np.corrcoef(comb.T)
    
    return np.stack([corr_a, corr_b, corr_both])
