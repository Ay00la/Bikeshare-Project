# Explore US Bikeshare Data
## Project Overview
In this project, I used Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.
## Software Used
To complete this project, the following softwares were used:
* Python 3.8, NumPy, and Pandas installed using Anaconda
* Text editor(**Atom**)
* A terminal application (**Git Bash**)

Check **requirements.txt** file for more information

## Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

In this project, I use data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

## Statistics Computed
In this project, I wrote python code to provide the following information:

**1. Popular times of travel (i.e., occurs most often in the start time)**
* most common hour of day

**2. Popular stations and trip**
* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

**3. Trip duration**
* average trip time
* maximum trip time
* least trip time

**4. User info**
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* most common, maximum and minimum birth age (only available for NYC and Chicago)

**4. UserID info**
* returns data for specific _UserID_

## The Files
The three city dataset files:
* chicago.txt
* new york.txt
* washington.txt

## Requirements.txt File
The **requirements.txt** file shows the software(python library) version to work with. On your terminal(**Git Bash**), you can start by installing the software(if need be) using the command below:
```
pip install -r requirements.txt
```
Then proceed by running:
```
python bikeshare.py
```
**Note:** Ensure you are on the bikeshare-project working directory before running the commands above.
