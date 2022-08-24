# open downloaded dataset
file = open("rosalind_ini5.txt", "r")

# read each line to make it into a list
lines = file.readlines()

# loop through the list to get even numbered lines
for i,line in enumerate(lines):
    if i % 2 == 0:
        continue
    else:
        print(line)
