# import os module to use its functions to change directory to the one where the sequence files are stored
import os
os.chdir("/Users/chowjx/Downloads")

# Created a blosum62 dictionary in a separete file (blosum62_dict) to be imported here to use
from blosum62_dict import blosum62

# To read the human, mouse & random sequences 
human = open('SOD2_human.fa')
mouse = open('SOD2_mouse.fa')
random = open('RandomSeq.fa')
human_seq = human.readlines()
mouse_seq = mouse.readlines()
random_seq = random.readlines()

# Create function to compare alignments of a pair of sequences & to compute the alignment score using blosum62 matrix
def compare(seq1, seq2):
    score = 0
    distance = 0
    for	i in range(len(seq1)):
        if	seq1[i]!=seq2[i]:
            distance +=	1   # Count the number of different terms

        if (seq1[i], seq2[i]) in blosum62:
            score = score + blosum62[seq1[i], seq2[i]]
        else:
            score = score + blosum62[seq2[i], seq1[i]]

    percentage = 1- distance/len(seq1)
    print('alignment score = ' + str(score))
    print('Percentage of identical amino acids = ' + str(percentage*100) + '%')

print(human_seq)
print(mouse_seq)
compare(human_seq[1][:-1], mouse_seq[1][:-1])

print(human_seq)
print(random_seq)
compare(human_seq[1][:-1], random_seq[1][:-1])

print(mouse_seq)
print(random_seq)
compare(mouse_seq[1][:-1], random_seq[1][:-1])

#Summary:
# ['>SOD2_human (NP_000627.2)\n', 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK\n']
# ['>SOD2_mouse (NP_038699.2)\n', 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK\n']
# alignment score = 1091
# Percentage of identical amino acids = 89.63963963963964%
# ['>SOD2_human (NP_000627.2)\n', 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK\n']
# ['>RandomSeq\n', 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL\n']
# alignment score = -250
# Percentage of identical amino acids = 5.405405405405405%
# ['>SOD2_mouse (NP_038699.2)\n', 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK\n']
# ['>RandomSeq\n', 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL\n']
# alignment score = -250
# Percentage of identical amino acids = 5.855855855855852%
#Interpretation: 
# Positive allignment scores indicate the pair of sequences compared are more related to each other.
# Negative allignment scores indicate the pair of sequences compared are more distant from each other.
# The sequence to code for the same protein (SOD2 protein) in both human and mouse are relatively identical, 
# with close to 90% of percentage identity and a positive allignment score. This means that the sequences are closely related with similar functions.
# The regions of matching amino acids in both human & mouse sequences are more likely to be functionally important for the protein as
# they are more likely to be a signature of evolutionary constraint between the two sequences which are preserved during evolution.
# The high percentage identity between the human & mouse sequences may suggest why mouse are often used as animal models in research, 
# for example: human diseases can be mimicked in mouse to carry out drug-testing; in gene therapy, 
# find potential therapeutic targets for treatment in humans through manipulation of the matches or mismatches in mouse sequence.
# The percentage identity in both human & mouse when align with the random sequence are similar, at 5.41% & 5.86% respectively.
# The alignment scores for both human & mouse when align with the random sequence are negative.
# This means that the random sequence is distant from both human and mouse sequence and they are hardly or not at all related, with different functions.

