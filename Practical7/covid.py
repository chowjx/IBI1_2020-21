import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/chowjx/Downloads")
os.getcwd()
os.listdir()

covid_data = pd.read_csv("full_data.csv")
print(covid_data)
print(covid_data.head(5))
covid_data.info()
