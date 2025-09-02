def plot_paths(motion_type, sampler, t_final, initial_value, drift, diffusion, n):
    if motion_type.upper() == 'BM':
        motion = qp.BrownianMotion(sampler, t_final, initial_value, drift, diffusion)
        title = f'Realizations of Brownian Motion using {type(sampler).__name__} points'
        ylabel = 'W(t)'
    elif motion_type.upper() == 'GBM':
        motion = qp.GeometricBrownianMotion(sampler, t_final, initial_value, drift, diffusion)
        title = f'Realizations of Geometric Brownian Motion using {type(sampler).__name__} points'
        ylabel = 'S(t)'
    else:
        raise ValueError("motion_type must be 'BM' or 'GBM'")
    
    t = motion.gen_samples(n)
    initial_values = np.full((n, 1), motion.initial_value)
    t_w_init = np.hstack((initial_values, t))
    tvec_w_0 = np.hstack(([0], motion.time_vec))

    plt.figure(figsize=(7, 4));
    plt.plot(tvec_w_0, t_w_init.T); 
    plt.title(title);
    plt.xlabel('t');
    plt.ylabel(ylabel);
    plt.xlim([tvec_w_0[0], tvec_w_0[-1]]);
    plt.show();