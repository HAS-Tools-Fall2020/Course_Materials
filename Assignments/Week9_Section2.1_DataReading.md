# Week 9: Reading data and APIs
This week we are starting our next section where we are going to consider alternative data formats to the single streamflow timeseries we have been working with so far. For starters this week will will learn about data APIs and how to get and access additional point data.
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Setup Instructions](#instructions)
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
- Official documentation on IO options available with [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)
- Official documentation on IO options available with [Numpy](https://numpy.org/devdocs/reference/routines.io.html)
- Importing data section of the Pandas cheat sheet
- [Python Dictionaries Guide](https://www.w3schools.com/python/python_dictionaries.asp)
___
<a name="training"></a>
## Required Training Activities
1. Chapter 15 of Intermediate to Earth Data Science: APIs
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/apis-in-python/): Intro to APIs
 - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/intro-to-json/): Introduction to JSON Data in Python
 - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/use-JSON-in-python/) : Introduction to Working With JSON Data in Open Source Python

2. Review this quick overview of [Python Dictionaries]([Python Dictionaries Guide](https://www.w3schools.com/python/python_dictionaries.asp))
___
<a name="instructions"></a>
## Setup instructions
To use the weather station data you will need to sign up for a token with the Mesonet database.

1. Read the getting started instruction on the mesonet website [here](https://developers.synopticdata.com/mesonet/v2/getting-started/)
2. [Sign up](https://developers.synopticdata.com/signup/). Fill out the required fields. When this is successful you should get to a page that gives you a token and you should also receive a confirmation email with your token. You can always log back into your account to get this token again or to generate more by going to [this site](https://myaccount.synopticdata.com/)
3. Copy and paste your token somewhere for safe keeping, this is what you will use for the Python starter script

___
<a name="assignment"></a>
## Assignment 9: Reading point data with APIs
This week your assignment is to add one additional dataset to your analysis using an API to access the data. The dataset can be whatever you choose but it must be a time series not a spatial dataset and it **can't** be another USGS stream gauge.

The starter code file for this week has examples of accessing data from DayMet and from MesoNet. You can use these as your starting points, or you can get any time series data you would like.

You might want to check out the following links for stations and datasets:
- [USGS Basin summary](https://water.usgs.gov/lookup/getwatershed?15060202/www/cgi-bin/lookup/getwatershed)
- [NOAA station mapper](https://www.ncdc.noaa.gov/cdo-web/datatools/findstation)

#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- **In addition** to the historical observed streamflow you must incorporate one additional non-streamflow time series into your analysis.

- All of the data you use must be accessed using a URL rather than reading it locally.

- This can be any time series you would like but it must be a time series for a single spatial location (i.e. not gridded data)

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.


#### Submission Instructions
- This week you should submit 2 things in your `submission` folder
  1. `Latname_HW9.py`: Your python script with your full analysis
  2. `Lastname_HW9.md`: Your written assignment

#### Coding assignment
- As noted above you need to add an additional time series to your analysis
- You should be accessing this time series using a Rest API (i.e. with a URL)
- You must be able to extract the time series of data and create a plot of weekly aggregated values.
- You can add this as an additional variable to your linear regression model or you can generate your forecast without the regression model this week. Up to you.

#### Written Assignment
Your submission folder should include a `Readme.md` file that contains the following:
1. A brief summary of the how you chose to generate your forecast this week.
2. A description of the dataset you added
  - What is the dataset? Why did you choose it?
  - What location have you chosen?
  - Where did you get the data from?
  - What was your approach to accessing it?
3. A plot of your additional time series along with your streamflow time series.
