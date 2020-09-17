# Example solution for HW 3

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

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 600 and flow [i] <= 700:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
subset = [flow[j] for j in ilist]

# %% 
# Answers to the assignment questions: 
#1. What type of variables are `flow`, `year`, `month`, and `day`
#   and how long are they?
print("Flow is a ", type(flow))
print("Flow is", len(flow), "long")

#2. How many times was the daily flow greater than your prediction 
#   in the month of September (express your answer in terms of the total 
#   number of times and as a percentage)?
prediction = 500
gt_list=[]
setp_list=[]
gt_list = [i for i in range(len(flow)) if flow[i] > prediction and month[i]==9]
sept_list = [i for i in range(len(flow)) if month[i]==9]
print("Flow was greater than predition", len(gt_list), "times")
print("this is", len(gt_list)/len(sept_list)*100, "% of the time")

#3. How would your answer to the previous question change if you 
#   considered only flows before 2000 or after 2010? 
#   (again report total number of times and percentage)
gt_list=[]
setp_list=[]
gt_list = [i for i in range(len(flow)) if flow[i] > prediction and \
          month[i]==9 and year[i] >= 2010]
sept_list = [i for i in range(len(flow)) if month[i]==9 and year[i] >= 2010]
print("Flow was greater than predition", len(gt_list), "time after 2010")
print("this is", len(gt_list)/len(sept_list)*100, "% of the time after 2010")

gt_list=[]
setp_list=[]
gt_list = [i for i in range(len(flow)) if flow[i] > prediction and \
          month[i]==9 and year[i] <= 2000]
sept_list = [i for i in range(len(flow)) if month[i]==9 and year[i] <= 2000]
print("Flow was greater than predition", len(gt_list), "time after 2010")
print("this is", len(gt_list)/len(sept_list)*100, "% of the time after 2010")

# 4. How does the flow generally change from the first half of
# September to the second?
first_half = [flow[i] for i in range(len(flow)) if \
        month[i]==9 and day[i] <= 15]
second_half = [flow[i] for i in range(len(flow)) if \
          month[i]==9 and day[i] >= 15]
print("First half average flows", np.mean(first_half))
print("Second half average flows", np.mean(second_half))

# %%
