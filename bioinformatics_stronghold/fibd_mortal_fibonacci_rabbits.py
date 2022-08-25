# open downloaded dataset
file = open('rosalind_fibd.txt', 'r').read()

# define variables
var_list = file.strip().split(' ')
n = int(var_list[0])
m = int(var_list[1])

# add deaths to the old solution (rosalind_fib)
rabbit_array = [0, 1]
for i in range(1, n):
    new_item = rabbit_array[-1] + rabbit_array[-2]
    if i == m:
        new_item -= rabbit_array[i - m + 1]
    elif i > m:
        new_item -= rabbit_array[i - m]
    rabbit_array.append(new_item)

# print results
print(rabbit_array[-1])
