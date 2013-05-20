'''
Created on 2013-5-20

@author: lavenda
'''
#!/usr/bin/env python2.6
# -*-coding:utf-8-*-

from socket import *
from time import sleep

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
    sleep(5)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
