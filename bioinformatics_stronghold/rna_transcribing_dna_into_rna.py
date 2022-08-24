from re import sub

# open downloaded dataset
file = open('rosalind_rna.txt', 'r').read()

# convert all T to U
rna = sub('T', 'U', file.strip())

# print results
print(rna)
