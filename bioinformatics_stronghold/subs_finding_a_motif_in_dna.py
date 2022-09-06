# open downloaded dataset
file = open('rosalind_subs.txt', 'r').readlines()

# define variables
s = file[0].strip()
t = file[1].strip()
positions = []

# loop in the possible range to check substrings if they are the same as t
for i in range(len(s) - len(t)):
    substr = s[i:i+len(t)]
    if t == substr:
        positions.append(str(i + 1))

# print results
print(' '.join(positions))
