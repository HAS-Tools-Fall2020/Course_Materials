
# %%
import numpy as np

# %%

# Ice Breaker Activity 
#1a.  Create a 3X3 matrix with values ranging from 2-10  
# Laura
x1=np.arange(2,11).reshape(3,3)
print("1a matrix")
print(x)

#Richard
print(np.array(range(2,11,1).reshape(3,3))

#diana 
Ex_1= np.array([(2,3,4),(5,6,7),(8,9,10)])
print(Ex_1)

#1.b  Make a matrix with all of the even values from 2-32
#Ty
xb=np.reshape(np.arange(2,33,2),(4,4))

# -1 means you dn't need to know how many rows you have it will fill it in
x=np.reshape(np.arange(2,33,2),(-1,4))

# taking values counting by 1 and just multiplying the matrix by 2 would give
# you evens
x2 = x1 *2


# 1.c Make a matrix with all of the even values from 2-32
# But this time have the values arrange along columns rather than rows
xc=np.reshape(np.arange(2,33,2),(4,4), order='F')
xd=np.arange(2,33,2).reshape(4,4, order='F')

# BONUS:
# Create the same 3x3 matrix with value ranging from 2-10 
# as you did in part a but this time do so by combining 
# one 3X1 matrix and one 1X3 matrix
x=np.arange(2,5,1) 
y = np.arange(0,7,3).reshape(3,1)
z= x+y

