# import modules for os and regular expressions
import os
import re 

# Perform os functions to change directory & print current working directory
os.chdir("/Users/chowjx/Downloads")
print(os.getcwd())

allcdna = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') # Open & read fasta file
lines = allcdna.readlines()     # get the data from the allcdna fasta file

result = []
for i in range(0, len(lines)):
    if lines[i].startswith(">"):  # Locate the description
        if 'unknown function' in lines[i]:  # Check whether sequence has an unknown function
            result.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
            bases = ''
            for n in range(0, len(lines[i:-1])):
                if not lines[i+n+1].startswith(">"):  # Skip the description line
                    bases += lines[i+n+1][:-1]
                else:
                    break
            bases += "\n"
            result.append(bases)

for i in range(0, len(result)):   # Read the length of the DNA sequence
    if result[i].startswith(">"):
        result[i] += "  "
        result[i] += str(len(result[i+1]) - 1)
        result[i] += "\n"

with open('unknown_function.fa', 'w') as output: # Create a fasta file to write output in it
    unknown_function = open('unknown_function.fa', "w")
for line in result:     #To branch out; the names & sequences of different DNA are separated using a for loop
    unknown_function.write(line)
unknown_function.close()