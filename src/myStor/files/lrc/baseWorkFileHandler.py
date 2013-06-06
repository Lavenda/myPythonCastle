#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-3-21

@author: lavenda
"""

import os
from odwlib.lrc import baseLrcFileOper
from odwlib.lrc import workFileData

class WorkFileFactory(object):
        
        
    VIDEO_EXT = ['.mov']
    PICTURE_TEX = ['.exr', '.tif']
    ILLEGAL_DIR = ['review', 'to_dw']
    
    
    def __init__(self):
        self.workFileAddrDic = {}
        self.signName = ''
        self.shotCodeCaseDic = baseLrcFileOper.getShotCodeCaseDic()
    
    
    def createWorkFile(self, filePath):
        """
        create workFile object by different file type.

        @param filePath: the file path
        @type filePath: string type

        @return: a WorkFile object or its subclass
        """
        fileExt = self._getFileExt(filePath)
        shotName = self.isInDBAndGetStandardName(filePath)
        if not shotName:
            return None
        
        if (fileExt in self.VIDEO_EXT and 
            self._isRepeatInAddrDic(shotName, '_video')):
            workFile = workFileData.VideoFile()
        elif (fileExt in self.PICTURE_TEX and 
              self._isRepeatInAddrDic(shotName, '_picture')):
            workFile = workFileData.PictureFile()
        else:
            workFile = None
        if workFile:
            workFile.setFile(filePath)
            workFile.setStandardName(shotName)
            self.workFileAddrDic[self.signName] = workFile
        return workFile
    
    
    def _getFileExt(self, filePath):
        """
        get the extension name from filePath
        """
        fileExt = os.path.splitext(filePath)
        fileExt = fileExt[1].lower()
        return fileExt
    
    
    def isInDBAndGetStandardName(self, filePath):
        """
        check this file is exist in the database or not.
        """
        shotName = baseLrcFileOper.getShotName(filePath)
        return self.shotCodeCaseDic.get(shotName.lower(), None)
    
    
    def _isRepeatInAddrDic(self, shotName, fileType):
        """
        check this object is exist in the object address dictionary or not
        """
        self.signName = shotName + fileType
        return self.signName not in self.workFileAddrDic
    
    
    def isIllegalFileAndDir(self, fileName, dirName):
        """
        check this file or directory is illegal or not
        """
        upperDir = dirName.split('\\')[-1]
        if upperDir in self.ILLEGAL_DIR:
            return True
        fileExt = self._getFileExt(fileName)
        if fileExt not in (self.PICTURE_TEX + self.VIDEO_EXT):
            return True
        else:
            return False
    
    def getWorkFileAddrDic(self):
        """
        get the Workfile object address dictionary
        """
        return self.workFileAddrDic


if __name__ == '__main__':
    pass