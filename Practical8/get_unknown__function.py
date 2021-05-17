# import modules for os and regular expressions
import os
import re 

# Perform os functions to change directory, print current working directory & list files in current directory
os.chdir("/Users/chowjx/Downloads")
print(os.getcwd())
print(os.listdir())

allcdna = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') # Open & read fasta file
output = open('unknown_function.fa', 'w') # Create a fasta file to write output in it
