import fastaparser
from difflib import SequenceMatcher
import sys

def longestSubstring(str1,str2):
     seqMatch = SequenceMatcher(None,str1,str2)
     match = seqMatch.find_matching_blocks(0, len(str1), 0, len(str2))
     return str1[match.a: match.a + match.size]


seq_dict={}
with open(sys.argv[1]) as fasta_file:
    parser=fastaparser.Reader(fasta_file)
    for seq in parser:
        seq_dict[seq.id]=seq.sequence_as_string()

keys=list(seq_dict.keys())
keys.sort()

seq1=seq_dict[keys[0]]
seq2=seq_dict[keys[1]]

longestSubstring(seq1,seq2)
