#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""

import os
from odwlib.lrc import baseWorkFileHandler

def checkLocalDirNaming(localPath):
    """
    check file(such as .mov or .exr/.tif) naming in the local directory
    """
    workFileFactory = baseWorkFileHandler.WorkFileFactory()
    unStandardFileName = []
    workFileObjList = []
    
    for rootDir, dirNameList, fileNameList in os.walk(localPath):
        for fileName in fileNameList:
            filePath = os.path.join(rootDir, fileName)
            if workFileFactory.isIllegalFile(fileName):
                continue
            workFile = workFileFactory.createWorkFile(filePath)
            if workFile:
                workFileObjList.append(workFile)
            else:
                unStandardFileName.append(filePath)
                
    for workFileObj in workFileObjList:
        if not workFileObj.checkNaming():
            print workFileObj.filePath
    

if __name__ == '__main__':
    checkLocalDirNaming(r'D:\test\qc\lighting\20130605')