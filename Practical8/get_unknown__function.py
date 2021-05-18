# import modules for os and regular expressions
import os
import re 

# Perform os functions to change directory & print current working directory
os.chdir("/Users/chowjx/Downloads")
print(os.getcwd())

allcdna = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') # Open & read fasta file
output = open('unknown_function.fa', 'a+') # Create a fasta file to write output in it

name = ''
seq = ''
for line in allcdna:
    if line[0] == '>':
        if 'unknown function' in line:
            output.write('\n')
            output.write(str(len(line)))
    elif line[0] != '>':
        output.write(line)

output.write(line.strip() +  '\n')





