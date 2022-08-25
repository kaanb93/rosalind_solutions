from Bio import SeqIO
from collections import Counter

# open downloaded dataset
records = SeqIO.parse('rosalind_cons.txt', 'fasta')

# get a list of nucleotides for each position
pos_dict = {}
for record in records:
    for i, nuc in enumerate(record.seq):
        if i not in pos_dict:
            pos_dict[i] = [nuc]
        else:
            pos_dict[i].append(nuc)

# define base matrix and result list
list_A = ['0' for i in range(len(record))]
list_C = ['0' for i in range(len(record))]
list_G = ['0' for i in range(len(record))]
list_T = ['0' for i in range(len(record))]
result = []

# count nucleotides for each position and add to matrix
for pos in pos_dict:
    counts = Counter(pos_dict[pos])
    for nucleotide in counts:
        if nucleotide == 'A':
            list_A[pos] = str(counts['A'])
        elif nucleotide == 'C':
            list_C[pos] = str(counts['C'])
        elif nucleotide == 'G':
            list_G[pos] = str(counts['G'])
        elif nucleotide == 'T':
            list_T[pos] = str(counts['T'])
    result.append(max(pos_dict[pos], key = pos_dict[pos].count))

# print results
print(''.join(result))
print('A: ' + ' '.join(list_A))
print('C: ' + ' '.join(list_C))
print('G: ' + ' '.join(list_G))
print('T: ' + ' '.join(list_T))
