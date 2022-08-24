import fastaparser
import re

def long_substr(data):
  substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
  s = substrs(data[0])
  for val in data[1:]:
    s.intersection_update(substrs(val))
  return max(s, key=len)

with open("rosalind_lcsm.txt","r") as fasta_file:
    parser = fastaparser.Reader(fasta_file)
    seqs=[]
    for seq in parser:
        seqs.append(seq.sequence_as_string())

    print(long_substr(seqs))
