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
