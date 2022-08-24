from re import sub

# open downloaded dataset
file = open('rosalind_rna.txt', 'r')

# convert all T to U
rna = sub('T', 'U', file)

# print results
print(rna)
