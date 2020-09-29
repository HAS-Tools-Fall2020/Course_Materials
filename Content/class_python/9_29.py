# %%
import numpy as np
import pandas as pd 


# %%
# Warm up 

# Starter dataframe:
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])


# A) Change the values for all of the vowel rows to 3
#Jill - repeat this for all vowel rows 
#using loc
data_frame.loc["a"] *= 3
data_frame

# Laura - using a list of row names []
data_frame.loc[['a', 'e']] = 3

# Ty - Mask conditional statment 
data_frame[(data_frame.index=='a') | (data_frame.index=='e')][['data2', 'data3']]

data_frame[data_frame['data2']>1]

# B) multiply the first 4 rows by 7
data_frame = data_frame.iloc[:4,  ] * 7

# C) Make the dataframe into a checkerboard  of 0's and 1's using loc
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])
data_frame.loc[['a', 'c', 'e', 'g'], ['data1', 'data3']]=0
data_frame.loc[['b', 'd', 'f'], ['data2']]=0

#Do the same thing without using loc
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])
data_frame.iloc[0:8:2, 0:3:2] = 0
data_frame.iloc[1:8:2, 1:3:2] = 0

