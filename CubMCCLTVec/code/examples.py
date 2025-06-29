import qmcpy as qp
import numpy as np

# Covariance Example
class CovIntegrand(qp.integrand.Integrand):
    def __init__(self,sampler):
        self.sampler = sampler
        self.true_measure = qp.Gaussian(sampler,mean=1)
        super(CovIntegrand,self).__init__(
        dimension_indv=3,dimension_comb=1,parallel=False)
    def g(self, t, compute_flags):
        y = np.zeros((len(t),3))
        y[:,1] = t.prod(1) 
        y[:,2] = t.sum(1) 
        y[:,0] = y[:,1]*y[:,2] 
        return y
    def _spawn(self, level, sampler):
        return CovIntegrand(sampler)
    def bound_fun(self, low, high):
        comb_low = low[0]-max(low[1]*low[2],low[1]*high[2],high[1]*low[2],
        high[1]*high[2])
        comb_high = high[0]-min(low[1]*low[2],low[1]*high[2],high[1]*low[2],
        high[1]*high[2])
        return comb_low,comb_high
    def dependency(self, comb_flag):
        return np.tile(comb_flag,3)

ci = CovIntegrand(qp.IIDStdUniform(4, seed=7))
sc_ci = qp.CubMCCLTVec(ci, abs_tol = 0.025)
solution_ci,data_ci = sc_ci.integrate()
print("Solution: " + str(solution_ci))
print("Data: ")
print(data_ci)

# Box Integral Example
f = qp.BoxIntegral(qp.IIDStdUniform(3,seed=7), s=[-1,1])
sc_f = qp.CubMCCLTVec(f,abs_tol = 5e-2)
solution_f,data_f = sc_f.integrate()
print("Solution: " + str(solution_f))
print("Data: ")
print(data_f)

# Custom Fun Example
cf = qp.CustomFun(
        true_measure = qp.Uniform(qp.IIDStdUniform(6,seed=7)),
        g = lambda x,compute_flags=None: (2*np.arange(1,7)*x).reshape(-1,2,3),
        dimension_indv = (2,3))
sc_cf = qp.CubMCCLTVec(cf,abs_tol=1e-2)
solution_cf,data_cf = sc_cf.integrate()
print("Solution: " + str(solution_cf))
print("Data: ")
print(data_cf)