import sys

file=open(sys.argv[1],"r")
lines=file.readlines()
for i,line in enumerate(lines):
    if i%2==0:
        continue
    else:
        print(line)
