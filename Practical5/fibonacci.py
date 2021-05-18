# number of terms in the sequence
n = 13

# first two terms in the sequence
a = 1
b = 1

# starting sum
sum = 1

# count each term in the sequence
count = 1

# print the sequence with space in between each value
print('Fibonacci Sequence: ', end = ' ')

# use a while loop to count up to the nth term
while(count <= n):
    print(sum, end = ' ')
    count += 1 # count number increases up to n
    a = b # replace first term by second term
    b = sum # replace second term by third term, which is the sum
    sum = a + b # add the first two terms, and so on
