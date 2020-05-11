import numpy as np
def keister(x):
    # x: nxd numpy ndarray
    #    n samples
    #    d dimensions
    d = x.shape[1]
    norm_x = np.sqrt((x**2).sum(1))
    k = np.pi**(d/2)*np.cos(norm_x)
    return k # size n vector