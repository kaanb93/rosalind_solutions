import collections
import sys

file = open(sys.argv[1],"r")
file = file.readlines()
s=file[0]
sdict=dict(collections.Counter(s))
print(str(sdict["A"])+" "+str(sdict["C"])+" "+str(sdict["G"])+" "+str(sdict["T"]))
