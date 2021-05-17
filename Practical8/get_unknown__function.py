# import modules for os and regular expressions
import os
import re 

# Perform os functions to change directory, print current working directory & list files in current directory
os.chdir("/Users/chowjx/Downloads")
print(os.getcwd())
print(os.listdir())