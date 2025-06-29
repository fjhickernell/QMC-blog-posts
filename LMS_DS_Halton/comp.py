import qmcpy as qp
from time import time
dimension = 25
samples = 100000
rand_options = ['QRNG', 'OWEN', 'LMS', 'DS', 'LMS_DS']
for i in range(len(rand_options)):
    t_start = time()
    rand_halton = qp.Halton(dimension,randomize = 
    rand_options[i], 
    generalize=False).gen_samples(samples,warn=False)
    t_end = time()
    print("Time to generate samples for " + 
    rand_options[i] + "= " + str(t_end - t_start))