#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2013-5-3

@author: lavenda
'''

import os, sys

def getNameList(localPath):
    """
    get the file list in local directory
    """
    # localPath = os.path.dirname(sys.argv[0])
    txtFilePath = os.path.join(localPath, 'element.txt')
    
    try:
        fileStream = open(txtFilePath,'w')
        for element in os.listdir(localPath):
            elementPath = os.path.join(localPath,element)
            if os.path.isfile(elementPath):
                print element
                basename = os.path.basename(element)
                basename = os.path.splitext(basename)[0]
                fileStream.write(basename+'\n')
    except:
        print 'write into file error'
    finally:
        fileStream.close()
#    print localPath
    

if __name__ == '__main__':
    localPath = sys.argv[1]
    print localPath
    getNameList(localPath)
    
