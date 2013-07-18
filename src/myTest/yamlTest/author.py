#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-7-15

@author: lavenda
"""


class Author(object):
    
    def __init__(self):
        self.aa = None
#        self.name = ''
        self.age = 0
        self.address = ''
        self.a = [1,2,3,4]
    
    def setAuthor(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
        
def main():
    pass
    

if __name__ == '__main__':
    main()
