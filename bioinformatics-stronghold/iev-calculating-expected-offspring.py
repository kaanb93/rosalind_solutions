AA_AA=18792
AA_Aa=18034
AA_aa=16307
Aa_Aa=18214
Aa_aa=18511
aa_aa=19199

pair_list=[AA_AA,AA_Aa,AA_aa,Aa_Aa,Aa_aa,aa_aa]
perc_list=[1,1,1,0.75,0.5,0]

total=0
for i,pair in enumerate(pair_list):
    total+=pair*perc_list[i]*2

print(total)
