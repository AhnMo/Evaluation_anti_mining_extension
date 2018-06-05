#!/usr/bin/python

try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3.x
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

import sys
import os

from posixpath import normpath
from urllib import unquote

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class RootedHTTPRequestHandler(SimpleHTTPRequestHandler):

    def translate_path(self, path):
        self.base_path = './output'

        path = normpath(unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = self.base_path
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)
        return path

if sys.argv[1:]:
    address = sys.argv[1]
    if (':' in address):
        interface = address.split(':')[0]
        port = int(address.split(':')[1])
    else:
        interface = '0.0.0.0'
        port = int(address)
else:
    port = 8000
    interface = '0.0.0.0'

if sys.argv[2:]:
    os.chdir(sys.argv[2])

print 'Started HTTP server on ' +  interface + ':' + str(port)

server = ThreadingSimpleServer((interface, port), RootedHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print 'Finished.'
