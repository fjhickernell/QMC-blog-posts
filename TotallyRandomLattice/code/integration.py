import qmcpy as qp

d = 5  
tol = 1E-3 

data_random = qp.CubQMCLatticeG(
    qp.Keister(
        qp.Gaussian(
            qp.Lattice(d,generating_vector = 26),
            mean = 0, covariance = 1/2)
        ), 
    abs_tol = tol).integrate()[1]
data_default = qp.CubQMCLatticeG(
    qp.Keister(
        qp.Gaussian(
            qp.Lattice(d),
            mean = 0, covariance = 1/2)
        ),
    abs_tol = tol).integrate()[1]
print("Integration data from a random lattice generator:")
print(data_random)
print("\nIntegration data from the default lattice generator:")
print(data_default)
