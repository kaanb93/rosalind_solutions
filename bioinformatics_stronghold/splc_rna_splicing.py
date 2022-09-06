# modified from prot_translating_rna_into_protein.py
from Bio import SeqIO
from Bio.Seq import Seq

# open downloaded dataset
file = list(SeqIO.parse('rosalind_splc.txt', 'fasta'))

# define the sequence
dna_sequence = str(file[0].seq)

# delete introns from sequence
for intron in file[1:]:
    dna_sequence = dna_sequence.replace(str(intron.seq), '')

# Seq object has translate function
# to_stop flag is needed for unnecessary character deletion
dna_seq = Seq(dna_sequence)
protein = dna_seq.translate(to_stop = True)

# print results
print(protein)
