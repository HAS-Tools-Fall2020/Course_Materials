# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl 

# %%
# Warm up

# Start with the following data frame
data_frame = pd.DataFrame([[1, np.nan, 2],
                            [2, 3, 5],
                            [np.nan, 4, 6]])
            

# 1) Use the function fill.na to fill the na values with 999
data_frame9= data_frame.fillna(999)

# 2) Turn the 999 values back to nas. See how many different ways you can do this
#Alcely
ans1=np.where(data_frame9==999, np.nan, data_frame9)

# Alexa 
data_frame9[data_frame9 == 999] = np.nan

# Laura
data_frame9 = data_frame.fillna(999)
data_frame9[data_frame.isnull()] = np.nan

# Taking advantage of the fact that nan's propagate when you do math on them 
data_frame9 = data_frame.fillna(999)
data_frame9 = data_frame9 + data_frame

#using the replace funciton - Jill 
data_frame9 = data_frame.fillna(999)
data_frame9.replace(999, np.nan)



# %%
# Matplotlib
#Making dummy datasets for plotting
x = np.linspace(0,10, 100)
y = np.sin(x)

#selecting a style to use -- this part is optional
plt.style.use('classic')

# easiest plot my data
plt.plot(x,y, color='red', linestyle='dashed')

# Also specify my style in shorthand
plt.plot(x,y, ':r')

# chaning axes etc
plt.plot(x,y, color='red', linestyle='dashed', label="sinx")
plt.plot(x, np.cos(x), label='cosx')
plt.xlim(-1,5)
plt.ylim(-2,2)
plt.xlabel('x')
plt.ylabel('sinx')
plt.title('my plot')
plt.legend()

#Rather than making a line plot I could do points
plt.plot(x, y, 'p', color="red")

# can combine with a line too
plt.plot(x, y, 'd', color= 'red', linestyle = 'solid')

# Can contorl the colors and styles of both the lines and the points
plt.plot(x, y, '-p', color= 'gray', 
        markersize=4, linewidth=1, 
        markerfacecolor='purple', markeredgecolor='black',
        markeredgewidth= '0.5')

# more sophisticated way to make scatter plots
# lets you change point properties according to variables
plt.scatter(x, y, marker='p')

#for example having the color change with the x value
plt.scatter(x, y, c=x, marker='p')

#Changing the size with some random value 
size=1000 * np.random.rand(len(x))
plt.scatter(x, y, c=x, s=size,  marker=',')


# %%
# A better way to setup your plot

# So far we have jsut done plt.xxxx 

#This line creates the plotting object we will use 
# Fig - is our overall figure -- use this to change things like plot dimension 
# ax - those are our graphs inside the figure
fig, ax = plt.subplots()
ax.plot(x,y, color='red', linestyle='dashed', label="sinx")
ax.plot(x, np.cos(x), label='cosx')
ax.set_xlim(-1,5)
ax.set_xlim(-1,5)
ax.set_ylim(-2,2)
ax.set_xlabel('x')
ax.set_ylabel('sinx')
ax.set_title('my plot')
plt.show()

# Can be more concise like this:
fig, ax = plt.subplots()
ax.plot(x,y, color='red', linestyle='dashed', label="sinx")
ax.plot(x, np.cos(x), label='cosx')
ax.set(xlim=(-1,5), ylim=(-2,2), xlabel='x', ylabel='sinx')

# Can make multi plots and refer to them using this appraoch 
# Another example witha biger grid
fig,ax = plt.subplots(2,2)
ax = ax.flatten() #necessary because of the structure of the ax 
# then we refer to these  objects when we want to do the plotting
ax[3].plot(x, np.cos(x), color='red')
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.sin(x))
ax[1].set_xlim(2,4)


# Another approach to naming your axes
#Accomplishing the same thing as the previous one
# but without the ax.flatten command
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2,2)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
ax3.plot(x, np.sin(x))
ax4.plot(x, np.cos(x))
plot.show()

fig.savefig('test.png')

