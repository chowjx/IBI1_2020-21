# import human, mouse & random sequences as string variables
human_seq = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse_seq = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random_seq = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

# human-mouse analysis
h_m_dist = 0
for i in range(len(human_seq)):
    if human_seq[i]!=mouse_seq[i]:
        h_m_dist += 1

print('human-mouse analysis: ')
print('alignment score = ' + str(h_m_dist))

# Find percentage identity between human & mouse amino acids
h_m_percentage = ((len(human_seq)-h_m_dist)/len(human_seq))*100
print('percentage of identical amino acids = ' + str(h_m_percentage) + '%')

# human-random analysis
h_r_dist = 0
for i in range(len(human_seq)):
    if human_seq[i]!=random_seq[i]:
        h_r_dist += 1

print('human-random analysis: ')
print('alignment score = ' + str(h_r_dist))

# Find percentage identity between human & random amino acids
h_r_percentage = ((len(human_seq)-h_r_dist)/len(human_seq))*100
print('percentage of identical amino acids = ' + str(h_r_percentage) + '%')

# mouse-random analysis
m_r_dist = 0
for i in range(len(mouse_seq)):
    if mouse_seq[i]!=random_seq[i]:
        m_r_dist += 1

print('mouse-random analysis: ')
print('alignment score = ' + str(m_r_dist))

# Find percentage identity between mouse & random amino acids
m_r_percentage = ((len(mouse_seq)-m_r_dist)/len(mouse_seq))*100
print('percentage of identical amino acids = ' + str(m_r_percentage) + '%')

#Summary:
#human-mouse analysis: 
#alignment score = 23
#percentage of identical amino acids = 89.63963963963964%
#human-random analysis: 
#alignment score = 210
#percentage of identical amino acids = 5.405405405405405%
#mouse-random analysis: 
#alignment score = 209
#percentage of identical amino acids = 5.8558558558558556%
#Interpretation: 
# The sequence to code for the same protein (SOD2 protein) in both human and mouse are relatively identical, 
# with close to 90% of percentage identity & only 23 mismatches. This means that the sequences are closely related with similar functions.
# The regions of matching amino acids in both human & mouse sequences are more likely to be functionally important for the protein as
# they are more likely to be a signature of evolutionary constraint between the two sequences which are preserved during evolution.
# The high percentage identity between the human & mouse sequences may suggest why mouse are often used as animal models in research, 
# for example: human diseases can be mimicked in mouse to carry out drug-testing; in gene therapy, 
# find potential therapeutic targets for treatment in humans through manipulation of the matches or mismatches in mouse sequence.
# The number of mismatches in both human & mouse when align with the random sequence is almost the same, with 210 and 209 mismatches respectively.
# This means that the random sequence is very distant from both human and mouse sequence and they are hardly or not at all related, with different functions.

