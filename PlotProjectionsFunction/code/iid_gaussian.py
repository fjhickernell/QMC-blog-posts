d = 2
iid = qp.IIDStdUniform(d)
iid_gaussian = qp.Gaussian(iid,mean =[2,4],covariance=[[9,4],[4,5]])
fig,ax = qp.plot_proj(iid_gaussian, n = 2**7)
ax[0,0].axvline(x=0,color= 'k',alpha=.25); #adding vertical line
ax[0,0].axhline(y=0,color= 'k',alpha=.25); #adding horizontal line