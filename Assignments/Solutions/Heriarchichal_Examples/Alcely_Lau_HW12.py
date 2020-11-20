# Section 0: Preprocessing
# Subset the region directly from https://disc.gsfc.nasa.gov/
# Download the data using wget in cmd
# copy the file_links.txt in C:/wgetdown

# %%
# Section 1: Importing Libraries

import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from scipy import stats
import seaborn as sns


# %%
# Section 2: Processing the data
# Section 2.1: open the dataset .HDF5

ds = h5py.File(r'C:\Users\alcel\Documents\GitHub\2020FA_CodingSkills' +
               r'\555_RemoteSensing\hw_9_GPM_DPR\2020-08-27' +
               r'\2A.GPM.DPR.V8-20180723.20200827-S022853-E040126.036907.V06A.HDF5')

# %%
# Section 2.2: Store the interested variables in numpy array.
# Remember to previous check the dataset using .keys()

ds_lat = ds['NS']['Latitude'][2555:2780, :]
ds_lon = ds['NS']['Longitude'][2555:2780, :]
ds_pr = ds['NS']['SLV']['precipRate'][2555:2780, :, 160]
ds_prns = ds['NS']['SLV']['precipRateNearSurface'][2555:2780, :]
ds_hst = ds['NS']['PRE']['heightStormTop'][2555:2780, :]

# Section 2.3: Clean missing values and flatten
lat = np.where(ds_lat[:, :] <= -9999, np.nan, ds_lat[:, :]).flatten()
lon = np.where(ds_lon[:, :] <= -9999, np.nan, ds_lon[:, :]).flatten()
pr = np.where(ds_pr[:, :] <= -9999, np.nan, ds_pr[:, :]).flatten()
prns = np.where(ds_prns[:, :] <= -9999, np.nan, ds_prns[:, :]).flatten()
hst_noflat = np.where(ds_hst[:, :] <= -9999, np.nan, ds_hst[:, :])
hst = hst_noflat.flatten()

# %%
# Section 3: Statistical analysis
# Section 3.1: Difference, correlation and BIAS for scatter plot
# Difference
dif_pr = (prns - pr).round(2)

# Pearson correlation coefficient
pearson_pr = round(stats.pearsonr(prns, pr)[0], 2)

# Bias = mean error
bias_pr = round(dif_pr.mean(), 2)

# Section 3.2: Maximum height storm top and max bin
maxh = (round(np.nanmax(hst), 2))
maxbin = int(176 - (maxh/125))

# Max Lon, Lat and beam
lon_maxh = round(lon[np.nanargmax(hst)], 2)
lat_maxh = round(lat[np.nanargmax(hst)], 2)
beam_maxh = np.argmax(np.amax(ds_hst, axis=0))

# %%
# Section 3.3: Prepare the reflectivity profile (cross track)
# using  “zFactorCorrected” variable.
# through the maximun height:
dbz_hmax = ds['NS']['SLV']['zFactorCorrected'][2555:2780, beam_maxh, :]
dbz_hmax_c = np.where(dbz_hmax[:, :] <= -9999, np.nan, dbz_hmax[:, :])
lat_hmax = ds_lat[:, beam_maxh]
lon_hmax = ds_lon[:, beam_maxh]

# through the hurricane eye:
dbz_eye = ds['NS']['SLV']['zFactorCorrected'][2555:2780, 48, :]
dbz_eye_c = np.where(dbz_eye[:, :] <= -9999, np.nan, dbz_eye[:, :])
lat_eye = ds_lat[:, 48]
lon_eye = ds_lon[:, 48]

# Altitude array in meters, from bin0 = 0 to bin175 = 22000
z_dbz = np.arange(176*125, 0, -125)

# Dataframe with z_dbz as index
df_dbz_hmax = pd.DataFrame(data=dbz_hmax_c.T, index=z_dbz)
df_dbz_eye = pd.DataFrame(data=dbz_eye_c.T, index=z_dbz)

# %%
# Section 4: Mapping
# Section 4.1: Create a dataframe
df = pd.DataFrame({'lon': lon, 'lat': lat,
                   'pr2km': pr, 'prns': prns,
                   'hst': hst, 'dif_pr': dif_pr})

# Section 4.2: set geometry and create a geodataframe
geometry = gpd.points_from_xy(df['lon'], df['lat'])
geo_df = gpd.GeoDataFrame(df, geometry=geometry)


# %%
# Section 4.3: Clipping lon and lat
lonmin = -97.5
lonmax = -92.5
latmin = 28.5
latmax = 31

# Section 4.4: plot map
plt.style.use('seaborn-white')

col_var = ['prns', 'pr2km', 'hst', 'dif_pr']
cmap_var = ['jet', 'jet', 'terrain_r', 'bwr']
title_var = ['Precip Rate Near Surface (mm/hr)',
             'Precip Rate at ~2km height from the surface (mm/hr)',
             'Height of storm top (m)',
             'Precip Rate Difference\nbetween Near Surface and at ~2km (mm/hr)']

# %%
# Section 4.5: plotting several times
for i in range(len(col_var)):
    # Variable to plot
    ax = geo_df.plot(figsize=(10, 6), column=col_var[i], alpha=0.7,
                     cmap=cmap_var[i], legend=True)

    # Set world as boundaries
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot(ax=ax, facecolor="None", edgecolors='y', lw=1.2)

    # Clip and format map
    plt.xlim(lonmin, lonmax)
    plt.ylim(latmin, latmax)
    plt.yticks(np.arange(latmin, latmax+1, 0.5), fontsize=10)
    plt.xticks(np.arange(lonmin, lonmax+1, 0.5), fontsize=10)
    plt.ylabel('Latitude($^\circ$)', fontsize=12, labelpad=0)
    plt.xlabel('Longitude($^\circ$)', fontsize=12, labelpad=0)

    # Special map
    if col_var[i] == 'hst':
        text = ('Max: ' + str(maxh) + '\nLat: ' +
                str(lat_maxh) + '\nLon: ' + str(lon_maxh))
        plt.annotate(text, xy=(lon_maxh, lat_maxh),
                     xycoords='data', xytext=(-96, 29), textcoords='data',
                     arrowprops=dict(arrowstyle="->"))
        plt.plot(lon_hmax, lat_hmax, c='k', ls='--', linewidth=2.0,
                 label='Maximun height cross track')
        plt.plot(lon_eye, lat_eye, c='r', ls='--', linewidth=2.0,
                 label='Eye of hurricane cross track')
        plt.legend()

    plt.title('Hurricane Laura\n08-27-2020 from 02:28:53 to 04:01:26\n' +
              title_var[i], fontsize=14)

    plt.savefig(col_var[i] + '.png')
    plt.show()

# %%
# Section 5: Scatter plot
# PrecipRate at 2km -vs- PrecipRate Near Surface
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.set_aspect(1)
sns.regplot(x=prns, y=pr,
            line_kws={"color": "r", "alpha": 0.7, "lw": 2})
ax.set(title="Comparison of GPM DPR Precipitation Rate\n" +
       "Near Surface -vs- at ~2km height from surface",
       xlabel='PrecipRate Near Surface (mm/hr)',
       ylabel='PrecipRate at ~2km (mm/hr)')
textstr = '\n'.join((
    r'$Pearson R = %.2f$' % (pearson_pr, ),
    r'$BIAS = %.2f$' % (bias_pr, )))
ax.text(10, 280, textstr, ha="left", va="center", size=10,
        bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="black", lw=1))

fig.savefig("plot_pr.png")

# %%
# Section 6: Reflectivity profile cross track
plt.style.use('seaborn-white')

var = [df_dbz_hmax, df_dbz_eye]
title_var = ['through the Maximun Height of Storm top',
             'through the eye of the hurricane']
for i in range(len(var)):
    fig, ax = plt.subplots(figsize=(6, 6))

    plot_var = ax.pcolormesh(df_dbz_eye.columns, df_dbz_eye.index, df_dbz_eye,
                             cmap='viridis_r')

    cbar = plt.colorbar(plot_var)
    cbar.set_label('Reflectivity factor with\nattenuation correction (dBZ)')
    plt.grid(which='both', axis='both')
    plt.ylabel('Elevation (mAGL)', fontsize=12, labelpad=0)
    plt.xlabel('Cross track bin', fontsize=12, labelpad=0)
    plt.title('Reflectivity profile\n' + title_var[i] +
              '\nHurricane Laura\n08-27-2020 from 02:28:53 to 04:01:26\n',
              fontsize=14)    
    plt.savefig('dbz_plot' + str(i) + '.png')
    plt.show()

# %%

