# Notes from class 9-8
# %%
# Step 2 - Import the modules we will use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# %%
#print out the directory I'm currently working in 
print(os.getcwd())

# %% 
# Homework question on data paths
filename = 'streamflow_week1.txt'
#path="/Users/laura/Documents/Teaching/HAS_Tools/Git_Master_organization/Course-Materials/Assignments/Solutions/data"
path="../../../../Git_Master_organization/Course-Materials/Assignments/Solutions/data"

filepath = os.path.join(path, filename)
print(filename)
print(filepath)

data=pd.read_table(filepath, sep = '\t', skiprows=30, 
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )
data = data.set_index('datetime')


# %%
# Training one - Python variables and types 
name = 'laura'  #this is a varible
type(name) #this is me using the function 'type' functionname(argument1, argument2...)

day = 8
type(day)

day=8.0
type(day)

# %% 
#First discussion of lists 
my_list = [1,56,68,100]
type(my_list)
#take the average
#help(np.mean)
np.mean(my_list)

my_list[0:2]



# %%
