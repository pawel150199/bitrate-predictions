import numpy as np
import os 


def split_sequence(sequence: np.array, n_steps: int):
    """
    Split timeseries data

    Args:
        sequence (np.array): Sequence to split
        n_steps (int): step to split
    """    
    X, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)