#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-15

@author: lavenda
"""

#!/usr/bin/env python2.6
# -*- coding:uft-8 -*-

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max:
        print b 
        a, b = b, a + b 
        n = n + 1 


def fab02(max): 
    n, a, b = 0, 0, 1 
    L = [] 
    while n < max: 
        L.append(b)
        a, b = b, a + b 
        n = n + 1 
    return L 


#use iterable object for saving RAM
class Fab3(object): 

    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 
    
    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration() 


#use the yield
def fab4(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 


#use the yield, if it has return
def fab5(max): 
    n, a, b = 0, 0, 1 
    while n < max:
        yield b 
        # print b 
        a, b = b, a + b
        print 'n:%s' % n
        if n == 5:
            return 
        n = n + 1


# use the yield to read file.
def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                a = yield block
            else: 
                return


if __name__ == '__main__':
#    for n in fab5(10):
#        print n
#    for n in read_file(r'C:\Users\lavenda\Desktop\Article.uml'):
#        print n
#    assert  1==2
    pass
