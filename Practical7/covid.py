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
# Get first 5 rows of covid_data dataframe
print(covid_data.head(5))
# Get info of data type of data points in covid_data
covid_data.info()
# Get summary statistics of covid_data dataframe
print(covid_data.describe())
# Get data in 1st row, 2nd column by row & column number
print(covid_data.iloc[0,1])
