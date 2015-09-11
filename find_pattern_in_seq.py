#!/usr/bin/env python3

import sys
pattern, seq = sys.stdin.read().split()
pattern = pattern.strip()
seq = seq.strip()
k = len(pattern)
first = pattern[0]
answers = []
for pos in range(len(seq) - (k-1)):
  if seq[pos] == first:
    if seq[pos:pos+k] == pattern:
      answers.append(str(pos))

print(" ".join(answers))
