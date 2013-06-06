#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-6-4

@author: lavenda
"""

import shutil
import os 


    
def copyFile(srcPath, tagPath):
    """
    copy the file 
    """
    if not (os.path.isfile(srcPath) and os.path.isfile(tagPath)):
        print '%s or %s is not exist.' % (srcPath, tagPath)
        return False
    try:
        shutil.copy(srcPath, tagPath)
    except:
        print 'copyFile Error'
        return False
    return True



def removeFile(tagPath):
    """
    remove the file
    """
    if not os.path.isfile(tagPath):
        print '%s is not exist.' % tagPath
        return False
    try:
        os.remove(tagPath)
    except:
        print 'removeFile error'
        return False
    return True



def getSingleFrame(LrcFile):
    """
    get first frame from the shot file
    """
    if LrcFile.fileType == '.mov':
        'run get single frame'
        pass



def getShotCodeCaseDic():
    from odwlib.tactic.server.biz import shotBiz 
    shotBizObj = shotBiz.ShotBiz()
    shotCodeList =  shotBizObj.getShotCodeList()
    shotCodeCaseDic = {}
    for shotCode in shotCodeList:
        shotCodeCaseDic[shotCode.lower()] = shotCode
    return shotCodeCaseDic



def getShotName(srcPath):
    """
    get the shot name from the file path
    """
    fileName = os.path.basename(srcPath)
    if fileName[18] == '_':
        return fileName[0:18]
    else:
        return fileName[0:19]



def compareFiles(srcLrcFile, tagLrcFile):
    """
    compare the modify time and its shot name between the two shot files.
    """
    if srcLrcFile.modifyTime <= tagLrcFile.modifyTime:
        return False
    if srcLrcFile.shotName != tagLrcFile.shotName:
        return False
    return True



def renameFile(rootPath, srcName, tagName):
    """
    rename the file 
    """
    srcPath = os.path.join(rootPath, srcName)
    if os.path.isfile(srcPath):
        tagPath = os.path.join(rootPath, 'standard', tagName) 
        try:
            shutil.copy(srcPath, tagPath)
            pass
        except Exception, e:
            print '<%s> is error' % srcPath
            return e
        return tagPath



def copyStandardFile(rootDir, rootPath, srcName, tagName):
    
    srcPath = os.path.join(rootPath, srcName)
    if os.path.isfile(srcPath):
        tagPath = os.path.join(rootPath, tagName)
        tagPath = tagPath.replace(rootDir, rootDir+'\\standard')
        tagDir = os.path.dirname(tagPath)
        if not os.path.isdir(tagDir):
            os.makedirs(tagDir)
        try:
            shutil.copy(srcPath, tagPath)
            pass
        except Exception, e:
            print '<%s> is error' % srcPath
            return e
        return tagPath