# %%
# Experiments with Scalers
# From: https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html
# Best Fit From: https://stackoverflow.com/questions/22239691/code-for-best-fit-straight-line-of-a-scatter-plot-in-python


# ----------------------------------------------------------------------------------
# Outline
# ----------------------------------------------------------------------------------
# 1. Define modules
# 2. Define functions
# 3a. Scalers pt. 1 - unscaled data
# 3b. Scalers pt. 2 - experiment with different scalers **interactive**
# 4a. Bring in and arrange T / P datasets
# 4b. Scale T / P / Flow datasets using norm_it() **look at**
# 5. Autoregressive model with scaled data **look at**

# %% Modules
# ----------------------------------------------------------------------------------
# 1. Define modules
# ----------------------------------------------------------------------------------
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer

from sklearn.datasets import fetch_california_housing

import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import os
import numpy as np

import time

import pandas as pd
# import geopandas as gpd
import numpy as np
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# %% Functions
# ----------------------------------------------------------------------------------
# 2. Define functions
# ----------------------------------------------------------------------------------


def clean_dataset(df):
    """Removes all infinity, nan, and numbers out of range
    from: https://stackoverflow.com/questions/31323499/
    sklearn-error-valueerror-input-contains-nan-infinity-or-a-value-too-large-for
    """
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


def makemodel(x, y):
    """returns a multiple regression model

       using sklearn linear regression tool

       returns the model object = model
       returns the score = score

       takes 2 required variables, x and y
       x is the predictive (independent) variable(s)
       y is the predicted (dependent) variable

       both x and y need to be pandas dataframes, where x
       contains ALL of the predictive (independent) variables
       to be used.

       IMPORTANT: 'x' needs to be a list of column titles, even
       if only one predictive variable is passed

       if dimensions[x] = 1, then single predictive variable
       if dimensions[x] > 1, then multiple predictive variables

       example:
       x = train_week[['flow_tm1']] # use double brackets here
       y = train_week['flow'] # use single brackets here
       m, x = makemodel(x,y)
       """

    model = LinearRegression()
    y = y.values
    if x.shape[1] == 1:
        x = x.values.reshape(-1, 1)
    print(type(y))
    print(type(x))
    model.fit(x, y)
    score = model.score(x, y)
    return model, score


def extractmasonet(base_url, args):
    """takes
       1) a string of 'base_url'
       2) a dictionary of api arguments
       3) a string of 'token'
       specific to the metamot API

       See more about metamot:
       https://developers.synopticdata.com/mesonet/explorer/
       https://developers.synopticdata.com/about/station-variables/
       https://developers.synopticdata.com/mesonet/v2/getting-started/

       returns a dictionary
       containing the response of a JSON 'query'
       """

    # concat api arguments (careful with commas)
    apiString = urllib.parse.urlencode(args)
    apiString = apiString.replace('%2C', ',')

    # concat the API string to the base_url to create full_URL
    fullUrl = base_url + '?' + apiString
    print('full url =', fullUrl, '\n')

    # process data (use url to query data)
    # return as dictionary
    response = req.urlopen(fullUrl)
    responseDict = json.loads(response.read())

    return responseDict


def assemble_data_masonet(base_url, args, stationDict,
                          data_join,
                          station_condition='ACTIVE',
                          station_name=False):
    """takes the basics for a data extraction
        and pulls out only the stations that meet a certain condition

        base_url = url at masonet for extraction
        args = arguments, including token and parameters
        station_Dict = a previously created response Dictionary
            of stations
        data_join = an external pandas dataset to join the data to.
            Must contain a datetime index
        station_condition = the condition used to crete response for data
            default is to look for only active stations. Only acceptable
            values are 'ACTIVE' and 'INACTIVE'
        station_name = by default FALSE. If specified a string, will
            only look for stations by the name specified.

        note by default resamples the data daily on the max

        returns a panda dataframe containint he data wanted
        """

    # 2b) Assemble all relevant dictionaries into a list, based on station name
    stationList = []
    for station in stationDict['STATION']:
        # station name and if is active
        print(station['STID'], station['STATUS'], station["PERIOD_OF_RECORD"],
              "\n")
        # time series data args
        args['stids'] = station['STID']
        # extract data from active/inactive stations
        if station['STATUS'] == station_condition:
            # if a station name is specified
            if station_name is not False:
                if (station['STID'] == station_name):
                    # extract data
                    responseDict = extractmasonet(base_url, args)
                    # create a list of all stations
                    stationList.append(responseDict)
            # if station name is not specified
            else:
                # extract data
                responseDict = extractmasonet(base_url, args)
                # create a list of all stations
                stationList.append(responseDict)

    # Checks to see if the API Call returned valid data
    if stationList[0]['SUMMARY']['RESPONSE_CODE'] == -1:
        print(stationList[0]['SUMMARY']['RESPONSE_MESSAGE'])
        return "nothing"

    # 2d) convert all data pd
    # list of keys under observations (for use in inner loop)
    for station in stationList:
        # if station id has the station_name, or station_name is False
        if (station['STATION'][0]['STID'] == station_name) or \
                            (station_name is False):
            print(station['STATION'][0]['STID'])
            for key, value in station["STATION"][0]['OBSERVATIONS'].items():
                # creates a list of value related to key
                # temp = station["STATION"][0]['OBSERVATIONS'][key]
                if (key == 'date_time'):
                    # create index
                    df = pd.DataFrame({key: pd.to_datetime(value)})
                else:
                    # concat df
                    df = pd.concat([df, pd.DataFrame({key: value})], axis=1)
            # # set index for df
            df = df.set_index('date_time')
            # resample on day
            df = df.resample('D').max()
            # join df to data dataframe
            data_join = data_join.join(df,
                                       rsuffix="_"+station['STATION'][0]['STID'
                                                                         ])
            df = pd.DataFrame()
    return data_join


def norm_it(startdate, enddate, dfin, dfname, l_back=1, toscale=True):
    """
    This function noramlizes a column of data from a pandas dataframe
    using the MinMaxScaler feature of sklearn
    to create a ~ normal distribution
    and allow for better fitting between different types of variables
    in a multivariable regression

    It also lags the data by a specified number of weeks (look_back)

    Takes:
    A start and end date (strings)
        startdate =
        enddate =
    A dataframe (pandas)
        dfin =
    The name of a single column of data to normalize (string)
        dfname =
    A specified number of look backs (integer)
        l_back = [1]
    A Boolean to decide if to scale the data (i.e. if not desired or already done)
        toscale = [True]

    Returns:
    The dataframe with a column of normalized, and lagged, data
    The scaler model that can be used to 'inverse' transform
        """

    # # subset
    dfin = dfin.loc[startdate:enddate]
    if toscale is True: 
        # # normalize
        scaler = MinMaxScaler(feature_range=(0, 1))
        # # add normalized to dataset
        dfin[dfname+'_norm'] = scaler.fit_transform(dfin[
                                                dfname].to_numpy().reshape(-1, 1))
        # # lag
        dfin[dfname+'_norm'+str(l_back)] = dfin[dfname+'_norm'].shift(l_back)
        return dfin, scaler
    else:
        dfin[dfname+str(l_back)] = dfin[dfname].shift(l_back)
        return dfin


def denorm_it(val, scaler):
    """De normalizes a single value

    Takes:
    A scaled value (a single number)
        val =
    A scaler from sklearn
        scaler =
    """
    # # inverse transform a single value
    newval = scaler.inverse_transform(val.reshape(1, -1))
    return newval


# %%
# ----------------------------------------------------------------------------------
# 3a. Scalers (pt1)
# ----------------------------------------------------------------------------------

start = '2010-01-01'
end = '2020-12-31'
site = '09506000'
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on" \
      "&format=rdb&site_no="+site+"&referred_module=sw&" \
      "period=&begin_date="+start+"&end_date="+end

flow_df = pd.read_table(url, sep='\t', skiprows=31,
                        names=['agency_cd', 'site_no',
                               'datetime', 'flow', 'code'],
                        parse_dates=['datetime'],
                        index_col='datetime'
                        )

flow_df.index = flow_df.index.tz_localize(tz="UTC")
flow_df = flow_df.resample("W").mean()

# unscaled and unnormalized data
print('unscaled and unnormalized data')
plt.hist(flow_df['flow'])
plt.show()

time.sleep(3)
# # x and y
temp = flow_df['flow']
x = temp.values[:-1]
y = temp.values[1:]
# plot
plt.scatter(x, y, zorder=0)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), zorder=1, color='black')
plt.show()
# delete vals
del(temp, x, y)

time.sleep(3)

# re-instantiate data with just the natural log of
# its flow values (to be used later)
print('unscaled and natural log normalized data')
flow_df = np.log(flow_df[['flow']])
plt.hist(flow_df['flow'])
plt.show()

time.sleep(3)
# # x and y
temp = flow_df['flow']
x = temp.values[:-1]
y = temp.values[1:]
# plot
plt.scatter(x, y, zorder=0)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), zorder=1, color='black')
plt.show()
# delete vals
del(temp, x, y)

# %%
# ---------------------------
# 3b. scalers (pt 2) - the experiment
# # # # USER-DEFINED VARIABLE TO SLICE <scalerl> (below)
ind = 0
# ---------------------------

scalerl = [MinMaxScaler(feature_range=(0, 1)), RobustScaler(), 
            PowerTransformer(), QuantileTransformer(output_distribution='normal'),
            QuantileTransformer(output_distribution='uniform')]
scaler = scalerl[ind]
print(scaler)

# scaled data
temp = scaler.fit_transform(flow_df['flow'].to_numpy().reshape(-1, 1))
# # add scaled to dataset
plt.hist(temp)
plt.show()
# # x and y
x = temp[:-1, 0]
y = temp[1:, 0]
# plot
plt.scatter(x, y, zorder=0)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), zorder=1, color='black')
# delete vals
del(temp, x, y, scaler)

# %% import other datasets
# ----------------------------------------------------------------------------------
# 4a. Temperature and Precip Datasets, Arrange and Merge with flow data
# ----------------------------------------------------------------------------------

# # --------------------------------------------------------------------------
# # Mesonet import and assembly
# # --------------------------------------------------------------------------
# 1) quickly look for nearby stations
# 1a) Token
# # IMPORTNAT: I overused my token ('a836998da79e4faeac2bf7f5cda57a6e')
# # so I am only able to use the demo token below
mytoken = 'demotoken'
# 1b) 'Base' URL
base_url = "https://api.synopticdata.com/v2/stations/metadata"
# 1c) nearby stations
# look for 10 nearest stations within 10 miles of usgs gaging station
args = {
       'token': mytoken,
       'radius': '34.448333,-111.789167,10',
       'limit': '10',
       }
# 1d) Extract station synoptic data
stationDict = extractmasonet(base_url, args)

# 2) Extract time series data from active sites
# 2a) 'Base' URL
base_url_in = "https://api.synopticdata.com/v2/stations/timeseries"
arg_vars = 'air_temp,precip_accum'
arg_units = 'temp|F,precip|mm'
args_in = {
        'start': start.replace('-', '')+'0000',
        'end': end.replace('-', '')+'0000',
        'obtimezone': 'UTC',
        'vars': arg_vars,
        'stids': '',
        'units': arg_units,
        'token': mytoken}
station_condition_in = 'ACTIVE'
station_name_in = 'QVDA3'

masonet_df = assemble_data_masonet(base_url_in, args_in, stationDict,
                                      data_join=pd.DataFrame(index=flow_df.index),
                                      station_name=station_name_in)

# ----------------------------------------------------------------------------------
# resample, subset, and lag datasets
# ----------------------------------------------------------------------------------
# sumarize flow, precip, air temp on weekly basis
# # resample
# # # flow
flow_df = flow_df.resample("W").mean()
# # # precip and temp masonet
masonet_df['precip_accum_set_1'] = masonet_df['precip_accum_set_1'] \
                                - masonet_df['precip_accum_set_1'].shift(1)
masonet_df['precip_accum_set_1'].where(
            masonet_df['precip_accum_set_1'] > 0, inplace=True)
p_masonet_df = pd.DataFrame(
                            masonet_df['precip_accum_set_1'].
                            resample("W").sum()
                            )
t_masonet_df = pd.DataFrame(
                            masonet_df['air_temp_set_1'].
                            resample("W").mean()
                            )
# %%
# ----------------------------------------------------------------------------------
# 4b. scale datasets
# ----------------------------------------------------------------------------------
# NOTE: This is where I use the scaler in the dataset
# # subset, normalize, and lag
flow_df, scale1 = norm_it(start, end, flow_df, 'flow', l_back=1)
print("min/max of unscale flow =", np.min(flow_df['flow']), np.max(flow_df['flow']))
print("min/max of scale flow =", np.min(flow_df['flow_norm']), np.max(flow_df['flow_norm']))
p_masonet_df, scale2 = norm_it(start, end, p_masonet_df,
                                  'precip_accum_set_1', l_back=1)
print("min/max of unscale precip =", np.min(p_masonet_df['precip_accum_set_1']), np.max(p_masonet_df['precip_accum_set_1']))
print("min/max of scale precip =", np.min(p_masonet_df['precip_accum_set_1_norm']), np.max(p_masonet_df['precip_accum_set_1_norm']))

t_masonet_df, scale3 = norm_it(start, end, t_masonet_df,
                                  'air_temp_set_1', l_back=1)
print("min/max of unscale temp =", np.min(t_masonet_df['air_temp_set_1']), np.max(t_masonet_df['air_temp_set_1']))
print("min/max of scale temp =", np.min(t_masonet_df['air_temp_set_1_norm']), np.max(t_masonet_df['air_temp_set_1_norm']))

# %% Using scaled data for regression (from HW_12)
# ----------------------------------------------------------------------------------
# 5. Build an autoregressive model with MinMaxScaler
# ----------------------------------------------------------------------------------
# Step 1: pick regression variables
# Step 2: pick periods of regression (train)
# Step 3: subset data to regression (trains)
t = pd.concat([flow_df, p_masonet_df, t_masonet_df], axis=1)
t = clean_dataset(t)
t = t.reset_index()

# Step 4: Fit a linear regression to 'train' data using sklearn
# for (i) 1 and 2 week prediction
# # predictive variables (all normalized between 0 and 1) =
# # # 1) 'flow_norm_tm1' (log of flow last week)
# # # 2) 'air_temp_set_1_norm' (mean weekly temperature, over 10 years)
# # # 2) 'precip_accum_set_1_norm' (sum weekly preciptation, over 10 years)
x = t[['flow_norm1',
       'air_temp_set_1_norm',
       'precip_accum_set_1_norm']]
# # dependent variable = 'flow' (log of flow this week)
y = t['flow_norm']
# # use predifined function (makemodel) to generate model
m, s = makemodel(x, y)

print('coefficient of determination:', np.round(s,2))
print('intercept:', np.round(m.intercept_, 2))
print('coeff 1:', np.round(m.coef_[0], 2))
print('coeff 2:', np.round(m.coef_[1], 2))
print('coeff 3:', np.round(m.coef_[2], 2))


# %%
