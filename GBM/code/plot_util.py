
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import FixedLocator, FixedFormatter


def plot_error_comparison(ax, samplers, qmcpy_errors, quantlib_errors):
    """Plot error comparison subplot"""
    x = np.arange(len(samplers))
    width = 0.35
    # Plot QuantLib data first (left side)
    ql_x, ql_errors = [], []
    for i, error in enumerate(quantlib_errors):
        if error is not None:
            ql_x.append(i)
            ql_errors.append(error)
    if ql_errors:
        ax.bar([x - width/2 for x in ql_x], ql_errors, width, label='QuantLib', color='blue', alpha=0.8)
    # Plot QMCPy data second (right side)
    ax.bar(x + width/2, qmcpy_errors, width, label='QMCPy', color='red', alpha=0.8)

    ax.set_xlabel('Sampler Type')
    ax.set_ylabel('Mean Error (log scale)')
    ax.set_title('Mean Error Comparison', fontsize=16, fontweight='bold')
    ax.set_yscale('log')
    ax.set_xticks(x)
    ax.set_xticklabels(samplers, rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3)

def plot_performance_comparison(ax, samplers, qmcpy_times, quantlib_times):
    """Plot performance comparison subplot"""
    x = np.arange(len(samplers))
    width = 0.35
    if qmcpy_times is not None:
        # Plot QuantLib timing data first (left side)
        ql_x, ql_times = [], []
        for i, time in enumerate(quantlib_times):
            if time is not None:
                ql_x.append(i)
                ql_times.append(time)
        if ql_times:
            ax.bar([x - width/2 for x in ql_x], ql_times, width, label='QuantLib', color='blue', alpha=0.8)
        # Plot QMCPy data second (right side)
        ax.bar(x + width/2, qmcpy_times, width, label='QMCPy', color='red', alpha=0.8)
        # Add speedup annotations where QuantLib data is available, positioned at center of QMCPy bars
        if len(ql_times) > 0:
            for i, (qmc_time, ql_time) in enumerate(zip(qmcpy_times, quantlib_times)):
                if ql_time is not None:
                    speedup = ql_time / qmc_time
                    annotation_height = qmc_time + max(qmcpy_times) * 0.3
                    # Position arrow at center of QMCPy bar (i + width/2)
                    ax.annotate(f'{speedup:.1f}x faster', 
                               xy=(i + width/2, qmc_time), xytext=(i + width/2, annotation_height),
                               ha='center', va='bottom', fontsize=9, fontweight='bold',
                               arrowprops=dict(arrowstyle='->', color='blue', lw=1))
        
        ax.set_xlabel('Sampler Type')
        ax.set_ylabel('Execution Time (s)')
        ax.set_xticks(x)
        ax.set_xticklabels(samplers, rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'Timing data not available\nRun previous cells to generate data', ha='center', va='center', transform=ax.transAxes, fontsize=12)
    
    ax.set_title('Performance Comparison', fontsize=16, fontweight='bold')


def get_clean_plotting_configuration():
    """Define clear, meaningful colors and styling - no mysterious hex codes"""
    library_colors = {
        'quantlib': {'primary': mcolors.CSS4_COLORS['navy'], 'secondary': mcolors.CSS4_COLORS['darkred']},
        'qmcpy': {'primary': mcolors.CSS4_COLORS['royalblue'], 'secondary': mcolors.CSS4_COLORS['orangered'], 
                 'tertiary': mcolors.CSS4_COLORS['forestgreen'], 'quaternary': mcolors.CSS4_COLORS['purple']}
    }
    
    sampler_color_mapping = {
        'IIDStdUniform': {'quantlib': library_colors['quantlib']['primary'], 'qmcpy': library_colors['qmcpy']['primary']},
        'Sobol': {'quantlib': library_colors['quantlib']['secondary'], 'qmcpy': library_colors['qmcpy']['secondary']},
        'Lattice': {'qmcpy': library_colors['qmcpy']['tertiary']},
        'Halton': {'qmcpy': library_colors['qmcpy']['quaternary']}
    }
    
    plot_formatting = {
        'figure_width': 16, 'figure_height': 6, 'line_thickness': 2, 'marker_size': 6,
        'label_font_size': 14, 'title_font_size': 16, 'legend_font_size': 11, 'grid_transparency': 0.3
    }
    
    return sampler_color_mapping, {'quantlib': 'o', 'qmcpy': 's'}, plot_formatting



def get_plot_styling():
    """Define colors and markers for plotting"""
    return {
        'colors': {
            'QuantLib': {'IIDStdUniform': '#1f77b4', 'Sobol': '#ff7f0e'},
            'QMCPy': {'IIDStdUniform': '#2ca02c', 'Sobol': '#d62728', 
                     'Lattice': '#9467bd', 'Halton': '#8c564b'}
        },
        'markers': {
            'QuantLib': {'IIDStdUniform': 'o', 'Sobol': 's'},
            'QMCPy': {'IIDStdUniform': '^', 'Sobol': 'v', 
                     'Lattice': 'D', 'Halton': 'p'}
        }
    }

def plot_single_series(ax, plot_data, series_name, x_col, y_col, title, xlabel, ylabel, log_scale=False, is_legend=False):
    """Plot a single series (runtime or error) for one experimental series"""
    series_data = plot_data[plot_data['Series'] == series_name]
    styling = get_plot_styling()
    
    # Collect all unique x values from the experiments
    all_x_values = sorted(series_data[x_col].unique())
    
    for method in ['QuantLib', 'QMCPy']:
        method_data = series_data[series_data['Method'] == method]
        
        for sampler in method_data['Sampler'].unique():
            sampler_data = method_data[method_data['Sampler'] == sampler].sort_values(x_col)
            
            if len(sampler_data) > 0:
                x_vals = sampler_data[x_col]
                y_vals = sampler_data[y_col]
                
                color = styling['colors'][method].get(sampler, '#000000')
                marker = styling['markers'][method].get(sampler, 'o')
                
                # Plot with connecting lines for trend visualization
                if log_scale:
                    ax.loglog(x_vals, y_vals, marker=marker, color=color, 
                            linewidth=2, markersize=8, label=f'{method} - {sampler}')
                else:
                    ax.semilogy(x_vals, y_vals, marker=marker, color=color,
                              linewidth=2, markersize=8, label=f'{method} - {sampler}')
    
    # Set x-axis ticks to show only exact experimental values
    ax.set_xticks(all_x_values)
    ax.set_xticklabels([str(int(x)) for x in all_x_values])
    
    # Disable minor ticks to prevent intermediate values from showing
    ax.tick_params(axis='x', which='minor', bottom=False)
    
    # For log plots, we need to explicitly control the x-axis formatter
    if log_scale:
        ax.xaxis.set_major_locator(FixedLocator(all_x_values))
        ax.xaxis.set_major_formatter(FixedFormatter([str(int(x)) for x in all_x_values]))
        ax.xaxis.set_minor_locator(FixedLocator([]))  # Remove minor ticks
    
    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    if is_legend:
        ax.legend(fontsize=10)

def create_parameter_sweep_plots(df):
    """Create 4-panel plots from parameter sweep data"""
    # Filter out theoretical data
    plot_data = df[df['Method'] != 'Theoretical'].copy()
    
    # Create figure with 2x2 subplots
    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    # Panel 1: Mean Error vs n_steps (upper left)
    plot_single_series(ax1, plot_data, 'Time Steps', 'n_steps', 'Mean Error',
                      'Mean Error vs Number of Time Steps\n(n_paths = 4,096)',
                      'Number of Time Steps', 'Mean Error', log_scale=True, is_legend=True)
        
    # Panel 2: Runtime vs n_steps (upper right)
    plot_single_series(ax2, plot_data, 'Time Steps', 'n_steps', 'Runtime (s)',
                      'Runtime vs Number of Time Steps\n(n_paths = 4,096)',
                      'Number of Time Steps', 'Runtime (seconds)', log_scale=True)
    
    # Panel 3: Mean Error vs n_paths (lower left)
    plot_single_series(ax3, plot_data, 'Paths', 'n_paths', 'Mean Error',
                      'Mean Error vs Number of Paths\n(n_steps = 252)',
                      'Number of Paths', 'Mean Error', log_scale=True)

    # Panel 4: Runtime vs n_paths (lower right)
    plot_single_series(ax4, plot_data, 'Paths', 'n_paths', 'Runtime (s)',
                      'Runtime vs Number of Paths\n(n_steps = 252)',
                      'Number of Paths', 'Runtime (seconds)', log_scale=True)
    
    plt.tight_layout()
    plt.savefig('images/figure_7.png', bbox_inches='tight', dpi=150)
    plt.show()
