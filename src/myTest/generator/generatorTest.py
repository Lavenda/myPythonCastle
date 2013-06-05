"""
Created on 2013-5-15

@author: lavenda
"""

#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

def echo(value=None):
    print "Execution starts when 'next()' is called for the time."
    try:
        while True:
            try:
                print type(value)
                value = (yield value)
                print type(value)
                
            except Exception, e:
                value = e

    finally:
        print "Don't forget to clean up when 'close()' is called."
        

if __name__ == "__main__": 
    generator = echo(1)
    print generator.next() 
    
    print "="*3
    print generator.next() 
    
    print "="*3
    print generator.send(2) 
    
    print "="*3
    generator.throw(TypeError, "spam") 
    
    print "="*3
    print generator.close() 