import qmcpy as qp
dimension = 3
lms_halton = qp.Halton(dimension, randomize= 'LMS', 
generalize=False)
ds_halton = qp.Halton(dimension, randomize= 'DS', 
generalize=False)
lms_ds_halton = qp.Halton(dimension, 
randomize='LMS_DS', generalize=False)
fig1,ax1 = qp.plot_proj(lms_halton, n = 2**5, 
d_horizontal = range(dimension), d_vertical = 
range(dimension),math_ind = False)
fig2,ax2 = qp.plot_proj(ds_halton, n = 2**5, 
d_horizontal = range(dimension), d_vertical = 
range(dimension),math_ind = False)
fig3,ax3 = qp.plot_proj(lms_ds_halton, n = 2**5, 
d_horizontal = range(dimension), d_vertical = 
range(dimension),math_ind = False)
fig1.suptitle("LMS")
fig2.suptitle("DS")
fig3.suptitle("LMS_DS")