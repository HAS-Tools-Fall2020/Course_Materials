# Week 11: Hierarchical Data
This week we are going to work with NetCDF data.

____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Training](#training)
1. [ Data Access Instructions](#data)
1. [ Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Review the training activities. If you can read through the required activities by Thursday that will be very helpful. We will walk through the details of Lesson 3 together in class.

2. Submit the following **3 things** by **noon on Monday**:
 - Your forecast to the forecast Precipitation
 - Your markdown and python script to the submission folder of your Precipitation
 - Your slide to the NetCDF gallery [here](https://docs.google.com/presentation/d/1aczDtIH-v7jttA3_CvKQBSiWCfeEyV6LnpbiYbzzPaY/edit?usp=sharing)

___
<a name="training"></a>
## Required Training Activities
1. [Section 6 Intro](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/) Hierarchichal Data Formats
2. [Chapter 13: Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/intro-to-climate-data/): Intro to NetCDF4
3.  [Chapter 13: Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/use-netcdf-in-python-xarray/): Working with NetCDF in Python (note its fine if you use our example dataset to work through this rather than downloading theirs)

## Optional Training Activities
Even if you don't have time to do these this week I recommend you scroll through these sections quickly just so you know what is here for future reference
1. [Chapter 12: HDF4](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/intro-to-hdf4/): Remote sensing data
2. [Chapter 13: Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/intro-to-MACAv2-cmip5-data/): Intro to climate  data
3. [Chapter 13: Lesson 4](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/subset-netcdf4-climate-data-spatially-aoi/): Spatial Subset Climate  data
4. [Chapter 13: Lesson 5](https://www.earthdatascience.org/courses/use-data-open-source-python/hierarchical-data-formats-hdf/summarize-climate-data-by-season/): Making seasonal summaries
___
<a name="data"></a>
## Data Access Instructions
This week we will be working with netcdf data from two sources. These instructions will help you download the datasets You don't need to do both of these if you don't want you can just pick one thing to download.

NOTE: For downloads I suggest a bounding box of:
- 34N to 36N
- 247E to 249E (or -113 to -111)

### 1. Historical Reanalysis data
A wide array of gridded climate data is available through the NOAA: Physical Sciences Lab. You can learn more about that [here](https://psl.noaa.gov/data/gridded_help/howtosub.html). We are going to download some NCEP re-analysis data in this example but you can download other datasets if you would like.
- Go to the [search page](https://psl.noaa.gov/cgi-bin/db_search/SearchMenus.pl) and select `NCEP Reanalysis Daily Averages` and `Precipitation Rate`
- Click `make a subset` and input the spatial region and time period you are interested in. Given the size of the dataset I suggest you limit your time period to after 2000.
- Click `create subset` and when you get to the page with the graph select `FTP the data` and finally select `FTP a copy of the data` to start the download you should see a nc file downloaded for you (note the file size limit, if you exceed this you might need to select a smaller subset)


### 2. Precipitation forecast data
In addition to historical reanalysis data we can also access forecast data through the UCAR research data archive:
- If you don't have one already, create an account on the [Research Data Archive](https://rda.ucar.edu/index.html?hash=data_user&action=register) (NOTE: It may take several hours and up to 2 business days for your registration to be accepted so plan accordingly)

- [Sign in](https://rda.ucar.edu/index.html?hash=data_user&action=signin)to the Research Data Archive

- Once you are signed in click on `Home` tab search for `NCEP GFS 0.25 Degree Global Forecast Grids Historical Archive`.

- On the `Data Access` tab, use the `Get a subset` tool. Use the following options to request a custom subset:
  - Initialization time: yesterday @ 0000 to yesterday +14 days @ 0000
  - Parameter: Total Precipitation
  - Output Format: Convert to netCDF
  - For Gridded Product: select all variables
  - Spatial selection: use a bounding box (see box info above)
  - Use the web download option. Up to you if you use gzip or not but note that if you use gzip you will need to unzip the file when you receive it.

- Now you can **submit** your request.
- When your request is processed you will receive the email from RDA with your subset of precipitation forecast data. You can then download the data using the python pre-populated script the provide you or by clicking on the tar file in the web link they send you to. If you do the Python script option you will need to run that python script (enter RDA account password).

- Once you have the tar file downloaded you will need to use the following set of commands to decompress and unzip the files (NOTE: if your file wasn't zipped you can just untar and skip the gunzip step):
  ```
  tar -xvf filename.gz.tar
  gunzip filename.gz
  ```
  This should give you the netcdf file with the .nc extension: **filename.nc**

___
<a name="assignment"></a>
## Assignment 12: Reading NetCDF data
This week your assignment is to add one additional dataset to your analysis that comes from a NetCDF. The dataset can be whatever you choose but it must be read from a NetCDF file and it can't be exactly the example I provided in the starter code.

There are two starer codes for this week `Week12_Forecast_Netcdf_starter.py` and `Week12_Reanalysis_Netcdf_starter.py` You can use these as your starting points showing you how to extract data  from different NetCDF files. The netcdf files referenced by these scripts are included in a `data` folder in the `start_codes` folder.

Note that one of the scripts includes a map at the bottom but you are not required to do mapping this week if you don't want. See the data access instructions above for instructions on accessing the two datasets used in the


#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- You can use and of the datasets we have used so far in your analysis

- **In addition** to the historical observed streamflow you must incorporate one additional non-streamflow time series into your analysis that comes from a netCDF.

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

- As always you are always welcome to discard your model and guess the streamflow however you would like.

#### Submission Instructions
- Submit your forecast to the forecast competition following normal procedures.
- This week you should submit 2 things in your `submission` folder
  1. `Latname_HW12.py`: Your python script with your full analysis
  2. `Lastname_HW12.md`: Your written assignment

#### Coding assignment
- As noted above you need to add an additional dataset to your analysis. This can be a historical time series that you add to your regression model or it can be a single forecast value that you incorporate into your predictions.
- The only requirement is that this dataset must come from a NetCDF file.
- Its up to you how this data gets aggregated/extracted as long as you have a way to incorporate it into your workflow.

#### Written Assignment
Your submission folder should include a `Readme.md` file that contains the following:
1. A brief summary of the how you chose to generate your forecast this week.
2. A description of the dataset you added
  - What is the dataset? Why did you choose it?
  - What is the spatial and temporal resolution and extent of the data ?
  - Where did you get the data from?
  - What was your approach to extracting and aggregating it into something useful to you?
3. A plot of the dataset you added. This can be a timeseries, map, histogram or any other plot that you think is a good summary of what you added.
4. Finally add your plot and a  brief summary of what you did to our slide deck for this week [here](https://docs.google.com/presentation/d/1aczDtIH-v7jttA3_CvKQBSiWCfeEyV6LnpbiYbzzPaY/edit?usp=sharing)
