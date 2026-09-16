import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a = np.array(a)
    return a.T