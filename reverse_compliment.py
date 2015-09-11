#!/usr/bin/env python

import sys

f = open(sys.argv[1])

seq = f.readline().strip()

comp = {"A":"T", "C":"G", "G":"C", "T":"A"}

seq = list(seq)
seq.reverse()
answer = []
for n in seq:
    answer.append(comp[n])

print "".join(answer)
