#!/usr/bin/env python

import sys
import operator

#first argument is a single-line fasta input
seq_f = sys.argv[1]

f = open(seq_f)

#f.readline() #toss input line
seq = f.readline() #grab fasta
seq = seq.strip()
kmer = f.readline().strip() #grab kmer
f.close()

#second argument is the k-mer to find
#kmer = sys.argv[2]
k = len(kmer)

count = 0

print seq
print kmer

#generate a list of all k-mers
for mer in [seq[i:i+k] for i in xrange(len(seq)-(k-1))]:
    print mer
    if mer == kmer:
        count += 1

print count
