#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-6-4

@author: lavenda
"""

import shutil
import os 

class LrcFileOperation(object):

    def __init__(self):
        pass


    @staticmethod
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


    @staticmethod
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


    @staticmethod
    def getSingleFrame(LrcFile):
        """
        get first frame from the shot file
        """
        if LrcFile.fileType == '.mov':
            'run get single frame'
            pass
    
    
    @staticmethod
    def getShotCodeCaseDic():
        from odwlib.tactic.server.biz import shotBiz 
        shotBizObj = shotBiz.ShotBiz()
        shotCodeList =  shotBizObj.getShotCodeList()
        shotCodeCaseDic = {}
        for shotCode in shotCodeList:
            shotCodeCaseDic[shotCode.lower()] = shotCode
        return shotCodeCaseDic
    
    
    @staticmethod
    def getShotName(srcPath):
        """
        get the shot name from the file path
        """
        fileName = os.path.basename(srcPath)
        if fileName[18] == '_':
            return fileName[0:18]
        else:
            return fileName[0:19]
    
    
    @staticmethod
    def compareFiles(srcLrcFile, tagLrcFile):
        """
        compare the modify time and its shot name between the two shot files.
        """
        if srcLrcFile.modifyTime <= tagLrcFile.modifyTime:
            return False
        if srcLrcFile.shotName != tagLrcFile.shotName:
            return False
        return True