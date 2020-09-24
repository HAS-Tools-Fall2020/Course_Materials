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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code

# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))

# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])


# %%
# Question Answers


#1. Describe the variable flow_data:
#   - What is it?
#   - What type of values is is composed of?
#   - What is are its dimensions, and total size?
print('Type:', type(flow_data))
print('Data Type:' flow_data.dypte)
print('Shape:', flow_data.shape)
print('Size:', flow_data.size)
print('Dimensions:', flow_data.ndim)

#2. How many times was the daily flow greater than your prediction 
#   in the month of September (express your answer in terms of the total 
#   number of times and as a percentage)?
prediction = 500
greater = np.sum((flow_data[:,3] > prediction) & (flow_data[:,1]==9))
greater_pct = greater/np.sum(flow_data[:,1]==9) * 100
print("Flow was greater than predition", greater, "times")
print("this is", greater_pct, "% of the time")

#3. How would your answer to the previous question change if you 
#   considered only flows before 2000 or after 2010? 
#   (again report total number of times and percentage)
greater = np.sum((flow_data[:,3] > prediction) & 
          (flow_data[:,1]==9) & (flow_data[:,0]>=2010))
greater_pct = greater/np.sum((flow_data[:,1]==9) & 
            (flow_data[:,0]>=2010)) * 100
print("Flow was greater than predition", greater, "times")
print("this is", greater_pct, "% of the time")

greater = np.sum((flow_data[:,3] > prediction) & 
          (flow_data[:,1]==9) & (flow_data[:,0]<=2000))
greater_pct = greater/np.sum((flow_data[:,1]==9) & 
            (flow_data[:,0]<=2000)) * 100
print("Flow was greater than predition", greater, "times")
print("this is", greater_pct, "% of the time")

# 4. How does the flow generally change from the first half of
# September to the second?
first_half = np.mean(flow_data[(flow_data[:,2] <= 15) & 
          (flow_data[:,1]==9),3])
second_half = np.mean(flow_data[(flow_data[:,2] >= 15) & 
          (flow_data[:,1]==9),3])
print("First half average flows", np.mean(first_half))
print("Second half average flows", np.mean(second_half))