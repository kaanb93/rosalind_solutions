from Bio import SeqIO

# open downloaded dataset
records = list(SeqIO.parse('rosalind_orf.txt', 'fasta'))

# define variables
dna_string = str(records[0].seq)
reverse_complement = str(records[0].reverse_complement().seq)
translations = []
results = []

# define a dna codon dictionary
codon_dict = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

# get 3 different translations from dna string
for n in range(3):
    translation = []
    for i in range(n + 2, len(dna_string), 3):
        codon = dna_string[i-2:i+1]
        translation.append(codon_dict[codon])
    translations.append(translation)

# get 3 different translations from reverse complement
for n in range(3):
    translation = []
    for i in range(n + 2, len(reverse_complement), 3):
        codon = reverse_complement[i-2:i+1]
        translation.append(codon_dict[codon])
    translations.append(translation)

# get possible proteins starting with M and ending with Stop
for translation in translations:
    re = []
    for i, aa1 in enumerate(translation):
        if aa1 == 'M':
            for aa2 in translation[i:]:
                if aa2 != 'Stop':
                    re.append(aa2)
                else:
                    if ''.join(re) not in results:
                        results.append(''.join(re))
                    re = []
                    break

# print results
for result in results:
    print(result)
