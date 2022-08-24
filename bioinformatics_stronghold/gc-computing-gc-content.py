import collections
import fastaparser
import sys

perc_dict={}

with open(sys.argv[1]) as fasta_file:
    parser=fastaparser.Reader(fasta_file)
    for seq in parser:
        seq.id
        seq.sequence_as_string()
        base_dict=dict(collections.Counter(seq.sequence_as_string()))
        perc=((base_dict["G"]+base_dict["C"])/len(seq.sequence_as_string()))*100
        perc_dict[seq.id]=perc

print(perc_dict)
