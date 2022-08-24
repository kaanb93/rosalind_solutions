# open downloaded dataset
file = open('rosalind_ini2.txt', 'r').read()

# define variables
var_list = file.split(' ')
a = int(var_list[0])
b = int(var_list[1])

# operation
result = a ** 2 + b ** 2

# print result
print(result)
