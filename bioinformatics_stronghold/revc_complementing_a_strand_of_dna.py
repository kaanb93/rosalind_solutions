# open downloaded dataset
file = open('rosalind_revc.txt', 'r').read()

# define variables
s = file.strip()

# operation to get complement
complement = []
for i in s:
    if i == 'A':
        complement.append('T')
    elif i == 'T':
        complement.append('A')
    elif i == 'C':
        complement.append('G')
    elif i == 'G':
        complement.append('C')
    else:
        raise KeyError(i + ' character should not exist in this file.')

# complement to reverse complement
reverse_complement = complement[::-1]

# print results
print(''.join(reverse_complement))
