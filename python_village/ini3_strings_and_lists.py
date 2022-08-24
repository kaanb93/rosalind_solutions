# open downloaded dataset
file = open('rosalind_ini3.txt', 'r').readlines()

# define variables
s = str(file[0])
var_list = file[1].split(' ')
a = int(var_list[0])
b = int(var_list[1])
c = int(var_list[2])
d = int(var_list[3])

# operation
result = s[a:b + 1] + ' ' + s[c:d + 1]

# print result
print(result)
