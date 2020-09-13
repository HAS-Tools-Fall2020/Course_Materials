# Week 3: Python setup and our first Python forecast
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Complete the required training Activities by **next Tuesday**, get through as much as you can before class **Thursday**
2. Submit your third streamflow forecast and assignment by **noon on Monday** following the instructions in the [ Forecast Assignment](#assignment).

___
<a name="resources"></a>
## Resources
Check out the following guides in the **cheatsheets** folder to help remind you of the content we cover this week:
  - python_basics.pdf
  - python_conditionals.pdf

___
<a name="training"></a>
## Required Training Activities
- Work through the following sections of Intro to Earth Data Science covering python fundamentals and Python Environments. There are quite a few this week so I recommend you start early. I recommend starting a separate .py file for working through the lessons and typing the commands as you go.
- **NOTE:** For some of the activities in chapter 17 you will need to install the package **earthpy** you should do this from terminal. First make sure that you have your *hastools* environment activated before you do the install by typing `conda activate hastools`  then you can install the package by typing `pip install earthpy`. 
  - **Chapter 10: Getting started with Python variables and Lists**
    - Lesson 3: [Lists](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/lists/)
    - Lesson 4: [Operators](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/python-operators/)
    - Lesson 5: [Exercises](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/python-fundamentals-exercises/)
  - **Chapter 17: Conditional Statements**
    - Lesson 1: [Intro to conditional statements](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/conditional-statements/)
    - Lesson 2: [Alternative and multiple conditions](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/conditional-statements/alternative-multiple-conditions/)
  - **Chapter 18: Loops**
    - Lesson 1: [intro to loops](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/) (NOTE: for this one you can focus mainly on the for loop section. Don't worry about the while loop section.
    - Lesson 4: [list comprehensions](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/list-comprehensions)

___
<a name="assignment"></a>
## Assignment 3: Lists and conditionals
This week you will be generating your forecast by using conditional statements in python to look at the historical streamflow and make forecast. You should write a script to subset the data however is most useful to you using conditionals and calculate the properties of this subset that will help you make your decision. You should use the HW3 starter code to see some examples of how to get started and for the setup of the variables you will need (*Remember* you should copy the starter code into your own repo and not work with it directly on the course materials repo).

#### Rules for this week:
- You can calculate min, max, mean and standard deviation but nothing more complicated than that at this point
- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )
- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission instructions:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):
1. Your streamflow forecast values in the forecast repo in the csv with your name
2. Your assignment summary (see instructions below). This should be named with the same convention  as always 'lastname_HWx.md' and saved in the submission folder of your homework repo.  It should include (1) an appropriate header, (2)answers to all of the questions listed below and (3) a summary of how you made your forecast decision.
3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name 'lastname_HWx.py'

#### Assignment questions
In addition to providing a summary of the forecast values you piked and why include the following analysis in your homework submission.
1. Describe the variables `flow`, `year`, `month`, and `day`. What type of objects are they, what are they composed of, and how long are they?
2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
4. How does the daily flow generally change from the first half of September to the second?
