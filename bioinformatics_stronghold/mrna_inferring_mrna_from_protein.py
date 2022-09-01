# open downloaded dataset
file = open('rosalind_mrna.txt', 'r').read()

# define variables
protein_string = file.strip()
list_to_multiply = []
result = 1

# define a rna codon dictionary
codon_dict = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2,
    'Stop': 3, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6,
    'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
    'A': 4, 'D': 2, 'E': 2, 'G': 4}

# append list with dictionary keys for each aminoacid
# add stop at last
for character in protein_string:
    list_to_multiply.append(codon_dict[character])
list_to_multiply.append(codon_dict['Stop'])

# multiply and mod with each int in the list
for number in list_to_multiply:
    result = (result * number) % 1000000

# print results
print(result)
