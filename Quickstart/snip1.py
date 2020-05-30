import numpy
def keister(x):
    # x: nxd numpy ndarray
    #    n samples
    #    d dimensions
    d = x.shape[1]
    norm_x = numpy.sqrt((x**2).sum(1))
    k = numpy.pi**(d/2)*numpy.cos(norm_x)
    return k # size n vector