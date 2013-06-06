#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-3-21

@author: lavenda
"""

import os
from odwlib.lrc import baseLrcFileOper

class WorkFile(object):

    def __init__(self):
        self.fileName = ''
        self.standardName = ''
        self.fileExt = ''
        self.shotName = ''
        self.sequenceName = ''
        self.filePath = ''
        self.dirPath = ''
        self.modifyTime = 0.0
    
    
    def setFile(self, filePath):
        """
        set the attributes of this object
        
        @param filePath: the file path
        @type filePath: string type
        """
        self.fileName = os.path.basename(filePath)
        self.fileExt = os.path.splitext(filePath)[1]
        self.shotName = baseLrcFileOper.getShotName(filePath)
        self.filePath = filePath
        self.dirPath = os.path.dirname(filePath)
        self.modifyTime = os.path.getmtime(filePath)
    
    
    def setStandardName(self, standardName):
        """
        set the standardName and sequenceName attribute
        
        @param standardName: the standard name of the file
        @type standardName: string type
        """
        self.standardName = self._setStandardName(standardName)
        self.sequenceName = self.standardName.split('_')[2]
    
    
    def _setStandardName(self, standardName):
        pass
    
    
    def initBeforeCopy(self, workFileAddrDic):
        """
        before the copy, have some preprocess
        @param workFileAddrDic: the address dictionary of the workFile object 
        @type workFileAddrDic: dictionary type
        """
        return workFileAddrDic
    
    
    def checkNaming(self):
        if self.fileName != self.standardName:
            return False
        return self._checkSuffixNaming()
        
        
    def _checkSuffixNaming(self):
        pass


    def renameAndCopyFileName(self, rootPath):
        """
        rename the file in this object and copy it to a standard directory
        """
        return baseLrcFileOper.copyStandardFile(rootPath, self.dirPath,
                                                self.fileName,
                                                self.standardName)



class VideoFile(WorkFile):
    """
    the video file object.
    video file contains: '.mov', '.mkv'
    """

    def __init__(self):
        WorkFile.__init__(self)
        self.pictureFile = None
    
    
    def setPictureFile(self, pictureFile):
        self.pictureFile = pictureFile


    def initBeforeCopy(self, workFileAddrDic):
        WorkFile.initBeforeCopy(self, workFileAddrDic)
        pictureSignName = self.shotName + '_picture'
        if pictureSignName in workFileAddrDic:
            self.pictureFile = workFileAddrDic[pictureSignName]
        else:
            """
            @todo: use the rv to get single frame from mov file
            """
            pass
        return workFileAddrDic
    
    
    def _setStandardName(self, standardName):
        WorkFile._setStandardName(self, standardName)
        return standardName + '_CMP' + self.fileExt
    
    
    def _checkSuffixNaming(self):
        WorkFile._checkSuffixNaming(self)
        suffixName = self.fileName[len(self.shotName):]
        if suffixName.startswith('_CMP'):
            return True
        else:
            return False



class PictureFile(WorkFile):
    """
    the picture file object.
    picture file contains: '.exr', '.tif'
    """

    def __init__(self):
        WorkFile.__init__(self)
    
    
    def _setStandardName(self, standardName):
        WorkFile._setStandardName(self, standardName)
        return standardName + '_LGT' + self.fileExt
    
    
    def _checkSuffixNaming(self):
        WorkFile._checkSuffixNaming(self)
        suffixName = self.fileName[len(self.shotName):]
        if suffixName.startswith('_LGT'):
            return True
        else:
            return False