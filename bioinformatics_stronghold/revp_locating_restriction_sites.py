from Bio import SeqIO

# open downloaded dataset
file = list(SeqIO.parse('rosalind_revp.txt', 'fasta'))

# define variables
# Seq objects have reverse_complement method
seq = str(file[0].seq)
reverse_complement = str(file[0].reverse_complement().seq)
positions = []
lengths = []

# loop to check subsequences with reverse complements
# take care of 1 indexing
for i in range(len(seq)):
    for j in range(4, 13):
        if i+j <= len(seq) and seq[i:i+j] == reverse_complement[len(seq)-i-j:len(seq)-i]:
            positions.append([str(i+1), str(j)])

# print results
for i in positions:
    print(' '.join(i))
