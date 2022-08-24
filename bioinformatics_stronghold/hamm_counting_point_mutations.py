# open downloaded dataset
file = open('rosalind_hamm.txt', 'r').readlines()

# define variables
s = file[0].strip()
t = file[1].strip()
count = 0

# check each character with the other using its index
for i, nuc in enumerate(s):
    if t[i] != nuc:
        count += 1

# print results
print(count)
