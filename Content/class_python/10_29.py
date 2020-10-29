# %% 
# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx


# %%
#  Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
file = os.path.join('../../../data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Let look at what this is 
type(gages)
gages.head()
gages.columns
gages.shape

# Looking at the geometry now
gages.geom_type
#check our CRS - coordinate reference system 
gages.crs
#Check the spatial extent 
gages.total_bounds
#NOTE to selves - find out how to get these all at once

# %% 
# Now lets make a map!
fig, ax =plt.subplots(figsize=(5,5))
gages.plot(ax=ax)
plt.show()

# Zoom  in and just look at AZ
gages.columns
gages.STATE.unique()
gages_AZ=gages[gages['STATE']=='AZ']
gages_AZ.shape

#Basic plot of AZ gages
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(ax=ax)
plt.show()

# More advanced - color by attribute
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='OrRd',
              ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
plt.show()


# %% 
# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower colorado 
file = os.path.join('../../../data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")

type(HUC6)
HUC6.head()

# plot the new layer we got:
fig, ax = plt.subplots(figsize=(5, 5))
HUC6.plot(ax=ax)
ax.set_title("HUC Boundaries")
plt.show()

HUC6.crs



# %%
# Add some points
# UA:  32.22877495, -110.97688412
# STream gauge:  34.44833333, -111.7891667
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333]])

#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)

# plot these on the first dataset
#Then we can plot just one layer at atime
fig, ax = plt.subplots(figsize=(5, 5))
HUC6.plot(ax=ax)
point_df.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
plt.show()


# %% 
# Now trying to put it all together - adding our two points to the stream gagees 
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
point_df.plot(ax=ax, color='r', marker='*')

# Trouble!! we are in two differnt CRS
gages_AZ.crs 
point_df.crs

# To fix this we need to re-project
points_project = point_df.to_crs(gages_AZ.crs)

# Trying to plot again 
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='r', marker='*')
# NOTE: .to_crs() will only work if your original spatial object has a CRS assigned
# to it AND if that CRS is the correct CRS!

# now putting everythign on the plot:
# Project the basins 
HUC6_project = HUC6.to_crs(gages_AZ.crs)

# Now plot again
fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=1)


# Adding a basemap 

fig, ax = plt.subplots(figsize=(5, 5))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=1)
ctx.add_basemap(ax)
