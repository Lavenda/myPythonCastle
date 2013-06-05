#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-6-4

@author: lavenda
"""

import shutil
import os

class ShotFileOperation(object):

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
    def getSingleFrame(shotFile):
        """
        get first frame from the shot file
        """
        if shotFile.fileType == '.mov':
            'run get single frame'
            pass
    
    @staticmethod
    def checkShotName(shotName):
        pass

    @staticmethod
    def getShotName(srcPath):
        """
        get the shot name from the file path
        """
        return os.path.basename(srcPath)[0:17]


    @staticmethod
    def compareFiles(srcShotFile, tagShotFile):
        """
        compare the modify time and its shot name between the two shot files.
        """
        if srcShotFile.modifyTime <= tagShotFile.modifyTime:
            return False
        if srcShotFile.shotName != tagShotFile.shotName:
            return False
        return True