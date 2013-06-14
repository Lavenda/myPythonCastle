#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-20

@author: lavenda
"""

from SocketServer import ThreadingTCPServer
from SocketServer import StreamRequestHandler
from time import ctime
import os
#from myLibs.thread.threadqueue import core

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print '...connected from:', self.client_address
        command = self.rfile.readline()
        back = os.system(command)
        print back
        response = 'has done'
        self.wfile.write('[%s] %s' % (ctime(), response))
        
        
def main():
    tcpServ = ThreadingTCPServer(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()


if __name__ == '__main__':
    main()