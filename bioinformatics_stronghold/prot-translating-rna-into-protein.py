import sys

file = open(sys.argv[1],"r")
file = file.readlines()
s = file[0]

a="""UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

s_codon=[(s[i:i+3]) for i in range(0,len(s),3)]

a_list=a.split()
a_dict={}
for i,v in enumerate(a_list):
    if i%2==0:
        a_dict[v]=a_list[i+1]

out=[]
for codon in s_codon:
    if a_dict[codon]=="Stop":
        break
    else:
        out.append(a_dict[codon])
print("".join(out))
