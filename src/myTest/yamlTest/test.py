#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-7-16

@author: lavenda
"""

from myTest.yamlTest import author 
from myTest.yamlTest import yamlTest1 


def main():
    authorObj = author.Author()
    yamlTestObj = yamlTest1.YamlTest()
    yamlTestObj.dump(authorObj)
    

if __name__ == '__main__':
    main()