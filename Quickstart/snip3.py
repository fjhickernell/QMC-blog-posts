solution, data = stopping_criterion.integrate()
print(data)
"""
Solution: 1.8082         
CustomFun (Integrand Object)
Lattice (DiscreteDistribution Object)
    dimension       2^(1)
    randomize       1
    seed            None
    backend         gail
    mimics          StdUniform
Gaussian (TrueMeasure Object)
    mean            0
    covariance      2^(-1)
CubQMCLatticeG (StoppingCriterion Object)
    abs_tol         1.00e-04
    rel_tol         0
    n_init          2^(10)
    n_max           2^(35)
LDTransformData (AccumulateData Object)
    n_total         2^(16)
    solution        1.808
    r_lag           2^(2)
    time_integrate  0.070
"""