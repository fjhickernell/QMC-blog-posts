d = 4
halton = qp.Halton(d)
halton_uniform = qp.Uniform(halton,lower_bound=[1,2,3,4],
upper_bound=[5,7,9,11])
fig, ax = qp.plot_proj(halton_uniform, n = [2**6, 2**7, 2**8], 
d_horizontal = [1,2], d_vertical = [3,4])
