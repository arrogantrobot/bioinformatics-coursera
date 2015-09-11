#!/usr/bin/env python3
import sys
seq, k, l, t = sys.stdin.read().split()


answer = {}
#generate a list of all k-mers
for i in xrange(len(seq)-(k-1)):
    x = seq[i:i+k]
    if x in answer:
        answer[x] += 1
    else:
        answer[x] = 1

#sort k-mers by occurences
#output = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)
for kmer in output:
    if answer[kmer] > l:

