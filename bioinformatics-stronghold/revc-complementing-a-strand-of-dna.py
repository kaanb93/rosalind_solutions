import re
import sys

file = open(sys.argv[1],"r")
file = file.readlines()
s = file[0]
res=[]
for i in s:
    if i=="A":
        res.append("T")
    elif i=="T":
        res.append("A")
    elif i=="C":
        res.append("G")
    elif i=="G":
        res.append("C")
    else:
        raise KeyError("WTF!?")
res=res[::-1]
print("".join(res))
