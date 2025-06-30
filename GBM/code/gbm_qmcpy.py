import qmcpy as qp
gbm = qp.GeometricBrownianMotion(qp.Lattice(2)) 
gbm.gen_samples(n=4) 