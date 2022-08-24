# open downloaded dataset
file = open('rosalind_ini4.txt', 'r').read()

# define variables
var_list = file.split(' ')
a = int(var_list[0])
b = int(var_list[0])

# operation
sum = 0
for n in range(a, b + 1):
    if n % 2 == 1:
        sum += n
    else:
        continue

# print result
print(sum)
