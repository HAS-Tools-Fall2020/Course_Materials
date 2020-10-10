# Week 8: Python skills week 6
This week is the grand finale of our first python section. And the last week where you will be restricted to only the historical streamflow data.  This week we will learn about time series data and you will revise your code from last week to submit as your first graded script.
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Revise your code following the comments you got from your partner and submit your final draft as well as a write up by **noon on Monday**  

2. Submit your forecast to the competition by **noon on Monday**.

3. Fill out the midcourse evaluation before class **next Tuesday**. You can access it [here](https://forms.gle/p33ioc9RE3oiF3yZ8)

___
<a name="resources"></a>
## Resources
- Official datetime documentation in the Python library [docs](https://docs.python.org/3/library/datetime.html)
- Chapter 3 of Python Data Science Handbook [Working with timeseries](https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html)

___
<a name="training"></a>
## Required Training Activities
1. Chapter 1 of Intermediate to Earth Data Science: Time Series Data in Python
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/introduction-to-time-series-in-pandas-python/): Intro to Timeseries
  - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/): Dates in Python
  - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/subset-time-series-data-python/): Subset Time Series Data
  - [Lesson  4](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/resample-time-series-data-pandas-python/): Resample Time series Data
  - [Lesson 5](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/): Customize Dates on Plots

- Optional: do the [Time series challenge](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/time-series-exercise/) from this chapter.

___
<a name="assignment"></a>
## Assignment 8: Final graded script from section 1
This week you will be submitting your final script for Section 1 of the course. This script will be worth **6 points** and will be graded by me following the same rubric you used for your peer review. Follow the instructions below to see the requirements and submission instructions.

#### Forecast Rules for this week:
- You must use the pandas dataframe *data* created as the basis for your analysis.

- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.


#### Scripting Assignment
- This week you should revise your script from last week. It's up to you how much you would like to change it depending on the comments you received.
- Refer to last weeks assignment for the functionality requirements.
- The only additional functionality you need in your script for this week relative to last week is that you should generate the 16 week forecasts also.  
- I should be able to run your script from the submission folder you create *without making any changes to it.*
- Your script should be well commented and organized so that I can follow what is going on.
- I will evaluate your script using the same rubric and questions that we used for the peer review (i.e. following the `code_review_rubric.md` in the `starter_codes` folder).

#### Written Assignment
Your submission folder should include a `Readme.md` file that contains the following:
1. A brief summary of the AR model you built and why. Use whatever graphs you find helpful.
2. An explanation of how you generated your forecasts and why (i.e. did you  use  your AR model or not?)
3. A brief summary of what you got out of the peer evaluation. How did you make your script better?
4. Describe the part of your script that you are most proud of and why.

#### Submission Instructions
- In your `submission` folder create a directory called `Code_Submission1`.
- Put your final python script in this folder named `LastName_HW8.py`
- Double check before you submit that the script can run directly from this folder and that you have the path to your data and functions setup correctly so I can run it without making any adjustments
- Add a file called `ReadMe.md` that includes your answers to the written assignment.
