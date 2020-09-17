# %%
import numpy as np 

# %%
#lists can be made up of anything and you can 
# mix and match
list2 = [True, 'test', 3.14, 4]
print(type(list2))

#but you have to loop over them to do things
#to every element in the list. It does not 
# do this automatically 
print([type(i) for i in list2])

#this does not work!
list2 + 7 

list3 = [2, 1, 3.14, 4]
#neither does this!
list3 + 7
#this does :) 
[i+7 for i in list3] 

# %%
#numpy arrays 

#This is almost the same as list3
# BUT we have turned it into an array
# and all of the values are not floats
array1 = np.array([2, 1, 3.14, 4])
print(array1)
print(list3)

print(array1.ndim)
print(array1.shape)
print(array1.size)

#this works! Because numpy arrays handle 
# broadcasting automatically. This is powerful
# see more details here: https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html 
array1 + 7 


#  %%
# Making Numpy arrays
#1d arrray of zeros where I am forcing it to be ints
arr_zero = np.zeros(10, dtype = int)
print(arr_zero.ndim)
print(arr_zero.shape)
print(arr_zero.size)

#1d arrray of zeros
#  where I let it default to float
arr_zero = np.zeros(10)
print(arr_zero)

# 2d arrray of zeros
arr_zero = np.zeros((3,5)) 
print(arr_zero)

# 2d arrray of sevens
arr_sev = np.zeros((3,5)) + 7
print(arr_sev)

# 2d arrray of sevens
arr_sev = np.ones((3,5)) * 7 
print(arr_sev)

# 2d arrray of sevens
arr_sev = np.full((3,5), 7.)
print(arr_sev)

#  %%
# Indexing numpy arrays

#staring with a 3 by 5 matix of 7s
test_array = np.ones((3,5)) * 7
print(test_array)

# Slicing in numpy arrays (really all of python)
# start:stop:step 
# default to start=0, stop= size of dimension, step=1
# axis0 = rows, axis1 = columns 


#grabbing out just the first row
test_array[0:1, 0:1 ] = 1.
print(test_array)

test_array[::2,  ] = 16.
print(test_array)

test_array[1, ::2 ] = 27.
print(test_array)

test_array[::, 4] = 30.
print(test_array)

#NOTE: we can still loop if we want
# But if you can avoid it do! 
# This is much much slower, and not the python way
for i in range(5):
    test_array[1,i]=75
print(test_array)


# %% 
# Universal Functions
# 'Vectorized' operations (that just means its doing the looping for you)
# If you can use universal functions, do

# This is applying the 7 to your whole array automatically 
test_array = test_array * 7 
print(test_array)

# Conditionals in numpy arrays are universal
# this automatically checks the condition for my entire
# array 
test_array < 115

# I can use this to grab out items automatically 
test_array[test_array < 115]

# We can aggregate things easily without loops
print(test_array)
np.max(test_array)
np.max(test_array, axis=0) # max for every column
np.max(test_array, axis=1) # max for every row
