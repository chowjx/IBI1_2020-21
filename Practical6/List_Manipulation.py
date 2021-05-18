exon_counts = [51,1142,42,216,25,650,32533,57,1,523]
gene_lengths = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
# Calculate average exon length by dividing gene lengths by exon counts
average_exon_length = [m/n for m, n in zip(gene_lengths, exon_counts)]
# Sort values in average exon length list ascendingly
average_exon_length.sort()
average_exon_length = [round(num) for num in average_exon_length]
print('sorted average exon length:', average_exon_length)

import matplotlib.pyplot as plt
plt.boxplot(average_exon_length) # Plot boxplot displaying the distribution of average exon length
plt.ylabel('Average Exon Length')
plt.xlabel('Gene')
plt.show()


