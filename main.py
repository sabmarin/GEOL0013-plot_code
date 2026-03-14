#import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from function import get_data, plot_data

# Load the data for the scenarios
baseline = get_data('SSP245_baseline', 'all', 'mean')
baseline_DJF = get_data('SSP245_baseline', 'DJF', 'mean')
baseline_JJA = get_data('SSP245_baseline', 'JJA', 'mean')
baseline_MAM = get_data('SSP245_baseline', 'MAM', 'mean')
baseline_SON = get_data('SSP245_baseline', 'SON', 'mean')
ARISE = get_data('ARISE', 'all', 'mean')
ARISE_DJF = get_data('ARISE', 'DJF', 'mean')
ARISE_JJA = get_data('ARISE', 'JJA', 'mean')
ARISE_MAM = get_data('ARISE', 'MAM', 'mean')
ARISE_SON = get_data('ARISE', 'SON', 'mean')
ssp245 = get_data('SSP245', 'all', 'mean')
ssp245_DJF = get_data('SSP245', 'DJF', 'mean')
ssp245_JJA = get_data('SSP245', 'JJA', 'mean')
ssp245_MAM = get_data('SSP245', 'MAM', 'mean')
ssp245_SON = get_data('SSP245', 'SON', 'mean')

scenarios = [ssp245, ssp245_DJF, ssp245_JJA, ssp245_MAM, ssp245_SON,
             ARISE, ARISE_DJF, ARISE_JJA, ARISE_MAM, ARISE_SON]
baselines = [baseline, baseline_DJF, baseline_JJA, baseline_MAM, baseline_SON,
             baseline, baseline_DJF, baseline_JJA, baseline_MAM, baseline_SON]             

scenario_names = ['SSP245 - baseline', 'SSP245 - baseline(winter)', 'SSP245 - baseline(summer)', 'SSP245 - baseline(spring)', 'SSP245 - baseline(autumn)',
                  'ARISE - baseline', 'ARISE - baseline(winter)', 'ARISE - baseline(summer)', 'ARISE - baseline(spring)', 'ARISE - baseline(autumn)']
# list of variables to plot
variables = ['pr', 'tas', 'snc', 'npp', 'tasmax']
# dictionary to map variable names to more descriptive labels for plotting
variable_names = {
    'pr': 'Precipitation',
    'tas': 'Temperature',
    'snc': 'Snow Cover',
    'npp': 'Net Primary Productivity',
    'tasmax': 'Maximum Temperature'
}
for scenario, base, name in zip(scenarios, baselines, scenario_names):

    #loop through the variables and create a plot for each one
    for var in variables:
        if var in ['tas', 'tasmax']:
            # use absolute difference for temperature variables in K
            data_to_plot = (scenario - base)[var]
            levels = np.arange(1, 4, 1) 
            cmap = 'RdBu_r'  # appropriate for temperature differences, with blue for cooling and red for warming
            label = 'K'  # unit for temperature difference
        else:
            # use percentage difference for precipitation, snow cover and NPP
            data_to_plot = 100 * ((scenario - base) / base)[var]
            if var == 'pr':
                levels = np.arange(-4, 7, 1)
                cmap = 'BrBG'
            elif var == 'snc':
                levels = np.arange(-42, -21, 2)
                cmap = 'Blues_r'  # from deep blue to light blue, avoiding light colors in the middle
            elif var == 'npp':
                levels = np.arange(7, 16, 1)
                cmap = 'Greens'  # same as above but for green colors
            label = '%'
        
        plot_data(data_to_plot, variable_names[var], name, levels, cmap, label)

        # export figure as PNG with 300dpi in a "figures" folder, creating the folder if it doesn't exist
        os.makedirs('figures', exist_ok=True)
        plt.savefig(f'figures/{variable_names[var]}_difference_{name}.png', dpi=300, bbox_inches='tight')
