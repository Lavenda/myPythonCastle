#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-3-21

@author: lavenda
"""

import os
from odwlib.lrc import baseLrcFileOper
from odwlib.lrc import workFileData
from odwlib.unitTest import myPyUnit

class WorkFileFactory(object):
        
        
    VIDEO_EXT = ['.mov']
    PICTURE_TEX = ['.exr', '.tif']
    
    
    def __init__(self):
        self.workFileAddrDic = {}
        self.signName = ''
        self.shotCodeCaseDic = baseLrcFileOper.LrcFileOperation.getShotCodeCaseDic()
    
    
    def createWorkFile(self, filePath):
        """
        create workFile object by different file type.

        @param filePath: the file path
        @type filePath: string type

        @return: a WorkFile object or its subclass
        """
        fileExt = self._getFileExt(filePath)
        shotName = baseLrcFileOper.LrcFileOperation.getShotName(filePath)
        shotName = self.__checkIsInDBAndGetStandardName(shotName)
        if not shotName:
            return None
        
        if (fileExt in self.VIDEO_EXT and 
            self.__isRepeatInAddrDic(shotName, '_video')):
            workFile = workFileData.VideoFile()
        elif (fileExt in self.PICTURE_TEX and 
              self.__isRepeatInAddrDic(shotName, '_picture')):
            workFile = workFileData.PictureFile()
        else:
            workFile = None
        if workFile:
            workFile.setStandardName(shotName)
            workFile.setFile(filePath)
            self.workFileAddrDic[self.signName] = workFile
        return workFile
    
    
    def _getFileExt(self, filePath):
        fileExt = os.path.splitext(filePath)
        fileExt = fileExt[1].lower()
        return fileExt
    
    
    def __checkIsInDBAndGetStandardName(self, shotName):
        return self.shotCodeCaseDic.get(shotName.lower(), None)
    
    
    def __isRepeatInAddrDic(self, shotName, fileType):
        self.signName = shotName + fileType
        return self.signName not in self.workFileAddrDic
    
    
    def isIllegalFile(self, fileName):
        fileExt = self._getFileExt(fileName)
        if fileExt not in (self.PICTURE_TEX + self.VIDEO_EXT):
            return True
        else:
            return False
    
    def getWorkFileAddrDic(self):
        return self.workFileAddrDic

if __name__ == '__main__':
    myPyUnit.run(globals())