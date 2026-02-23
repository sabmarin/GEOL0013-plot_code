# Practical Week 2 Solutions

## Description

This project analyzes climate data from ARISE (Assessing Responses and Impacts of Solar climate intervention on the Earth system) scenarios. It compares different climate scenarios (SSP245, ARISE-SAI, and baseline) by generating difference maps for key variables such as precipitation, temperature, snow cover, net primary productivity, and maximum temperature. The maps are focused on the Lithuania region and visualize absolute or percentage differences between scenarios.

The main script loads NetCDF data files, processes them using xarray, and creates contour plots with Cartopy for geographic projections.

## Requirements

- Python 3.x
- Required Python packages (see requirements.txt):
  - numpy
  - matplotlib
  - scipy
  - cartopy
  - xarray
  - netCDF4

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository to your local machine.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
   Alternatively, use the provided `run.bat` file (for Windows), which will automatically check for missing packages and install them before running the script.

## Usage

To run the analysis and generate the figures:

- Execute the main script directly: `python main.py`
- Or, on Windows, run `run.bat` which handles dependency installation and execution.

The script will:
- Load data for SSP245, ARISE, and baseline scenarios.
- Compute differences for each variable.
- Generate and save PNG images in the `figures/` directory, showing differences between scenarios (e.g., SSP245 - baseline and ARISE-SAI - baseline).

Each figure includes a colorbar and is saved at 300 DPI.

## Data Structure

- `ARISE_data/`: Contains NetCDF files organized by scenario (ARISE, preindustrial, SSP245, SSP245_baseline) and season (all, DJF, MAM, JJA, SON), with mean and standard deviation files.
- `figures/`: Output directory for generated PNG images (created automatically if it doesn't exist).

## Variables Analyzed

- `pr`: Precipitation
- `tas`: Temperature
- `snc`: Snow Cover
- `npp`: Net Primary Productivity
- `tasmax`: Maximum Temperature

Differences are shown as absolute values (K) for temperature variables and percentages (%) for others.

## Notes

- The maps are projected using Mercator projection and zoomed to the Lithuania region (approximately 19.9°E to 27.8°E, 52.9°N to 57.4°N).
- Ensure the data files are present in the `ARISE_data/` folder before running the script.
- If you encounter import errors, verify that all packages are installed correctly.
