rab_array=[1,1]

def rab(k):
    global rab_array
    new=(rab_array[-2])*k+rab_array[-1]
    rab_array.append(new)

n=28
for i in range(n-2):
    rab(4)
print(rab_array[-1])
