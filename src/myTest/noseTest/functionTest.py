#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-6-3

@author: lavenda
"""


import nose

def setup_func():
    "set up test fixtures"
    print 'setup_func'

def teardown_func():
    "tear down test fixtures"
    print 'teardown_func'

@nose.with_setup(setup_func, teardown_func)
def testAA():
    "test ..."
    print 'test'
    

if __name__ == '__main__':
    nose.run()