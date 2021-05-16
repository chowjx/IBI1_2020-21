# Import necessary modules
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Perform os functions to change directory, print current working directory & list files in current directory
os.chdir("/Users/chowjx/Downloads")
print(os.getcwd())
print(os.listdir())

# Read full_data.csv file into a dataframe object named covid_data via pandas
covid_data = pd.read_csv("full_data.csv")
print(covid_data)

print(covid_data.head(5)) # Get first 5 rows of covid_data dataframe
covid_data.info() # Get info of data type of data points in covid_data
print(covid_data.describe()) # Get summary statistics of covid_data dataframe

print(covid_data.iloc[0,1]) # Get data from 1st row, 2nd column by row & column index
print(covid_data.iloc[2,0:5]) # Get data from 3rd row, from columns 0 to 5
print(covid_data.iloc[0:2,:]) # Get data from first 2 rows & all columns
print(covid_data.iloc[0:10:2,0:5]) # Get data from every second row between & including 0 & 8, & from columns 0 to 5

# Get data from every second row between & including 0 & 10, & from all columns
print(covid_data.iloc[0:12:2,:]) 

print(covid_data.iloc[0:3,[0,1,3]])
# Get data from first 3 rows but only the 1st, 2nd & 4th columns, below using Boolean
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3, my_columns])

print(covid_data.loc[2:4,"date"]) # Get data from row 2 to 4 & column named "date"
print(covid_data.loc[0:81,"total_cases"]) # Get data from row 0 to 81 & column named "total_cases"

# Get total cases from Afghanistan only (same output asc ovid_data.loc[0:81,"total_cases"])
print(covid_data.loc[covid_data['location'] == 'Afghanistan','total_cases'])

