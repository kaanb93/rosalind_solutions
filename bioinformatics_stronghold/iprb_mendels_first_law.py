from collections import Counter

# open downloaded dataset
file = open('rosalind_iprb.txt', 'r').read()

# define variables
var_list = file.strip().split(' ')
k = int(var_list[0])
m = int(var_list[1])
n = int(var_list[2])

# define organisms and populate the population
organisms = [['AA'], ['Aa'], ['aa']]
starting_population = organisms[0] * k + organisms[1] * m + organisms[2] * n
ending_population = []

# get every single possible outcome into the ending population
for i, org1 in enumerate(starting_population[:-1]):
    for j, org2 in enumerate(starting_population[i + 1:]):
        ending_population.append(org1[0] + org2[0])
        ending_population.append(org1[1] + org2[0])
        ending_population.append(org1[0] + org2[1])
        ending_population.append(org1[1] + org2[1])

# count all genotypes and calculate dominant phenotype probability
population_counts = dict(Counter(ending_population))
dominant_phenotype_prob = ((len(ending_population) - population_counts['aa']) / len(ending_population))

# print results
print(dominant_phenotype_prob)
