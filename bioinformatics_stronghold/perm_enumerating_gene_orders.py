from itertools import permutations

# open downloaded dataset
file = open('rosalind_perm.txt', 'r').read()

# define variables
number = int(file.strip())

# get permutations in a list
perm = list(permutations([i for i in range(1, number + 1)]))

# print results as the format requires
print(len(perm))
for i in perm:
    print(' '.join([str(a) for a in i]))
