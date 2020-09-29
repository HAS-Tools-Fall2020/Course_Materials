# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Solution
# 1. Provide a sumary of the data frames properties. What are the column names? 
# What is its index? What data types do each of the columns have? 
data.columns
data.info()
data.describe()

# 2. Provide a summary of the flow column including the min, mean, max and  
# standard deviation and quartiles
data['flow'].describe()

# 3. Provide the same information but on a monthly basis. (Note: you should
# be able to do this with one or two lines of code)

# one line answer
data_monthly=data.groupby(["month"])[["flow"]].describe()

# two - line answer
data_monthly2=data.groupby(["month"])
data_monthly2[["flow"]].describe()


# 4. Provide a table with the 5 highest and 5 lowest flow 
# valuesfor  the period of record. Include the date, month and flow 
# values in your summary.
data.sort_values(by="flow", ascending = True)
print(data[['datetime', 'month', 'flow']].head(5))
print(data[['datetime', 'month', 'flow']].tail(5))


# 5. Find the highest and lowest flow  values for every month of the year. 
# (i.e. you will find 12 maxs and 12 mins). 
# and report back what year these occured in. 
yearmax=np.zeros(12)
yearmin=np.zeros(12)
for m in range(12):
        monthsort = data[data['month']== (m  +1)].sort_values(by ='flow', ascending=True)\
                [['datetime', 'year', 'flow']]
        print('Month', m)
        print("Minimum")
        print(monthsort.head(1))
        print("Maximum")
        print(monthsort.tail(1))
        yearmin[m] = monthsort['year'].head(1)
        yearmax[m] = monthsort['year'].tail(1)
        

# 6. provide a list of historical dates with flows that are within 10% of your
# week 1 forecast value. If there are none than increase the %10 window until 
# you have at least one other  value and repor the date and the new window you used
forecast = 72
window = 0.10
data[(data['flow']> forecast*(1-window)) & 
      (data['flow'] <  forecast * (1+window)) &
      (data['month'] ==9)]['datetime']
