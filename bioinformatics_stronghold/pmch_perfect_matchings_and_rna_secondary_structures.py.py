from Bio import SeqIO
import math

# open downloaded dataset
file = list(SeqIO.parse('rosalind_pmch.txt', 'fasta'))

# define variables
sequence = str(file[0].seq)

# perfect matchings  = factorial x * factorial y
result = math.factorial(sequence.count('A')) * math.factorial(sequence.count('G'))

# print results
print(result)
