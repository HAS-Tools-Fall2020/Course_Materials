# Week 1: GitHub, Command Line, and our first forecast

This readme has the instructions for the first week of class. Every week you will find a readme similar to this outlining the activities and instructions you will need as well as the weekly forecasting assignment.

____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Setup Instructions](#github)
  - [ GitHub Install](#githubinst)
  - [ Repo Cloning](#repo)
  - [ Text Editor](#atom)
1. [ Homework Setup](#classroom)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Follow all of the instructions in the [ Setup Instructions](#setup) to install the necessary software and get the course repo's cloned. You should be able to do all of the steps except the homework repo **before class on Thursday**.
1. Email Laura your GitHub user name by **Wednesday at 5pm**.
2. Complete the required GitHub and command line tutorials in the [training activities](#training) section before next week.
3. Accept the homework assignment invitation to create your own homework repo.
3. Submit your first streamflow forecast and assignment by **noon on Monday** (see forecast submission instructions).

___
<a name="setup"></a>
## Setup Instructions
<a name="githubinst"></a>
#### 1. Setup account and install Github and GitHub Desktop
  - Register for account on GitHub: <https://github.com/>
  - Check if you have GitHub installed and if not install it.  Directions for both Windows & Mac [here](http://happygitwithr.com/install-git.html). Windows users should follow Option 1 in 6.2. Mac users can follow Option 1 in 6.3.
    - *Note:* If you are a Windows user make sure you also install [GitBash](https://www.atlassian.com/git/tutorials/git-bash) as is noted in the instructions.
  - Setup options in Git. If you have a Mac, you can go to the terminal (Applications -> Utilities -> Terminal) as shown above. If you have a Windows, open Git BASH, which you should have downloaded.  You will need to  setup you [username](https://help.github.com/en/github/using-git/setting-your-username-in-git) and your [email](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address)
  - Generate a SSH key so you don’t need to enter your password every time you interact with GitHub. Instructions for this can be found [here](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
  - Install [GitHub Desktop](https://desktop.github.com/) to manage your GitHub repos. This way you won't need to use command line for committing and pushing changes.

<a name="repo"></a>
#### 2. Clone the course repos
I recommend you start by creating a directory for this class where you will keep all of your repos.
- *GitHub Desktop Approach*
  - Go to the Course Materials Repo on the [GitHub organization](https://github.com/HAS-Tools-Fall2020) for this course and click on the green 'code' button
  - When you do this you should see an 'Open in Desktop' option  this will create a clone and open it into GitHub Desktop directly for you.
  - In GitHub Desktop, you should see that the URL to the GitHub repo has been pasted into the *Repository URL* box. Below this you can select what local folder this will clone to with the **Choose** button.
  - Once you push **clone**, GitHub Desktop shows a screen that says 'Cloning (name of the repo)' with a progress bar. When it completes, you should be able to see the repo in the top left hand corner under the words *Current repository*. The repo should also be visible in your course folder as a new folder.

- *Command Line Approach*
    - Make a directory for this class wherever you would like to have it on your computer
    - Open a terminal window and navigate to your course directory (you can do this using the commands cd and pwd)
    - Clone the main course materials repo: `git clone [ADD SSH]`
    - *if your ssh keys aren't setup you can also clone it like this* `git clone [ADD LINK]`

<a name="atom"></a>
#### 3.	Install the **Atom text editor**
 - This is a great text editor that has GitHub integration.You can install it for Mac or Windows [here](https://atom.io/)

___
<a name="classroom"></a>
## Getting Started - Homework and GitHub Classroom
1. Once I have your GitHub IDs, I will give you a link to an assignment, either through email or the class page. You should follow the instructions for getting the homework repository set up included in this invitation. You should now have a repository for this homework.

      *Note:* After you accept an assignment for the first time, we will send you an invite to join the classroom organization as a member. **Please accept this.** You will probably get an email with the invitation, but you should also see a link at the top of your main GitHub page.

2. Enter the homework repository on GitHub the same as you did with the previous two.  Click “code”, and make sure it says “Clone with SSH” in bold in the top left of the pop-up box. If not, click on the blue “Use SSH” and click 'open with GitHub Desktop' (you can also copy the link to the clipboard and use the command line approach described above).

      *Note:* If you received an error in the above steps, you may have to clone with HTTPS instead of SSH. You can do this by again clicking on the "Clone or Download" button in the repository page, then clicking "Use HTTPS" in the top right of the pop-up box. Now copy the link and repeat this step.

___
<a name="training"></a>
## Required Training Activities
1. Read and do the exercises of Intro to Earth Data Science **Chapter 2** on Bash and Shell
  - [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/) Intro to Bash
  - [lesson 2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/bash-commands-to-manage-directories-files/) Bash Commands
2. Read **Chapter 7** Intro to Earth Data Science on the basics of GitHub
  - [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/) What is Version Control?
  - [Lesson 2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/fork-clone-github-repositories/) Get files from GitHub
  - [Lesson 3](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/git-commands/) Git Commnad for Verion control
  - [Lesson 4](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/git-undo-local-changes/) Undo local changes with Git
2. Do this [intro to GitHub tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners).
3. After you have practiced Git command from command line check out how you can do some of the same things with [Github Desktop](https://www.softwaretestinghelp.com/github-desktop-tutorial/)

## Additional Training activities
If you want more practice check these out:
1. More command line practice: [Chapter 3 of The Unix Workbench](https://seankross.com/the-unix-workbench/command-line-basics.html#navigating-the-command-line) try the exercises in sections 3.1-3.4. Note that for Mac users you will use **Terminal** and for Windows users you should use **Git Bash** to complete these exercises.
2. Even more command line practice:  [crash course](https://learnpythonthehardway.org/book/appendixa.html)
3. Another [Github tutorial](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6) with practice exercises
4. A GitHub tutorial setup as a [game](https://learngitbranching.js.org/)


___
<a name="assignment"></a>
## Assignment 1: First Forecast
This week you will generate your first streamflow forecast. The rules for this forecast are simple you will use only Excel to generate your forecasts and the most complicated mathematical operation you can do is take an average. You should make your forecast by simply looking at the historical streamflow and making your best guess of what you think it will be in the future based on whatever logic you want (no fancy calculations!). Don't worry we will get more sophisticated from here, but this week we start basic.

#### 1. Download the stream gauge observations to your homework repo
 The USGS NWIS website has all of the USGS maintained observation sites in the country. Go to their main [website](https://waterdata.usgs.gov/nwis) or their [mapper](https://maps.waterdata.usgs.gov/mapper/) and download the following daily streamflow data for station  *09506000 Verde River Near Camp Verde* using the following parameters:
   - Daily Data
   - Parameter 00060 Discharge (mean)
   - Start date = 1989-01-01
   - End date = Today
   - Select 'tab separated'

- The data will load in a new tab of your browser. Right click and save it as a *streamflow_week1.txt* file in the *data* folder of your **homework repo**.

### 2. Import the data into Excel and calculate the average
- Open a new Excel workbook and copy and paste the text file into it.
- Use the *text to columns* option in the *data* menu and select *delimited* and by *tabs* to separate the data into columns (If tab doesn't work you can also delimit by *space*)
- Save your workbook as *streamflow_week1.xlsx* in the *assignment_1* folder.
- Read the documentation at the top of the file to understand the format of the data you have downloaded.
- Look at the streamflow values and decide what your forecasted flows will be (remember you can't do any math here other than taking an average, the idea here is just to take a look at the historical flow and use your own judgement to make a forecast).  You need to make three forecasts all of which should be expressed as average daily flow in cfs (1) flow next week, (2) flow two weeks from now, (3) flow for every week of the semester.

### 5. Submit your first forecast to the competition
- Clone the Forecasting repo from our course organization website on GitHub: https://github.com/HAS-Tools-Fall2020
- To avoid conflicts make sure your local repo is up to date before you submit your forecast. You can do this with they synch option in github desktop or by doing `git pull`. Refer to the training materials for more information if you forget how to do this.
- Find the csv with your last name in the *forecast_entries* folder and enter your forecasts. Enter your forecasts on the row for foercast #1. A few notes:
    - Make sure you just enter numbers (i.e. enter 5 not 5 cfs)
    - Don't convert the file to an xlsx file keep it as a csv.
    - the one '1week' and '2week' refers to your forecasts for next week and the following week. The 'lt_weekx' columns are for your forecasts for every week of the semester. You can refer to the forecasts_dates files in the Forecast repo for more details.
- Save your changes, commit them, and push your changes. Again you can do this in GitHub desktop or  on command line.

### 5. Submit your first forecast homework assignment
In addition to submitting your numerical forecasts to the forecast competition you also need to submit a description of your forecast through your homework repo. This is what I will be grading for credit.

- Create a file named lastname_HW1.md in the **submission** folder of your homework repo. The easiest way  to do this is just to create a new file in atom.

- Include a header in your file that includes, your name, the date, and the assignment number

- Write a few sentences describing the forecast you made and rational for making it.  Note that we aren't doing anything fancy this week so your rational can be very simple, I'm not looking for a lot of text or any external research. This is really just to practice getting files submitted on GitHub.
