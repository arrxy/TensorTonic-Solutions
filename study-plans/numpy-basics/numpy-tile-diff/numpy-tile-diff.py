import numpy as np

def tile_diff(data: list, reps: int) -> np.ndarray:
    """
    Returns float64 slices of tiled values and next-row differences with a final zero row.
    """
    data = np.array(data, dtype=np.float64)
    
    tile = np.tile(data, (reps, 1))
    diff = np.diff(tile, axis=0)
    return np.stack([
        tile,
        np.pad(diff, ((0,1),(0,0)))
    ])
    
