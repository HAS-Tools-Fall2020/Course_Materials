# This script assumes you have already downloaded several netcdf files
# see the assignment instructions for how to do this
# %%
import pandas as pd
import matplotlib.pyplot as plt
# netcdf4 needs to be installed in your environment for this to work
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset


#NOTE To install the packages you need you should use the followin line:
# conda install xarray dask netCDF4 bottleneck
# If it doesn't work all together yo might try installing separately

# NOTE 2: If you end up with conflicts and things not workign I recommend you start a
# a new environment and that you set the environment to automatically install packages from
# conda-forge as its first priority. You can do that like this:
# will look for packages at conda-forge first.
# From terminal you do the following:
# conda create --name mynewenv
# conda activate mynewenv
# conda config --add channels conda-forge
# conda config - -set channel_priority strict

# %%
# Net CDF file historical time series
data_path = os.path.join('./data',
                         'Reanalysis_Precip.nc')

# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# look at it
dataset


# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata
# And we can grab out any part of it like this:
metadata['dataset_title']
metadata['history']

# we can also look at other  attributes like this
dataset.values
dataset.dims
dataset.coords

# Focusing on just the precip values
precip = dataset['prate']
precip

# Now to grab out data first lets look at spatail coordinates:
dataset['prate']['lat'].values.shape
# The first 4 lat values
dataset['prate']['lat'].values
dataset['prate']['lon'].values

# Now looking at the time;
dataset["prate"]["time"].values
dataset["prate"]["time"].values.shape


# Now lets take a slice: Grabbing data for just one point
lat = dataset["prate"]["lat"].values[0]
lon = dataset["prate"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset["prate"].sel(lat=lat,lon=lon)
one_point.shape

# use x-array to plot timeseries
one_point.plot.line()
precip_val = one_point.values

# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
one_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="purple",
                    markeredgecolor="purple")
ax.set(title="Time Series For a Single Lat / Lon Location")

#Conver to dataframe
one_point_df = one_point.to_dataframe()

#from here you can do anything you want the same way we have when working with other dataframes
