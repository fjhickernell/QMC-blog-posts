import ctypes
from ctypes import CDLL, RTLD_GLOBAL
from os.path import dirname, abspath
from glob import glob
from numpy import *

# load the library 
c_lib = CDLL(
    glob(dirname(abspath(__file__))+'/c_lib*')[0], 
    mode = RTLD_GLOBAL)

# define the function arguments
halton_cf = c_lib.halton_owen
halton_cf.argtypes = [
    ctypes.c_int,  # n
    ctypes.c_int,  # d
    ctypes.c_int, # n0
    ctypes.c_int, # d0
    ctypes.c_int, # randomize
    ctypeslib.ndpointer( # result array 
        ctypes.c_double, 
        flags = 'C_CONTIGUOUS'),  
    ctypes.c_long]  # seed

# define the return value
halton_cf.restype = None

# example call to the function
#   create an empty array to fill with Halton points
x = zeros((5,3), dtype=double)
#   fill the array with 5, 3-dimensional Halton points
halton_cf(5, 3, 0, 0, True, x, 17)