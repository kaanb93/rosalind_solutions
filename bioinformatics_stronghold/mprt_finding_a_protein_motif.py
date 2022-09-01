from Bio import SeqIO
from io import StringIO
import requests
import re

# open downloaded dataset
file = open('rosalind_mprt.txt', 'r').readlines()
ids = [id.strip() for id in file]

# base uniprot string
base_uniprot_url = 'http://www.uniprot.org/uniprot/'

# get each fasta to be saved to records
records = []
for id in ids:
     with requests.get(base_uniprot_url + id + '.fasta') as handle:
         fasta_io = StringIO(handle.text)
         rec = list(SeqIO.parse(fasta_io, 'fasta'))[0]
         records.append(rec)
         handle.close()

# define a function to check if there is n-glucosylation motif at the position
def motif_check(seq):
    exp = r'N[^P][ST][^P]'
    if re.match(exp, seq):
        return True

motif_positions = []
for record in records:
    position_list = []
    for i in range(len(record.seq) - 4):
        substr = str(record.seq[i:i + 4])
        if motif_check(substr):
            position_list.append(str(i + 1))
    motif_positions.append(position_list)

for i, lst in enumerate(motif_positions):
    if lst != []:
        print(ids[i])
        print(' '.join(lst))
