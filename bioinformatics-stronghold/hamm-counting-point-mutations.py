import sys

file = open(sys.argv[1],"r")
file = file.readlines()

s = file[0]
t = file[1]

count=0
for i,b in enumerate(s):
    if t[i]!=b:
        count+=1
print(count)
