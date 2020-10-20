# %% 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# %%
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime'
                     )


# 3) Return the streamflow January 3-5 as many ways as you can
#Xenia

## Aprroaches using loc
data.loc["1989-01-03":"1989-01-05"][['flow']]
data.iloc[2:5][['flow']]

data.flow.loc["1989-01-03":"1989-01-05"]
data.flow["1989-01-03":"1989-01-05"]
data.flow.iloc[2:5]

data.loc["1989-01-03":"1989-01-05", 'flow']
data.iloc[2:5, 2]


## Approaches using iloc
#Danielle 
#using iloc with a column name
mycol = ['flow', 'code']
data.iloc[2:5][mycol]

#using iloc with a column number
#just flow 
data.iloc[2:5, 2]

#Two consecutive columns
data.iloc[2:5, 2:4]

#every other column
data.iloc[2:5, 0:6:2]

# a list of column numbers
mycol=[0,3]
data.iloc[2:5, mycol]

# Approach using head
#richard
data['flow'].head(5)[2:5]
data.flow.head()[2:5]

# Another approach
data[(data.index.month == 1) & (data.index.day <= 5)
     & (data.index.day >= 3) & (data.index.year == 1989)][["flow", 'code']]

# %%
# Option 1: You have a file locally that you want to read: 
# 1) You need the file location (os.path.join)
# 2) YOu to know how the file is formatted so you can read it correctly 
# this is how we have been reading data:
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime'
                     )


# %%
# Option 2: Read the data from a URL rather than a local file 
# 1) the location of the data --- this time on the internet
# 2) You need to know how its formatted.

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-19"

# Now we can read it with read_table command the same as we did before
# Note this only works if you select the tab separated data --- try it with table and you will see it doesn't
data2 = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                      parse_dates=['datetime'], index_col='datetime')

#separating url onto multiple lines 
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000" \
      "&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-19"

#Replace parts of my url with variables 
site = '09506000'
start = '1990-01-01'
end = '2020-10-16'
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
data2 = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                      parse_dates=['datetime'], index_col='datetime')

# %%
# Option 3: We can generate this URL and get the data using an API
# Technically we were already doing this you just didn't know it 
# API = Application Programming Interface  (Translation - a standard set of appraches/protocols
# for working with a given dataset in a predictable way --- rules for accessing data)
# Different datasets have their own APIs
# 1) Step 1 see if there is an API and get the rules for working with it
