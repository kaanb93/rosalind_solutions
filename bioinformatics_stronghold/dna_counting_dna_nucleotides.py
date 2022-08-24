from collections import Counter

# open downloaded dataset
file = open("rosalind_dna.txt", "r").read()

# save nucleotide counts to a dictionary
nuc_dict = dict(Counter(file))

# print results in the specified order
print(str(nuc_dict["A"]), str(nuc_dict["C"]), str(nuc_dict["G"]), str(nuc_dict["T"]), sep=" ")
