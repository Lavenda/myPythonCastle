#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-6-4

@author: lavenda
"""

import shutil
import os 
from odwlib.rv import rvio

    
def copyFile(srcPath, tagPath):
    """
    copy the file 
    
    @param srcPath: the path of the source file you want to copy
    @type srcPath: string type
    @param tagPath: the path of the target file where you want to copy to
    @type srcPath: string type
    
    @return: copy success or not
    @rtype: boolean type
    """
    tagDirPath = os.path.dirname(tagPath)
    if not os.path.isfile(srcPath):
        msg = '%s is not exist.' % srcPath
        print msg
        return False, msg
    if not os.path.isdir(tagDirPath):
        os.makedirs(tagDirPath)
    try:
        shutil.copy(srcPath, tagPath)
    except Exception, errorMsg:
        return False, str(errorMsg)
    return True, None



def removeFile(tagPath):
    """
    remove the file
    """
    if not os.path.isfile(tagPath):
        print '%s is not exist.' % tagPath
        return False
    try:
        os.remove(tagPath)
    except Exception, errorMsg:
        print errorMsg
        return False, errorMsg
    return True, ''



def getSingleFrame(videoFilePath, tagFilePath):
    """
    get first frame from the shot file
    """
    isSuccess = False
    fileExt = os.path.splitext(videoFilePath)[1]
    if fileExt == '.mov':
        try:
            isSuccess = rvio.getImageFromMov(inMov=videoFilePath, outImage=tagFilePath)
        except Exception, errorMsg:
            print errorMsg
            return False, errorMsg
    return isSuccess, ''


def getShotName(srcPath):
    """
    get the shot name from the file path
    """
    fileName = os.path.basename(srcPath)
    if fileName[18] == '_':
        return fileName[0:18]
    else:
        return fileName[0:19]



def compareFiles(srcFileModifyTime, tagFilePath):
    """
    compare the modify time and its shot name between the two shot files.
    """
    
    if srcFileModifyTime <= os.path.getmtime(tagFilePath):
        return False
    else:
        return True



def renameFile(rootPath, srcName, tagName):
    """
    rename the file 
    """
    srcPath = os.path.join(rootPath, srcName)
    if os.path.isfile(srcPath):
        tagPath = srcPath.replace(srcName, tagName)
        try:
            shutil.move(srcPath, tagPath)
        except Exception, errorMsg:
            print '<%s> is error' % srcPath
            return errorMsg
        return tagPath


def getSubmitPersonName(fileName):
    """
    get a person name from a submit file
    """
    fileNameExceptExt = os.path.splitext(fileName)[0]
    return fileNameExceptExt.split("_")[-1]

