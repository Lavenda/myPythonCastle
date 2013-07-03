#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-3-21

@author: lavenda
"""

import os, shutil

def renameFile(dirPath, fileSuffix, srcStr, targetStr):
    """
    Rename all the files that it's suffix is 'fileSuffix' in the dirPath.
    Replace the string from srcStr to targetStr.
    
    @param dirPath: the source directory path.
    @type dirPath: string type
    @param fileSuffix: the suffix of files, eg: .ma, .txt
    @type fileSuffix: string type
    @param srcStr: the original string which you want to replace.
    @type srcStr: string type
    @param targetStr: the target string that you want to 
    @type targetStr: string type
    
    """
    for root, dirs, files in os.walk( dirPath ):
        for file in files:
            if not file.endswith(fileSuffix):
                continue
            filePath = os.path.join(root, file)
            
            suitableFile = file.replace(srcStr, targetStr)
            fileSuitableFilePath = os.path.join(root, suitableFile)
            
            shutil.move(filePath, fileSuitableFilePath)


if __name__ == '__main__':
    renameFile(r'S:\E020DW\Data_ from_DW\preAsset\20130703\_assets', '.ma', 
               '_TEX', '_TEX_HI')