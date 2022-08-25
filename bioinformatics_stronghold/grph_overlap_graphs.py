from Bio import SeqIO

# open downloaded dataset
records = list(SeqIO.parse('rosalind_grph.txt', 'fasta'))

# define a list to keep matches
matches = []

# loop to get O3 matches
for record1 in records:
    for record2 in records:
        if str(record1.seq) == str(record2.seq):
            continue
        else:
            None
        if record1.seq[-3:] == record2.seq[:3]:
            matches.append([record1.id, record2.id])

# print results
for match in matches:
    print(' '.join(match))
