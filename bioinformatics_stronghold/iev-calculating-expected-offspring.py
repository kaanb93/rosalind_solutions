import sys

file = open(sys.argv[1],"r")
file = file.readlines()
sp = file[0].split()
AA_AA=sp[0]
AA_Aa=sp[1]
AA_aa=sp[2]
Aa_Aa=sp[3]
Aa_aa=sp[4]
aa_aa=sp[5]

pair_list=[AA_AA,AA_Aa,AA_aa,Aa_Aa,Aa_aa,aa_aa]
perc_list=[1,1,1,0.75,0.5,0]

total=0
for i,pair in enumerate(pair_list):
    total+=pair*perc_list[i]*2

print(total)
