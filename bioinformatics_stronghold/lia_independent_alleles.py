from scipy.stats import binom

# open downloaded dataset
file = open('rosalind_lia.txt', 'r').read()

# define variables
var_list = file.strip().split(' ')
k = int(var_list[0])
n = int(var_list[1])

# calculate cdf of binomial distribution as (2**k - n) trials, 2**k successes, 0.75 probabilty
prob = binom.cdf(2**k-n, 2**k, 0.75)

# print results
print(prob)
