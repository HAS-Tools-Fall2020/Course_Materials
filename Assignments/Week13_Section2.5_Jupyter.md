# Week 13: IPython Notebooks
This week we are going to convert our scripts to IPython notebooks with Jupyter.

____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Training](#training)
1. [ Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Review the training activities.

2. Submit the following **2 things** by **noon on Monday**:
 - Your forecast to the forecast Precipitation
 - Your Jupyter notebook in the submission folder

___
<a name="references"></a>
## References and resources
  - Jupyter_Notebook_cheat_sheet.pdf in the cheat sheet folder
  - [Pros and cons of using Jupyter](https://medium.com/better-programming/pros-and-cons-for-jupyter-notebooks-as-your-editor-for-data-science-work-tip-pycharm-is-probably-40e88f7827cb)
  - [A Gallery of interesting Ipython Notebooks](http://pythonic.zoomquiet.top/data/20171227234039/index.html)
  - [Plotly Phython Notebook Gallery](https://plotly.com/python/v3/ipython-notebooks/)

___
<a name="training"></a>
## Required Training Activities
Intro to Earth Data Science Chapter 3: Jupyterfor Python
1. [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/) Intro to Jupyter
1. [Lesson 2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/get-started-with-jupyter-notebook-for-python/) Jupyter Notebooks for Python
1. [Lesson 3](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/code-markdown-cells-in-jupyter-notebook/) Code and Markdown Cells
1. [Lesson 4](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/manage-directories-jupyter-dashboard/) Manage Directories Using Dashboard
1. [Lesson 5](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/manage-jupyter-notebook-files/) Manage Jupyter Notebooks
1. [Lesson 6](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/jupyter-python/jupyter-notebook-shortcuts/) Keyboard shortcuts

___
<a name="assignment"></a>
## Assignment 13: IPython notebook
This week you will be submitting your second and final graded code for the semester. This time rather than submitting a readme and a python script though you will just be submitting an **IPython otebook**.

You will be graded following the same evaluation metrics used for your last script. You should focus on making sure your code is well organized, well documented and easy to follow.

Your submission should be unique to you but you are welcome to use and build on what you did in your group script and to collaborate with others.

#### Coding assignment
As noted above your assignment this week is to pull together a complete forecast analysis in a Jupyter notebook.
- Its up to you how  your organize your script and what documentation you provide but the goal is to create a notebook that anyone could pick up and follow what you are doing and what the outcomes are.
- Its also completely up to you what datasets you use in your analysis, you can stick just to the stream gauge even as long as you justify your choices.
- All graphs and maps should be accompanied with discussion. Don't include all the graphs you have ever made here just the ones you want to show and discuss.

At a minimum your notebook must include:
1. Text explaining the overall purpose of the notebook
2. An explanation of how you are generating forecasts and why
3. A discussion of how you have done so far and how your foreasting has evolved over time.
4. A map
5. At least two different kinds of plots (i.e. line graph, scatter plot, histogram, boxplot)
6. One function (Note this can be in a separate file and not  in the notebook directly if you don't want)
7. A printed statement with your 1, 2 and 16 week forecasts.

#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- You can use and of the datasets we have used so far in your analysis

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission Instructions
1.  Submit your forecast to the forecast competition following normal procedures.
2. Submit your Jupyter notebook to your submission folder `Latname_HW13.ipynb`
  - Your Jupyter notbook should be setup so that I can run it from the submission folder without making any changes
  - Its fine if you source additional python script(s) that contain your functions as long as the paths are setup appropriately for me to run.
  - All data that you are using should be included in your repo with the paths fixed or it should be downloaded directly from within your script using API calls. Again totally up to you as long as I can run your notebook without downloading anything myself or updating paths.
