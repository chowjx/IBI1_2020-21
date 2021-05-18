# What does this piece of code do?
# Answer: Draw a random integer between 1 and 50.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:        # while loop to keep drawing random number until a random number is printed
	p = True
	n = randint(1,100) # draws a random number between 1 and 100
	if n > 50:         # if random number drawn is bigger than 50, return to while loop and draw another random number
		p = False

print(n)
