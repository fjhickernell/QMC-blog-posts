d = 4
halton = qp.Halton(d)
fig,ax = qp.plot_proj(halton, n = [2**5, 2**6, 2**7], 
d_horizontal = range(d), d_vertical = range(d), 
math_ind = False, marker_size = 15)