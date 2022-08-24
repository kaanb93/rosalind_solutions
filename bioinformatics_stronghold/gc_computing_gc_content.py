from collections import Counter
from Bio import SeqIO

# open downloaded dataset
records = SeqIO.parse('rosalind_gc.txt', 'fasta')

# just need to remember the record with highest percentage
max_id = None
max_perc = 0

# loop that calculates gc percentage for each record
for record in records:
    counts = dict(Counter(record.seq))
    gc_perc = ((counts['G'] + counts['C']) / len(record.seq)) * 100

    # if new percentage is higher, switch max percentage, and define new record id
    if gc_perc > max_perc:
        max_perc = gc_perc
        max_id = record.id

# print results
print(max_id)
print(max_perc)
