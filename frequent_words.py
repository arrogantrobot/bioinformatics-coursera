#!/usr/bin/env python

import sys
import operator

#fasta of sequence
seq_f = sys.argv[1]

f = open(seq_f)
f.readline()
seq = f.readline().strip()
k = int(f.readline().strip())
f.close()

answer = {}
#generate a list of all k-mers
for i in xrange(len(seq)-(k-1)):
    x = seq[i:i+k]
    if x in answer:
        answer[x] += 1
    else:
        answer[x] = 1

#sort k-mers by occurences
output = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

for x in output:
    print "{0}: {1}".format(x[0],x[1])
