#!/usr/bin/python
from json import dumps
from random import random

total    = 10000
set_cnt  = 6 # max 15
set_sz   = 1000
template = 10
output   = 'seed.txt'


randomInt = lambda x: int(random() * x)

a = [(i % template) * 0x10 for i in range(total)]

for j in range(set_cnt):
  i = 0
  while i < 1000:
    r = randomInt(total)
    if a[r] % 0x10 != 0:
      continue
    a[r] |= 1 + j
    i += 1

a = dumps(a)
with open(output, 'w') as f:
  f.write(a)
