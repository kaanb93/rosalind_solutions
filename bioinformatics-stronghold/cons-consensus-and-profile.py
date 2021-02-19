import collections
import fastaparser

listA=[]
listC=[]
listG=[]
listT=[]

with open("rosalind_cons.txt") as fasta_file:
    parser=fastaparser.Reader(fasta_file)
    for seq in parser:
        if len(listA)==0:
            listA=[0 for i in range(len(seq.sequence_as_string()))]
            listC=[0 for i in range(len(seq.sequence_as_string()))]
            listG=[0 for i in range(len(seq.sequence_as_string()))]
            listT=[0 for i in range(len(seq.sequence_as_string()))]
        for i,s in enumerate(seq.sequence_as_string()):
            if s=="A":
                listA[i]+=1
            elif s=="C":
                listC[i]+=1
            elif s=="G":
                listG[i]+=1
            elif s=="T":
                listT[i]+=1
            else:
                raise KeyError("WTF!?")

consensus=[]
for i in range(len(listA)):
    greater="A"
    g=listA[i]
    if listC[i]>g:
        greater="C"
        g=listC[i]
    if listG[i]>g:
        greater="G"
        g=listG[i]
    if listT[i]>g:
        greater="T"
        g=listT[i]
    consensus.append(greater)
consensus="".join(consensus)
lists=[listA,listC,listG,listT]
for l in lists:
    for i,v in enumerate(l):
        l[i]=str(v)

A=" ".join(listA)
A="A: "+A
C=" ".join(listC)
C="C: "+C
G=" ".join(listG)
G="G: "+G
T=" ".join(listT)
T="T: "+T

output=open("cons_out.txt","w+")
output.write(consensus+"\n"+A+"\n"+C+"\n"+G+"\n"+T)
output.close()
