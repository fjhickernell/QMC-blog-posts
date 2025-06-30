import QuantLib as ql
import time

def generate_quantlib_paths(initial_value, mu, sigma, maturity, n_steps, n_paths):
    """Generate GBM paths using QuantLib"""
    process = ql.GeometricBrownianMotionProcess(initial_value, mu, sigma)
    rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(n_steps, ql.UniformRandomGenerator()))
    sequence_gen = ql.GaussianPathGenerator(process, maturity, n_steps, rng, False)
    start_time = time.time()
    paths = np.zeros((n_paths, n_steps + 1))
    for i in range(n_paths):
        sample_path = sequence_gen.next().value()
        paths[i, :] = np.array([sample_path[j] for j in range(n_steps + 1)])
    generation_time = time.time() - start_time
    return paths, generation_time

# Parameters
params = {'initial_value': 100, 'mu': 0.05, 'sigma': 0.2, 'maturity': 1.0, 'n_steps': 252, 'n_paths': 2**14}

# Generate paths 
quantlib_paths, quantlib_time = generate_quantlib_paths(**params)