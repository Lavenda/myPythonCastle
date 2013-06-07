#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-23

@author: lavenda
"""

from socket import *

#HOST = '192.168.16.192'
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

revc = '> '
while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)   #this module only 
    tcpCliSock.connect(ADDR)
    data = raw_input(revc)
    if not data:
        break
    tcpCliSock.send('%s\n\r' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    result = data.split('@')[0]
    format = data.split('@')[1]
    if format == 'system':
        revc = '    cmd->'
    else:
        revc = '> '
    print result.strip()
    tcpCliSock.close()
