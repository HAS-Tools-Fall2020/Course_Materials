# %%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# %%
# Given the following series of flow values and days
# Assume that the flow has uncertainty of +/- 25%
# Come up with a way to visualize this information
flow = np.random.randn(100)
day = range(len(flow))

#Alcely 
flow_down = flow*(0.75)
flow_up = flow*(1.25)


fig, ax = plt.subplots()
ax.plot(flow, color='grey', linewidth=2, label='flow')
ax.plot(flow_down, color='blue', linewidth=2, label='flow-25%')
ax.plot(flow_up, color='red', linewidth=2, label='flow+25%')
ax.set(title="Flows", xlabel="Date", ylabel="Weekly Avg Flow [cfs]")
ax.legend()
plt.show()

# Using fill_between 
fig, ax = plt.subplots()
ax.plot(day, flow)
ax.fill_between(day, flow*0.75, flow*1.25,
                color='gray', alpha=0.2)

# The Python data science handbook also has some examples
# https://jakevdp.github.io/PythonDataScienceHandbook/04.03-errorbars.html


# Quinn
dy = flow*0.25
plt.errorbar(day, flow, yerr=dy, fmt='.k')


# %%

# Fun with functions :) 

x = np.arange(2, 11).reshape(3, 3)
y = 3
answer = np.floor(np.divide(x, y))

# %%
# Our first function 
def get_floor(numerator, denominator):
    fl = np.floor(np.divide(numerator, denominator))
    return fl



floor = get_floor(x, y)
print(floor)

# %% 
def get_floor(numerator, denominator):
    fl = np.floor(np.divide(numerator, denominator))
    print("calculation complete")
    return fl


floor = get_floor(denominator=y, numerator=x)
print(floor)

floor = get_floor(y, x)
print(floor)

# %%
# Adding default values to our funciton 


def get_floor(numerator, denominator=5):
    fl = np.floor(np.divide(numerator, denominator))
    print(denominator)
    return fl


floor = get_floor(x, y)
print(floor)

floor = get_floor(x)
print(floor)


# %%
# multiple outputs  - dividing 2 ways 
def divide_two_ways(numerator, denomiator=5):
    f_divide = np.floor(np.divide(numerator, denomiator))
    reg_divide = np.divide(numerator, denomiator)
    return f_divide, reg_divide

# Getting the outputs as one variable and separating after
output = divide_two_ways(x,y)
# and then separte them out like this 
floor=output[0]
regular=output[1]

#another way to get the ouputs
floor1, regular1 = divide_two_ways(x, y)
print(floor1)
print(regular1)

# %%
# Documenting functions 
# Docstrings 


def get_floor(numerator, denominator=5):
    """ Function to do floor divide 

    This is the function I have ever written. It 
    divides two things these things are NP arrays..

    numerator - np array... 
    denominator - np array...
    """

    fl = np.floor(np.divide(numerator, denominator))
    print(denominator)
    return fl

help(get_floor)

# %%
output = divide_two_ways(x, y)


# %%
