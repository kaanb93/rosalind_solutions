import collections
import fastaparser

perc_dict={}

with open("rosalind_gc.txt") as fasta_file:
    parser=fastaparser.Reader(fasta_file)
    for seq in parser:
        seq.id
        seq.sequence_as_string()
        base_dict=dict(collections.Counter(seq.sequence_as_string()))
        perc=((base_dict["G"]+base_dict["C"])/len(seq.sequence_as_string()))*100
        perc_dict[seq.id]=perc

print(perc_dict)

#
# perc_dict={}
# for i,line in enumerate(lines):
#     if line.startswith(">"):
#         line=line.strip()
#         id=line[1:]
#         seq=lines[i+1]
#         seq=seq.strip()
#         base_dict=dict(collections.Counter(seq))
#         perc=((base_dict["G"]+base_dict["C"])/len(seq))*100
#         perc_dict[id]=perc
# print(perc_dict)
