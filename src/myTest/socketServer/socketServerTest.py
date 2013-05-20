'''
Created on 2013-5-20

@author: lavenda
'''
#!/usr/bin/env python2.6
# -*- utf-8

from SocketServer import TCPServer
from SocketServer import StreamRequestHandler
from time import ctime
from myLibs.thread.threadqueue import core

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
        
tcpServ = TCPServer(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()