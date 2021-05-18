# create a function to translate DNA sequences to amino acids
def translate(seq):
    # import codon table
    codon_table = {
        'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'U',
        'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W',
        }
    # create a list for protein
    protein = ''
    # match codon in seq to amino acid (translation)
    if len(seq)%3 == 0: # to ensure codons are 3-letter long
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            protein += (codon_table[codon])
        return protein

import re, os

file = open(input())
lines = file.readlines()     # get the data from the input file

result = []
for i in range(0, len(lines)):
    if lines[i].startswith(">"):  # Locate the description
        if 'unknown function' in lines[i]:  # Check whether it is unknown function
            result.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
            bases = ''
            for n in range(0, len(lines[i:-1])):
                if not lines[i+n+1].startswith(">"):  # Skip the description line
                    bases += lines[i+n+1][:-1]
                    protein_sequence = translate(bases)   #Translate the DNA into a protein sequence using the translate function
                else:
                    break
            protein_sequence += "\n"
            result.append(protein_sequence)

for i in range(0, len(result)):   # Read the length of the protein
    if result[i].startswith(">"):
        result[i] += "  "
        result[i] += str(len(result[i+1]) - 1)
        result[i] += "\n"

with open('unknown_protein.fa','w') as output:
    unknown_function = open('unknown_protein.fa', "w")
for line in result:     #To branch out; the names and sequences of different protein are separated using a for loop
    unknown_function.write(line)
unknown_function.close()

