# Week 6: Python skills week 4
This week we are going to continue using Pandas DataFrames and we will be focusing on plotting with matplotlib.
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Complete the required training Activities by **next Tuesday**, get through as much as you can before class **Thursday**.
2. Submit your sixt streamflow forecast and assignment by **noon on Monday** following the instructions in the [ Forecast Assignment](#assignment).

___
<a name="resources"></a>
## References
- There are two images in the Cheet_sheets folder that covers the major plotting commands: `matlotlib_commands.png` and `matlotlib_commands2.png`

- You should also check out the [matplotlib website](https://matplotlib.org/) I especially recommend the [plot gallery](https://matplotlib.org/gallery/index.html) as a good place to get started.

- [Python Data Science Handbook Chapter 4](https://jakevdp.github.io/PythonDataScienceHandbook/) (sections of this chapter are also assigned in the required training).
___
<a name="training"></a>
## Required Training Activities
1.  Read the following sections from the [Python Data Science Handbook Chapter 4](ttps://jakevdp.github.io/PythonDataScienceHandbook/index.html). Note that this material is more detailed than the Earth Data Science Handbook. Its fine if you don't have time to work through every example they discuss but at a minimum you should read through these sections to be familiar with the concepts and know where to refer back to as needed:
  - [Simple Line Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html)
  - [Simple Scatter Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html)
  - [Visualizing  Errors](https://jakevdp.github.io/PythonDataScienceHandbook/04.03-errorbars.html)
  - [Histograms, Binning and Density](https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html)
  - [Customizing  Plot Legends](https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html)
  - [Customizing Colorbars](https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html)
  - [Multiple Subplots](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)
  - [Customizing  Matplotlib: Configurations and Stylesheets](https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html)
___
<a name="assignment"></a>
## Assignment 5: Pandas DataFrames
This week we will be building auotregressive models. Its  up to you whether you use your autoregresive model to actually make your forecast (you are welcome to continue guessing however you would like) but for your written assignment and the script you submit you must build a regression  model.

(*Remember* you should copy the starter code into your own repo and not work with it directly on the course materials repo).

#### Rules for this week:
- You must use the pandas dataframe *data* created at the top of the starter code as the basis for your analysis.

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy or pandas package to do so.  

- We will use sklearn to build auotregressive models. For this week stick only to the LinearRegression model in sklearn. Nothing fancier than that.

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### What to submit:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):

1. Your streamflow forecast values in the forecast repo in the csv with your name

2. Your assignment summary (see instructions below). This should be named with the same convention  as always `lastname_HWx.md` and saved in the submission folder of your homework repo.  It should include
  1. An appropriate header,
  2. A summary of your forecast and how you made it
  3. Answers to all of the questions listed below

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name `lastname_HWx.py`. **NOTE:** *Even if you have a free pass on the written assignment for this week you should still build AR models and graphs and submit your python script.*

Note: if you want to copy images into your markdown file for your submission I recommend installing the atom package ['markdown-image-assistant'](https://atom.io/packages/markdown-image-assistant#:~:text=atom%2Dmarkdown%2Dimage%2Dassistant,useful%20for%20notetaking%20in%20Atom.) Here are instructions for  [how to install a package in Atom](https://flight-manual.atom.io/using-atom/sections/atom-packages/)

#### Assignment
Review the starter code I provided to see how to build an autoregressive(AR) model. Then build your own model, you can modify my model in any way for example changing the number of time steps used for prediction or changing the testing and training data periods. The only rule is that you must make some modifications to make the model your own.

For your written assignment provide the following. Your submission should include at least **3** different types of plots (see the note at the end of the previous section for how to add these into your markdown file if you are not sure how to do that):

1. A summary of the AR model that you ended up building, including (1) what you are using as your prediction variables, (2) the final equation for your model and (3) what you used as  your testing and training periods. In your discussion please include graphical outputs that support why you made the decisions you did with your model.

2. Provide an analysis of your final model performance. This should include at least one graph that shows the historical vs predicted streamflow and some discussion of qualitatively how you think your model is good or bad.

3. Finally, provide discussion on what you actually used for your forecast. Did you use your AR model, why or why not? If not how did you generate your forecast this week?
