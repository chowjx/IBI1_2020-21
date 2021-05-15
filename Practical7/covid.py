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

print(covid_data.iloc[0,1]) # Get data in row 0, column 1 by row & column number
print(covid_data.iloc[2,0:5]) # Get data in row 2, from columns 0 to 5
print(covid_data.iloc[0:2,:]) # Get data from row 0 to 2 & all columns
print(covid_data.iloc[0:10:2,0:5]) # Get data from every second row between & including 0 & 8, & from columns 0 to 5
print(covid_data.iloc[0:12:2,:]) # Get data from every seconf row between & including 0 & 10, & from all columns