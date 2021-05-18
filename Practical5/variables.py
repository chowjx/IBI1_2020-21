# 3.1 Some simple math
# define variable a as my birthday as a 6 figure value
a = 131100
# define variable b as Rob's birthday as a 6 figure value
b = 190784
# define variable c as today's date as a 6 figure value 
c = 100321

d = a - c
e = a - b

# compare if value d is bigger than value e
if d > e:
    print('d is greater than e')
else:
    print('e is greater than d')

# 3.2 Booleans
X = False # Make boolean variable X
Y = True # Make boolean variable Y
Z = (X and not Y) or (Y and not X)
print(Z)
# Output return 'True'

W = X != Y
if W == Z:
    print(W == Z)
# Output return 'True'

# verify Z as true if either X or Y (but not both) are true
X = True # Make boolean variable X
Y = True # Make boolean variable Y
Z = (X and not Y) or (Y and not X)
print(Z)
# Output return 'False'

# verify that W and Z are always the same, no matter the values of X and Y
W = X != Y
if W == Z:
    print(W == Z)
# Output return 'True'