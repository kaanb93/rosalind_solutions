from Bio.Seq import Seq

# open downloaded dataset
file = open('rosalind_prot.txt', 'r').read()

# define seq as Seq object
seq = Seq(str(file.strip()))

# Seq object has translate function
# to_stop flag is needed for unnecessary character deletion
protein = seq.translate(to_stop = True)

# print results
print(protein)
