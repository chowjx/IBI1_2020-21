# total number of IBI1 students
n = 84

# r rate variable
r_rate = 1.1

# calculate total no. of infections after 5 generations
inf_num = n *r_rate *r_rate *r_rate *r_rate *r_rate

# output
print('R rate is the average number of individuals infected by each individual with the virus.')
print('The total number of individuals infected after 5 generations is ' + str(int(inf_num)) + '.')