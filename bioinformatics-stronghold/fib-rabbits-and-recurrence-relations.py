import sys

file = open(sys.argv[1],"r")
file = file.readlines()
n = file[0].split()[0]
k = file[0].split()[1]
rab_array=[1,1]

def rab(k):
    global rab_array
    new=(rab_array[-2])*k+rab_array[-1]
    rab_array.append(new)

for i in range(n-2):
    rab(k)
print(rab_array[-1])
