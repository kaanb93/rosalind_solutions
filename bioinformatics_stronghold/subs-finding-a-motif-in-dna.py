import sys

file = open(sys.argv[1],"r")
file = file.readlines()
s = file[0]
t = file[1]

pos=[]
for i in range(len(s)):
    try:
        check=s[i:i+len(t)]
    except:
        pass
    if t==check:
        pos.append(str(i+1))

print(" ".join(pos))
