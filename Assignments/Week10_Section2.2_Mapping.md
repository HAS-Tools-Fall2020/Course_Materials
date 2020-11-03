# Week 10: Mapping
This week we are starting are going to work with spatial vector data and explore mapping with Python.
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
1. [ Training Activities](#training)
1. [ Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Add your data download script to the `class_scripts/datasets` folder in the forecast repo **before Thursday**

2. Complete the required training activities **before next Tuesday**

3. Complete your forecast and submit your written summary in your repo by **noon on Monday**.

4. Submit your map to the google slides [here](https://docs.google.com/presentation/d/1Vx_A2FNrRM-08SPloBi5PI6AXIRu9lNdMyihj0gkxdE/edit?usp=sharing) and add your mapping script to the forecast folder by **noon on Monday**

___
<a name="resources"></a>
## Resources
#### Geopandas documentation
- [GeoPandas official documentation](https://geopandas.org/)
- [GeoPandas Examples Gallery](https://geopandas.org/gallery/index.html)

#### Spatial Datasets:
- [USGS Stream Gauges](https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder)
- [USGS Spatial Resources Site](https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products)
- [USGS Mapping Viewer](https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View)
___
<a name="training"></a>
## Required Training Activities
1. Chapter 2 of Intermediate to Earth Data Science: Vector Data in Python
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/): GIS in Python: Introduction to Vector Format Spatial Data - Points, Lines and Polygons
 - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/intro-to-coordinate-reference-systems-python/): Introduction to Coordinate Reference Systems
 - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/geographic-vs-projected-coordinate-reference-systems-python/): Geographic vs projected coordinate reference systems - GIS in Python

## Optional but Highly Recommended Activities
1. Chapter 3 of Intermediate to Earth Data Science: Processing Spatial Vector Data in Python
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/reproject-vector-data-in-python/): Reproject Vector Data
 - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/clip-vector-data-in-python-geopandas-shapely/): Clip Vector Data
 - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/dissolve-polygons-in-python-geopandas-shapely/): Dissolve Polygons
  - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/spatial-joins-in-python-geopandas-shapely/): Spatial Joins
  - [Lesson 4](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/vector-data-processing/missing-data-vector-data-in-python/): Missing Spatial Data

___
<a name="assignment"></a>
## Assignment 10: Map our watershed! (Due Monday noon)
This week you will still make a forecast as usual but we won't really be advancing our forecasting approach (you are of course welcome to if you would like though). Rather we are going to focus on making a spatial map of the watershed. As such the assignment has two parts:
 1. Submitting your forecast to the competition as usual and putting the python script you used to generate it in your submission folder of your repo
 2. Creating a map and submitting this to our class gallery and folder of scripts.

 NOTE: There is no markdown file required this week. Also note that your mapping script should be completely separate from your forecast script and will be submitted separately.  

### Part 1: Forecast
Note this part should be really fast for you. Just run your forecast as you have been doing and submit to the competition.

#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- You can use and of the datasets we have used so far in your analysis.

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission Instructions
This week you should submit 2 things in your `submission` folder
  1. Submit your forecast to the forecast repo as normal
  2. submit the script you used to generate your forecast to the submission folder of your repo `Latname_HW10.py`

### Part 2: Mapping
This is the part I would like for you to focus your efforts on. Your assignment is to make the **most visually appealing and informative map** you can of our watershed. Its completely up to you what layers you include and what the spatial extent of your map will be.

#### Requirements:
At a minimum you map must include:
- At least 4 layers
- A minimum of two vector data types (i.e. point, line, polygon)
- A legend

#### Submission Instructions
1.  Add your map to our map gallery [here](https://docs.google.com/presentation/d/1Vx_A2FNrRM-08SPloBi5PI6AXIRu9lNdMyihj0gkxdE/edit?usp=sharing) follow the instructions slide to see what you should include on your slide.
2. Submit the script you used to make your map to the `forecast repo` `class_scripts/maps`
  - Your script should be named `lastname_map.py`
  - Your script should be well commented, follow pep8 standards and be easy to follow.
  - **Do not** upload the datasets for your map to the repo. Its okay if your script wont run from the forecast repo because its pointing to files you have locally.
  - For each file you use include a comment with a link for where you got it.
  - This script should include only what is necessary to generate the map you submitted to the gallery. Don't include your forecast analysis here.
