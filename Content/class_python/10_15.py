# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime


# %%
# Warm up
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every colum
# If you have time try doing it with and without a for loop


#Diana
# using np axes to average columns without a loop (implicit *faster :))
def get_mean(data):
    mymean = data.mean(axis=0)
    return mymean

get_mean(data)

#Jake
# Using indexing to go column by column (slower)
def get_mean2(data):
    ans = []
    for i in range(5):
        print(i)
        ans.append(data[:, i].mean())
    return ans

get_mean2(data)

# Laura 
# Defining a simple mean function then calling the function 
# inside of the loop
def simple_mean(input):
    average = np.mean(input)
    return average

#option 1 making an array of zeros to put it in
average = np.zeros(data.shape[1])
for i in range(data.shape[1]):
    average[i] = simple_mean(data[:,i])

#option 2: making a blank array and appending 
average = []
for i in range(data.shape[1]):
    average.append(simple_mean(data[:, i]))


# %%

#reaing in our streamflow data
filename = 'streamflow_week1.txt'
filepath = os.path.join('../../../data', filename)
print(os.getcwd())
print(filepath)

# Read in our data as a dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     )

print(data.dtypes)

# Read in our data as a dataframe - making the dates into a dattime object
data2 = pd.read_table(filepath, sep='\t', skiprows=30,
                      names=['agency_cd', 'site_no',
                             'datetime', 'flow', 'code'],
                      parse_dates=['datetime']
                      )
# after doign parse_dates --- this is treated as a date!                    
print(data2.dtypes)

# %%
# Datetimes plot much more nicely!
plot_data = data.iloc[0:365]
plot_data2 = data2.iloc[0:365]

fig, ax = plt.subplots()
ax.plot(plot_data['datetime'], plot_data['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

fig, ax = plt.subplots()
ax.plot(plot_data2['datetime'], plot_data2['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

fig, ax = plt.subplots()
ax.plot(data2['datetime'], data2['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

# %%
# setting the datetime after the fact 
data3=data.copy()
print(data3.dtypes)
data3['datetime'] = pd.to_datetime(data3['datetime'])
print(data3.dtypes)


#setting this as the index of our dataframe
data3= data3.set_index('datetime')






# %%
# indexing 

# Grab out the first row
data3.iloc[0]

data3.loc["1989-01-01"]

#We can do smater indexing with datetimes
data3.loc["1989"]

# Grab out just one month of data
data3[data3.index.month == 5]

# we can also grab out a range of dates
data3.loc["1989-01-01":"1989-01-20"]

# we can split things up and see components of the data
data3.index.year
data3.index.month
data3.index.day
data3.index.dayofweek



# %%
# you can also resample to aggregate however you want
data_w = data3.resample("w").mean()
data_wmax = data3.resample("w").max()

# You don't have to have your datetime as the index of your dataframe for this to work 
data_w2 = data2.resample("w", on='datetime').mean()

# Can also do it annually 
data_y2 = data2.resample("Y", on='datetime').mean()


