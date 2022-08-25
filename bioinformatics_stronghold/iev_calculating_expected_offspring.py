# open downloaded dataset
file = open('rosalind_iev.txt', 'r').read()
number_of_couples = [int(i) for i in file.strip().split(' ')]

# define a list of couples genotypes
genotypes = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']

# define a list of probabilies of each couple in order
percentages = [1, 1, 1, 0.75, 0.5, 0]

# multiply number of couples with its percentage
# double it since there are two offspring for each couple
result = 0
for i, num in enumerate(number_of_couples):
    result += num * percentages[i] * 2

# print results
print(result)
