# %%
import numpy as np
import pandas as pd 

# %%
#1. Get the largest integer that is less than or equal to the division
# of the inputs x1 and x2 where x1 is all the integers from 1-10 and x2=1.3
#Abibail
x1=np.array(range(1,11))
print(x1)
x2=1.3
x3=x1//x2
print(x3)
print(max(x3))

#alexa
x1 = np.divide(np.arange(1,11,1),1.3).astype(int)

#Laura
x1 = np.arange(1,11)
x2 = 1.3
answer = np.floor_divide(x1,x2)
print(answer)

# 2. given an array x1=[0, 4, 37,17] and a second array with the values
# x2=[1.2, 3, 4.6, 7] return x1/x2 rounded to two decimal places
x1 = [0, 4, 37,17]
x2=[1.2, 3, 4.6, 7]

answer = np.round(np.divide(x1,x2), decimals=2)
print(answer)


# 3. Create a 10 by 100 matrix with 1000 random numbers and report the 
# average and standard deviation across the entire matrix and 
# for each of the 10 rows. Round your answer to  two decimal places

#Hint:
#np.random, np.round , np.mean, np.std 
 
# %%
#PANDAS!
# With pandas - we can can name our rows and columns and refer to them by names
# We don't have to have just one data type like with numpy 
# Builds off of numpy 

# Pandas - series
# Three things - Series, DataFrames and Indices
#making a pandas series - note when you print this that it
# has an extra column to the left --- this is the index!
data = pd.Series([0.1, 50, 47, 1.376])
data0= [0.1, 50, 47, 1.376]

#We can grab elements from the Series the same as we did with a numpy array
data[1:3]

# Or we can name our index differently 
data1 = pd.Series([0.1, 50, 47, 1.376], index=['a', 'b', 'c', 'd'])
data1['b']

# our series has two things it has values and indices
data1.values  #this gives us just the values
data1.index #this is the index that goes with it

# %%
#Pandas - Dataframes
# these are like series but in 2D so we have rows and columns
# remember - the index is always refering to the row numbers/numes
rng = np.random.RandomState(42) # this holds my random numbers constant
dataframe = pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'], 
            index=['row1', 'row2', 'row3']) 

np.random.randn(3,5)

# Grab out a column of data
dataframe.b
np.mean(dataframe.b)

dataframe['b']
np.mean(dataframe['b'])

#grabing out the parts of our dataframe
dataframe.values
dataframe.index
dataframe.columns

# loc - lets you find rows by their names
dataframe['b']
dataframe.loc['row1']
dataframe.loc['row1', 'a']

# iloc - lets you find rows by their numbers
dataframe.iloc[0]
dataframe.iloc[0, 1]



dataframe2 = pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'], 
            index=['row3', 'row1', 'row']) 

dataframe + dataframe2


dataframe3 = pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'], 
            index=['row3', 'row1', 'row4']) 

dataframe + dataframe3

# Masking values
dataframe[dataframe['c']>5]
