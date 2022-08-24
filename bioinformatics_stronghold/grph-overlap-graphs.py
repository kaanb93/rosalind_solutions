import fastaparser
import sys

seq_dict={}

with open(sys.argv[1]) as fasta_file:
    parser=fastaparser.Reader(fasta_file)
    for seq in parser:
        seq_dict[seq.id]=seq.sequence_as_string()

pairs=[]
for s in seq_dict.keys():
    suffix=seq_dict[s][-3:]
    for k in seq_dict.keys():
        if s==k:
            continue
        prefix=seq_dict[k][:3]
        if suffix==prefix:
            pairs.append([s,k])

for pair in pairs:
    print(pair[0]+" "+pair[1])
