#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-20

@author: lavenda
"""

from socket import *
from time import sleep

#HOST = '192.168.16.192'
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)   #this module only 
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\n\r' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
