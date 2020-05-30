solution,data = stopping_criterion.integrate()
print(data)
'''
Solution: 1.8082         
QuickConstruct (Integrand Object)
Lattice (DiscreteDistribution Object)
	dimension       2
	scramble        1
	seed            None
	backend         gail
	mimics          StdUniform
Gaussian (TrueMeasure Object)
	distrib_name    Lattice
	mean            0
	covariance      0.5000
CubLattice_g (StoppingCriterion Object)
	abs_tol         0.0001
	rel_tol         0
	n_init          1024
	n_max           34359738368
CubatureData (AccumulateData Object)
	n_total         65536
	solution        1.8082
	r_lag           4
	time_integrate  0.0708
'''