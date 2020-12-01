# Week 15: Computing resources
This week we are going explore how you can access and use computing resources beyond your laptop.
___
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#references)
1. [ Instructions](#instructions)
1. [ Assignment](#assignment)
___
<a name="todo"></a>
## To Do List
1. Modify your forecast script so it is easy to transport.

2. Run your forecast script on two locations other than your laptop

2. Submit your homework assignment and your **final** forecast by **noon on Monday**:

___
<a name="references"></a>
## References and resources
**UA HPC**
- Getting started
  - [Quick Start Guide](https://public.confluence.arizona.edu/display/UAHPC/Ocelote+Quick+Start)
  - [Training Page](https://public.confluence.arizona.edu/display/UAHPC/Training+Resources)
  - [Setting up Python on UAHPC](https://public.confluence.arizona.edu/display/UAHPC/Using+and+Installing+Python)
  - [Tutoral on running Jupyter Notbooks on UAHPC](https://public.confluence.arizona.edu/display/UAHPC/Jupyter+Notebook+-+Python)

- Allocations and storage limits
  - [Compute time allocations and queue rules](https://public.confluence.arizona.edu/display/UAHPC/Allocation+and+Limits)
  - [Storage information](https://public.confluence.arizona.edu/display/UAHPC/Storage)

- Account management and access
  - [Portal for account management](https://portal.hpc.arizona.edu/portal/)
  - [OnDemand Dashboard](https://ood.hpc.arizona.edu/pun/sys/dashboard)



**Cyverse**
 - [Cyverse](https://cyverse.org/)
 - [Cyverse getting started](https://learning.cyverse.org/en/latest/#cyverse-faq)

**Some Cloud Computing Examples**
- [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
- [My Binder](https://mybinder.org/)
- [Pangeo Binder](https://binder.pangeo.io/)

**Docker**
- [Intro to Docker](https://docker-curriculum.com/)

___
<a name="instructions"></a>
## Quick Start Steps For logging in and running a job on UAHPC
These instructions are following [this tutorial](https://public.confluence.arizona.edu/display/UAHPC/Ocelote+Quick+Start)
- Step 0: The first time you want to access UAHPC you will need to activate your account. To do this go [here](https://account.arizona.edu/account/create/hpcaccount)
and click on the link to `Notify your sponsor of your request` and when prompted put in Tom's email: tmeixner@email.arizona.edu. Once he accepts your request you should have access and step 1 will work for you.

1. Login to UA HPC. You can do this either from terminal line like this:
`ssh lecondon@hpc.arizona.edu` (This should work from GitBash but windows users might need to install putty for this to work) or you can login to the on-demand portal: <https://ood.hpc.arizona.edu/>. From the on demand portal you can then launch a terminal and follow along with these instructions the same as if you had launched a local terminal and ssh into HPC. In both cases you should select **Ocelote** as the location.

2.  To see where you are type `echo $HOSTNAME` this should return `login2`
Then use `va` to see what group you are a part of and what your allocation is.

3. Setup a Python environment (Note you only need to do this step once). The instructions below follow [this tutorial](https://public.confluence.arizona.edu/display/UAHPC/Using+and+Installing+Python). Note that we are doing this with virtual env not conda but the idea is the same. You could also load the conda module and use conda as your package manager if you prefer.
  - Load Python: `module load python` (if this is successful you should now see python3.6 when you type `module list`)
  - Create a virtual env: `virtualenv --system-site-packages ~/mypyenv` *Note**: you could choose to put your files somewhere other than `mypyenv` if you would like just change the name at the end here.
  - Activate your envrironment: `source ~/mypyenv/bin/activate`. You should  now see (mypyenv) on the left of your terminal lines indicating that you are in that environment.
  - Now you can add packages using `pip install` **NOTE** we are using virtualenv here rather than conda so you need to pip install rather than conda install.

4. Optional: Setup your environment to be active all the time. (if you prefer not to do this you can just module load and source your environment within a run script and as needed when you login).
  - `vi ~/.bashrc`
  - type `i` get into insert mode and then add the following two lines:
  ```
  module load python
  source ~/mypyenv/bin/activate
  ````
  - type `esc + shift + zz` to save
  - `source ~/.bashrc`

5. Create a directory for `HAS_tools`. You can do this with the file explorer from OnDemand or using mkdir from terminal

4. Upload some files to this directory. You can use the starter codes for this week if you want. Or you can just create your own really simple 'hello  world' python script (i.e. a python script with a print statement in it that says 'hello world')

2. Create a pbs script to submit your job. You can do this using the job builder tool: <https://jobbuilder.hpc.arizona.edu/>
  - select: 1 node, 1 core, for the standard queue
  - Create a run name and use tmeixner for your group name
  - set your run time to 5  minutes
  - Create a new file in the folder with your python script (e.g. `run_python.pbs`) and copy and paste the resulting bash file lines into that files
  - Add the following two lines to the bottom of the  script:
  ```
  cd ~/HAS_Tools
  python test.py
  ```
  - Note 1: Replace `/path/to` with the path to your HAS tools directory
  - Note 2: If the job won't submit you might need to change `cputime` to `cput`.
  - Note 3: There is an example pbs script in the starter code for this week. You can also upload that as a starting place.

7. Submit your job like this: `qsub run_python.pbs`

8. check on the status of your job `qstat -u yournetid` or you can just check on your one job like this: `qstat -u yourjob#`

9. Use vi to look at the outputs of your job in the two files that are created `runame.orunnumber` and `runname.erunnumber`

___
<a name="assignment"></a>
## Assignment 15: Supercomputing!
This week we are going to voyage off our our laptops. Your job is to make your script portable and run your forecast on Ocelote and one other location of  your choosing (i.e. two locations total)

#### Assignment

**Part 1: Run your forecast on Ocelote**
1. Modify your python script so that it will not need to be run interactively (i.e. so that you can run it from command line like this `python myscrip.py` and it will print out and save everything that you want).  You can test this by opening a terminal from within vscode and trying to run your script from there.  You can also simplify your script so that you don't need as many packages if you would like. No maps are required for this weeks submission.

2. Setup your environment and make a directory to work in on UA HPC see the instructions above.

3. Upload your script and inputs, create a submissions script and submit a job to generate your forecast.

4. Download your output file and pbs script for submission.

**Part 2: Run your forecast somewhere else**

Bonus points if you run it multiple other places :)

Suggested places to try:
- Run it on Puma (UAHPC)
- Make it a Ipython notebook and run it through the Jupyter server on Puma or Ocelote
- Run it on the cloud using google Colab
- Run it through Cyverse using Atmosphere

Depending on where you run the approach will be different but take a screen shot or download the output file to document your successful run.

**Part 3: Reflection**

With your submission please provide a readme that answers the following questions:

1. What resources did you request on Ocelote? How long did you wait in the queue for your job to run and how long did it take to run?
2. What was the most confusing part to you about setting up and running your job on Ocelote?
4. Where else did you run your job? How did the setup compare to your run on Ocelote?
3. What questions do you still have after doing this?


#### Forecast Rules for this week:
- You can do any mathematical operation using numpy or pandas package to do so and you can use LinearRegression models from the sklearn package.  

- You can use and of the datasets we have used so far in your analysis

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions for the one and two week forecasts and up to August 21st for the 16 week forecast.

#### Submission Instructions
1. Submit your forecast to the forecast competition following normal procedures.
2. Create a `Week15` folder in your `Submissions` folder of your homework folder and submit the following:
  - The output file generated from your run `runname.orunnumber`
  - The python script you ran
  - The submission script you created
  - Your written discussion `LastName_HW15.md`
