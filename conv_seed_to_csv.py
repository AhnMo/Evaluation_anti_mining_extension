#!/usr/bin/python
from json import loads

with open('seed.txt', 'r') as f:
  data = f.read()
data = loads(data)
print len(data)

out = []

t = []
t.append('Template')
t.append('Type')
t.append('IsMining')
out.append(t)

for i in range(len(data)):
  x = data[i]
  t = []
  t.append(str(x / 0x10))
  y = x % 0x10
  if y == 0:
    t.append('Normal')
  elif y == 1:
    t.append('Coinhive Direct')
  elif y == 99:
    t.append('Coinhive Server')
  elif y == 98:
    t.append('Coinhive Inline')
  elif y == 2:
    t.append('Coinhive LibRename')
  elif y == 3:
    t.append('JSECoin')
  elif y == 4:
    t.append('SelfHosted')

  if y == 0:
    t.append('False')
  else:
    t.append('True')

  out.append(t)

out = [','.join(i) for i in out]

with open('seed.csv', 'w') as f:
  for o in out:
    f.write(o+'\r\n')
print 'Done'
