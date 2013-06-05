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
        self.modifyTime = 0.0
    
    
    def setFile(self, filePath):
        self.fileName = os.path.basename(filePath)
        self.fileExt = os.path.splitext(filePath)
        self.shotName = baseLrcFileOper.LrcFileOperation.getShotName(filePath)
        self.filePath = filePath
        self.modifyTime = os.path.getmtime(filePath)
    
    
    def setStandardName(self, standardName):
        self.standardName = standardName
        self.sequenceName = self.standardName.split('_')[2]
    
    
    def initBeforeCopy(self, workFileAddrDic):
        return workFileAddrDic
    
    
    def checkNaming(self):
        if self.shotName != self.standardName:
            return False
        return self._checkSuffixNaming()
        
        
    def _checkSuffixNaming(self):
        pass
    


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
        pictureSignName = self.shotName + '_picture'
        if pictureSignName in workFileAddrDic:
            self.pictureFile = workFileAddrDic[pictureSignName]
        else:
            """
            @todo: use the rv to get single frame from mov file
            """
            pass
        return workFileAddrDic
    
    
    def _checkSuffixNaming(self):
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
    
    
    def _checkSuffixNaming(self):
        suffixName = self.fileName[len(self.shotName):]
        if suffixName.startswith('_LGT'):
            return True
        else:
            return False