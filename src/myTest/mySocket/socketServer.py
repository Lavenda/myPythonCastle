'''
Created on 2013-5-23

@author: lavenda
'''

#!/usr/bin/env python2.6
# -*- utf-8

from SocketServer import ThreadingTCPServer
from SocketServer import StreamRequestHandler
from time import ctime
import os
import socketConfigHelper
#from myLibs.thread.threadqueue import core

flag = None
goal = None
class MyRequestHandler(StreamRequestHandler):
 
    
    
    def handle(self):
        print '...connected from:', self.client_address
        hint = self.rfile.readline()
        result, formatFlag = self.commandHandle(hint)
        response = ''
        if result == 0:
            response = 'has done'
        else:
            response = 'error'
        if formatFlag == u'None':
            response += '@None'
        elif formatFlag == u'system':
            response += '@system'
        else:
            response += '@'
        self.wfile.write('[%s] %s' % (ctime(), response))
    
    def setup(self):
        StreamRequestHandler.setup(self)
    
    def commandHandle(self, hint):
        global flag
        global goal
        hint = hint.strip()
        print flag
        if not flag:
            scf = socketConfigHelper.SocketConfigHelper() 
            importEnv, goalType, goalValue = scf.getGoalByHint(hint)
            if not importEnv:
                return 1, u'None'
            goal = getattr(__import__(importEnv), goalValue)
            flag = hint
            return 0, u'system'
        if flag == u'system':
            if hint == u'exit':
                flag = None
                return 0, u'None'
            result = goal(hint)
            return result, u'system'


def main(host, port=21567):
    address = (host, port)
    tcpServ = ThreadingTCPServer(address, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()


if __name__ == '__main__':
    main('localhost')
#    print __import__()
