from itertools import permutations

# open downloaded dataset
file = open('rosalind_lexf.txt', 'r').readlines()

# define variables
# multiply symbols to include each character itself for permutation
n = int(file[1].strip())
symbols = file[0].strip().split(' ') * n
strings = []

# use set to get unique values only
for element in list(set(permutations(symbols, n))):
    strings.append(''.join(element))

# python sort already sorts lexicographically
strings.sort()

# print results
for result in strings:
    print(result)
