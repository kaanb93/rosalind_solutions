from Bio import SeqIO
from itertools import combinations

# open downloaded dataset
records = list(SeqIO.parse('rosalind_lcsm.txt', 'fasta'))

# define a list to include every substring of the first string
sub_list = [str(records[0].seq[x:y]) for x, y in combinations(range(len(records[0].seq)), r = 2)]

# reverse sort the list by their length so that we do not loop through the list with short subs
sub_list.sort(key = len, reverse = True)

# run a loop to check subs if it is in every string
# replace longest_sub if it is
longest_sub = ''
for sub in sub_list:
    if len(sub) <= len(longest_sub):
        break
    next = False
    for record in records:
        if sub in str(record.seq):
            continue
        else:
            next = True
            break
    if next == True:
        continue
    else:
        longest_sub = sub

# print results
print(longest_sub)
