#!/usr/bin/env python

import sys
import math

pattern = sys.argv[1].strip()
p = list(pattern)
p.reverse()
answer = 0

chars = { "A":0, "C":1, "G":2, "T":3 }

for n in range(0, len(p)):
    answer += math.pow(4, n) * (chars[p[n]])
    print answer
print answer
