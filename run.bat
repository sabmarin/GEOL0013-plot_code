@echo off
REM Batch file to check and install required Python packages, then run main.py

REM List of required packages
set PACKAGES=numpy matplotlib scipy cartopy xarray netCDF4

REM Check and install each package if not present
for %%p in (%PACKAGES%) do (
    echo Checking for %%p...
    python -c "import %%p" 2>nul
    if errorlevel 1 (
        echo %%p is not installed. Installing...
        pip install %%p
        if errorlevel 1 (
            echo Failed to install %%p. Please check your Python and pip setup.
            pause
            exit /b 1
        )
    ) else (
        echo %%p is already installed.
    )
)

REM Run the main Python script
echo Running main.py...
python main.py

REM Pause to see output
pause
