# Week 4: Python skills week 2
This week we will be expanding our python skills focusing on numpy arrays
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Complete the required training Activities by **next Tuesday**, get through as much as you can before class **Thursday**. Once again there is a lot of content this week so if you can start early  thats a good idea.
2. Submit your fourthstreamflow forecast and assignment by **noon on Monday** following the instructions in the [ Forecast Assignment](#assignment).

___
<a name="resources"></a>
## Refernces
- There is a *numpy-cheat-sheet.pdf* in the cheetsheets folder  that covers the major functions

- [Python Data Science Handbook Chapter 2](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) (sections of this chapter are also assigned in the required training).
___
<a name="training"></a>
## Required Training Activities
1. Work through the following sections of Intro to Earth Data Science covering python fundamentals and Python Environments.
  - **Chapter 12 Lesson 2**: [Directories and File Paths](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/work-with-files-directories-paths-in-python/set-working-directory-os-package/) *Review this lesson to understand how to set and check file paths in Python as we have been doing at the top of our scripts so far. Note that you don't need to make an 'earth-analytics' folder as they have in their examples you can just test this out with your homework directories.*
  - **Chapter 11 Lesson 1**: [Python Packages](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/use-python-packages/)
  - **Chapter 14: Numpy Arrays** (Note: for these lessons you can follow along with the datasets they download directly or you can try running the tests and examples on your datasets form the homework)
    - Lesson 1: [Intro to Numpy Arrays](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/numpy-arrays/)
    - Lesson 3: [Run Calculations and Summary Statistics on Numpy Arrays](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/numpy-arrays/run-calculations-summary-statistics-numpy-arrays/)
    - Lesson 4: [Slice (or Select) Data From Numpy Arrays](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/numpy-arrays/indexing-slicing-numpy-arrays/)

2. Read the following sections from the [Python Data Science Handbook](ttps://jakevdp.github.io/PythonDataScienceHandbook/index.html). Note that this material is more detailed than the Earth Data Science Handbook. Its fine if you don't have time to work through every example they discuss but at a minimum you should read through these sections to be familiar with the concepts and know where to refer back to as needed:
  - [The Basics of Numpy Arrays](https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html)
  - [Computation on Numpy Arrays: Universal Functions](https://jakevdp.github.io/PythonDataScienceHandbook/02.03-computation-on-arrays-ufuncs.html)
  - [Aggregations: Min, Max, and Everything in Between](https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html)
  - [Computation on Arrays: Broadcasting](https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html)
  - [Comparisons,Masks and Boolean Logic](https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html)


## Additional Recommended Training Activities
  1. Chapter 12 Lesson 4: [Glob](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/work-with-files-directories-paths-in-python/os-glob-manipulate-file-paths/) this lesson shows you how to use the glob function to generate lists of files within directories. This will come in handy later on.
  2. Chapter 11 Lesson 2: [Conda environments](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/use-python-packages/introduction-to-python-conda-environments/) and Lesson 3: [Installing Packages](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/use-python-packages/use-conda-environments-and-install-packages/)
___
<a name="assignment"></a>
## Assignment 4: Numpy Arrays
Similar to last week this week you will be generating your forecast by using conditional statements in python to look at the historical streamflow and make forecast. However this week we will be using numpy arrays rather than lists. You should write a script to subset the data however is most useful to you using conditionals and calculate the properties of this subset that will help you make your decision.  

You should use the HW4 starter code to see some examples of how to get started and for the setup of the variables you will need (*Remember* you should copy the starter code into your own repo and not work with it directly on the course materials repo).

#### Rules for this week:
- You must use the numpy array *flow_data* created at the top of the starter code as the basis for your analysis (i.e. don't use lists again)

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy package to do so.  

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission instructions:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):

1. Your streamflow forecast values in the forecast repo in the csv with your name

2. Your assignment summary (see instructions below). This should be named with the same convention  as always 'lastname_HWx.md' and saved in the submission folder of your homework repo.  It should include (1) an appropriate header, (2)answers to all of the questions listed below and (3) a summary of how you made your forecast decision.

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name 'lastname_HWx.py'

#### Assignment questions
In addition to providing a summary of the forecast values you picked and why include the following analysis in your homework submission. Note that questions 3-5 are the same as last weeks questions, however this time you are expected to calculate your answer using the numpy array rather than lists.

1. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.

2. Describe the variable flow_data:
  - What is it?
  - What type of values is is composed of?
  - What is are its dimensions, and total size?

3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?

4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)

5. How does the daily flow generally change from the first half of September to the second?
