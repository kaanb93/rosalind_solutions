import re
import sys

file = open(sys.argv[1],"r")
file = file.readlines()
s = file[0]
ss=re.sub("T","U",s)
print(ss)
