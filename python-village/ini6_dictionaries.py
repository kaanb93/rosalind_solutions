from collections import Counter

# open downloaded dataset
s = open('rosalind_ini6.txt', 'r')

# split dataset to make it into a list
slist = s.split(' ')

# Counter does all the work itself, just need to store it as a dictionary
sdict = dict(Counter(slist))

# print results
for key in sdict.keys():
    print(key + ' ' + str(sdict[key]))
