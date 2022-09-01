from Bio import SeqIO

# open downloaded dataset
file = list(SeqIO.parse('rosalind_revp.txt', 'fasta'))

# define variables
seq = str(file[0].seq)
reverse_complement = str(file[0].reverse_complement().seq)
positions = {}
lengths = []

# loop to check substrings if they are the same
for i in range(len(seq)):
    for j in range(4, 13):
        if i + j + 1> len(seq):
            break
        sub = seq[i:i + j]
        search = reverse_complement.find(sub)
        if search != -1:
            if i + 1 not in positions:
                positions[i + 1] = len(sub)
            else:
                if len(sub) > positions[i + 1]:
                    positions[i + 1] = len(sub)

for i in positions:
    print(i, positions[i], sep=' ')
