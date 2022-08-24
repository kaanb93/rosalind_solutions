# open downloaded dataset
file = open('rosalind_fib.txt', 'r').read()

# define variables
var_list = file.strip().split(' ')
n = int(var_list[0])
k = int(var_list[1])

# define a sequence, calculate new item, append the sequence
rabbit_array = [1, 1]
for i in range(n - 2):
    new_item = rabbit_array[-1] + rabbit_array[-2] * k
    rabbit_array.append(new_item)

# print results
print(rabbit_array[-1])
