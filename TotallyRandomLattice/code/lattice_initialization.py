import qmcpy as qp

lattice = qp.Lattice(dimension = 2, generating_vector=21, seed = 120) 
print(lattice) #information about the lattice

n = 4 #number of points in the sample
print(lattice.gen_samples(n))




