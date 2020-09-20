# Week 5: Python skills week 3
This week we will be expanding our python skills focusing on Pandas DataFrames
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
2. Submit your fifth streamflow forecast and assignment by **noon on Monday** following the instructions in the [ Forecast Assignment](#assignment).

___
<a name="resources"></a>
## References
- There is a *pandas-cheat-sheet.pdf* in the Cheet_sheets folder  that covers the major functions

- [Python Data Science Handbook Chapter 2](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) (sections of this chapter are also assigned in the required training).
___
<a name="training"></a>
## Required Training Activities
1. Work through Chapter 15 of Intro to Earth Data Science covering Pandas DataFrames.
  - **Lesson 1**: [Pandas DataFrames Intro](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/)
  - **Lesson 2**: [Importing Data into DataFrames](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/import-csv-files-pandas-dataframes/) (NOTE: you can see in this exercise that the approach is the same that I have applied for the starter codes. You can use the example dataset they provide or just use the ones we have downloaded for homework already)
  - **Lesson 3**: [Recalculate and Summarize](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/run-calculations-summary-statistics-pandas-dataframes/) (Note: Same as the previous section you can do these exercises with they data they recommend or practice applying the same functions to the data you already have)
  - **Lesson 4**: [Selecting Data from DataFrames ](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/indexing-filtering-data-pandas-dataframes/) *This lesson is longer but very  important, make sure you walk through all of this.

2. Read the following sections from the [Python Data Science Handbook Chapter 3](ttps://jakevdp.github.io/PythonDataScienceHandbook/index.html). Note that this material is more detailed than the Earth Data Science Handbook. Its fine if you don't have time to work through every example they discuss but at a minimum you should read through these sections to be familiar with the concepts and know where to refer back to as needed:
  - [Introducing Pandas Objects](https://jakevdp.github.io/PythonDataScienceHandbook/03.01-introducing-pandas-objects.html)
  - [Data Indexing and Selection](https://jakevdp.github.io/PythonDataScienceHandbook/03.02-data-indexing-and-selection.html)
  - [Operating on Data in Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.03-operations-in-pandas.html)
  - [Handling Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html)

___
<a name="assignment"></a>
## Assignment 5: Pandas DataFrames
We are still in the exploratory data phase. This week you will be using Pandas to look  at the historical streamflow and make your forecast. You should write a script to subset the data however is most useful to you for your decision making. The HW5 starter code will help you get your DataFrame setup and after that it is up to you.

(*Remember* you should copy the starter code into your own repo and not work with it directly on the course materials repo).

#### Rules for this week:
- You must use the pandas dataframe *data* created at the top of the starter code as the basis for your analysis (i.e. don't use lists or numpy arrays, take advantage of all of the handy pandas functionality!)

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy or pandas package to do so.  

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission instructions:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):

1. Your streamflow forecast values in the forecast repo in the csv with your name

2. Your assignment summary (see instructions below). This should be named with the same convention  as always 'lastname_HWx.md' and saved in the submission folder of your homework repo.  It should include
  1. An appropriate header,
  2. A summary of your forecast and how you made it
  3. Answers to all of the questions listed below

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name 'lastname_HWx.py'

Note: if you want to copy images into your markdown file for your submission I recommend installing the atom package ['markdown-image-assistant'](https://atom.io/packages/markdown-image-assistant#:~:text=atom%2Dmarkdown%2Dimage%2Dassistant,useful%20for%20notetaking%20in%20Atom.) Here are instructions for  [how to install a package in Atom](https://flight-manual.atom.io/using-atom/sections/atom-packages/)

#### Assignment questions
In addition to providing a summary of the forecast values you picked and why include the following analysis in your homework submission. Note that questions 3-5 are the same as last weeks questions, however this time you are expected to calculate your answer using the numpy array rather than lists.

1. Provide a summary of the data frames properties.
  - What are the column names?
  - What is its index?
  - What data types do each of the columns have?

2. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.

3. Provide the same information but on a monthly basis. (Note: you should be able to do this with one or two lines of code)

4. Provide a table with the 5 highest and 5 lowest flow
values for  the period of record. Include the date, month and flow values in your summary.

5.  Find the highest and lowest flow  values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.

6. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other  value and report the date and the new window you used
