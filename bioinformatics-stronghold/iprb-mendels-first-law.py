import sys

file = open(sys.argv[1],"r")
file = file.readlines()
sp = file[0].split()
k=sp[0]
m=sp[1]
n=sp[2]

pop=k+m+n

prob_kk=(k/pop)*((k-1)/(pop-1))
prob_km=((k/pop)*(m/(pop-1)))+((m/pop)*(k/(pop-1)))
prob_kn=((k/pop)*(n/(pop-1)))+((n/pop)*(k/(pop-1)))
prob_mm=(m/pop)*((m-1)/(pop-1))
prob_mn=((m/pop)*(n/(pop-1)))+((n/pop)*(m/(pop-1)))
prob_nn=(n/pop)*((n-1)/(pop-1))

kk=1
km=1
kn=1
mm=0.75
mn=0.5
nn=0
print(prob_kk*kk,prob_km*km,prob_kn*kn,prob_mm*mm,prob_mn*mn,prob_nn*nn)

print(prob_kk*kk+prob_km*km+prob_kn*kn+prob_mm*mm+prob_mn*mn+prob_nn*nn)
