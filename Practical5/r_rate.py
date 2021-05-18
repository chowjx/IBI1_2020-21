# Initial number of infected inidividuals
n = 84

# r rate variable
r_rate = 1.1

# calculate total no. of infections after 5 generations
i = 0
while i < 5:
    n = n + n * r_rate
    i = i + 1

# output
print('R rate is the average number of individuals infected by each individual with the virus.')
print('The r rate is ' + str(r_rate) + '.')
print('The total number of individuals infected after 5 generations is ' + str(int(n)) + '.')