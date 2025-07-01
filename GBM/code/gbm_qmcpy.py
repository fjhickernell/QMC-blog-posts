import qmcpy as qp
qp_gbm = qp.GeometricBrownianMotion(qp.Lattice(2)) 
qp_gbm.gen_samples(n=4) 