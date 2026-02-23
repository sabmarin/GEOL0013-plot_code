#import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime
import scipy.stats as stats
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
from cartopy.util import add_cyclic_point

#define a function to load the data for a given scenario, season and statistic.
def get_data(scenario, season='all', stat='mean'):
    # scenario: 'SSP245', 'SSP245_baseline', 'ARISE', or 'preindustrial'
    # season: 'all', 'DJF', 'MAM', 'JJA', or 'SON'
    # stat: 'mean' or 'std'
    
    # Note: by defining this function with "season='all'" we've defined a default value for our function..
    # .. so if you call the function without specificying a season.. 
    # ..python will assume you want 'all', i.e. the annual mean. 
    
    # Use the scenario, season and stat varibles to select the file location and name. HINT: you'll find matching files in the Data folder"
    # .format() is a handy way to fill in python strings based on variables
#     path = 'Data/{a}/{a}_{b}_{c}.nc'.format(a=scenario, b=season, c=stat)
    path = 'ARISE_data/{a}/{a}_{b}_{c}.nc'.format(a=scenario, b=season, c=stat)
    
    # open the xarray dataset at that file location.
    data = xr.open_dataset(path)
    
    # return the xarray dataset.
    return data


# Load the data for the three scenarios
ssp245 = get_data('SSP245', 'all', 'mean')
baseline = get_data('SSP245_baseline', 'all', 'mean')
ARISE = get_data('ARISE', 'all', 'mean')

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
#ssp245 senario
scenario = 'ssp245'
#loop through the variables and create a plot for each one
for var in variables:
    if var in ['tas', 'tasmax']:
        # use absolute difference for temperature variables in K
        data_to_plot = (ssp245 - baseline)[var]
        levels = np.arange(1, 4, 1) 
        cmap = 'RdBu_r'  # appropriate for temperature differences, with blue for cooling and red for warming
        label = 'K'  # unit for temperature difference
    else:
        # use percentage difference for precipitation, snow cover and NPP
        data_to_plot = 100 * ((ssp245 - baseline) / baseline)[var]
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
    
    #define the lats and lons for plotting, and add a cyclic point to avoid gaps in the plot
    lats = data_to_plot.y
    data_to_plot, lons = add_cyclic_point(data_to_plot, data_to_plot.x)
    
    fig, ax = plt.subplots(figsize=(7, 5), subplot_kw={'projection': ccrs.Mercator()})
    
    p = ax.contourf(lons, lats, data_to_plot, 
                     transform=ccrs.PlateCarree(),
                     cmap=cmap,
                     levels=levels,
                     extend='both')
    
    ax.set_extent([19.9, 27.8, 52.9, 57.4], ccrs.PlateCarree())  # leave some space around lithiuania
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.7)
    ax.set_title(f'{variable_names[var]} difference: {scenario} - baseline ({label})')
    
    # add colourbar with custom position and label
    cax = fig.add_axes([0.85, 0.15, 0.05, 0.7])  # location adjustment for the colorbar
    cbar = plt.colorbar(p, cax=cax, orientation='vertical', label=label)
    
    # export figure as PNG with 300dpi in a "figures" folder, creating the folder if it doesn't exist
    os.makedirs('figures', exist_ok=True)
    plt.savefig(f'figures/{variable_names[var]}_difference_ssp245.png', dpi=300, bbox_inches='tight')
    
    plt.show()

#ARISE-SAI scenario
scenario = 'ARISE-SAI'
for var in variables:
    if var in ['tas', 'tasmax']:
        # use absolute difference for temperature variables in K
        data_to_plot = (ARISE - baseline)[var]
        levels = np.arange(1, 4, 1) 
        cmap = 'RdBu_r'  # appropriate for temperature differences, with blue for cooling and red for warming
        label = 'K'  # unit for temperature difference
    else:
        # use percentage difference for precipitation, snow cover and NPP
        data_to_plot = 100 * ((ARISE - baseline) / baseline)[var]
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
    
    #define the lats and lons for plotting, and add a cyclic point to avoid gaps in the plot
    lats = data_to_plot.y
    data_to_plot, lons = add_cyclic_point(data_to_plot, data_to_plot.x)
    
    fig, ax = plt.subplots(figsize=(7, 5), subplot_kw={'projection': ccrs.Mercator()})
    
    p = ax.contourf(lons, lats, data_to_plot, 
                     transform=ccrs.PlateCarree(),
                     cmap=cmap,
                     levels=levels,
                     extend='both')
    
    ax.set_extent([19.9, 27.8, 52.9, 57.4], ccrs.PlateCarree())  # leave some space around lithiuania
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.7)
    ax.set_title(f'{variable_names[var]} difference: {scenario} - baseline ({label})')
    
    # add colourbar with custom position and label
    cax = fig.add_axes([0.85, 0.15, 0.05, 0.7])  # location adjustment for the colorbar
    cbar = plt.colorbar(p, cax=cax, orientation='vertical', label=label)
    
    # export figure as PNG with 300dpi in a "figures" folder, creating the folder if it doesn't exist
    os.makedirs('figures', exist_ok=True)
    plt.savefig(f'figures/{variable_names[var]}_difference_ARISE_SAI.png', dpi=300, bbox_inches='tight')
    
    plt.show()