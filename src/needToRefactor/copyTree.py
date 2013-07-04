#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-7-4

@author: lavenda
"""

import os
import shutil

def copyTree(srcPath, tagPath):
    
#    if not os.path.isdir(tagPath):
#        os.makedirs(tagPath)
#    print srcPath, tagPath
    
    try:
        shutil.copytree(srcPath, tagPath)
    except Exception, e:
        print e
        return
    print '%s ......OK' % srcPath


def parseTxt(txtFilePath):
    SOURCE_PATH = r'S:/E020DW/DWep20'
    TARGET_PATH = r'S:\E020DW\Data_ from_DW\preAsset\20130704\toMip'
    
    unHandlePathList = []
    fileStream  = open(txtFilePath, 'r')
    for line in fileStream:
        noEnterLine = line.strip()
        srcPath = os.path.join(SOURCE_PATH,noEnterLine)
        if not os.path.isdir(srcPath):
            unHandlePathList.append(srcPath)
            print '%s ......not exist'
            continue
        tagPath = os.path.join(TARGET_PATH, noEnterLine)
        copyTree(srcPath, tagPath)
    print unHandlePathList
        
if __name__ == '__main__':
    parseTxt(r'C:\Users\huangchengqi\Desktop\drgn2015\needCopyTreeToMip.txt')