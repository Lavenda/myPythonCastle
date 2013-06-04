"""
Created on 2013-3-21

@author: lavenda
"""

#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

import os
import baseFileOper

class WorkFile(object):

    def __init__(self):
        self.fileName = ''
        self.standardName = ''
        self.fileSuffix = ''
        self.shotName = ''
        self.sequenceName = ''
        self.filePath = ''
        self.modifyTime = 0.0


    def setFile(self, filePath):
        self.fileName = os.path.basename(filePath)
        self.fileSuffix = os.path.splitext(filePath)
        self.shotName = baseFileOper.ShotFileOperation().getShotName(filePath)
        self.sequenceName = self.shotName.split('_')[2]
        self.filePath = filePath
        self.modifyTime = os.path.getmtime(filePath)


    def initBeforeCopy(self, workFileAddrDic):
        return workFileAddrDic


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
        videoSignName = self.shotName + '_video'
        pictureSignName = self.shotName + '_picture'
        if pictureSignName in workFileAddrDic:
            self.pictureFile = workFileAddrDic[pictureSignName]
        else:
            """
            @todo: use the rv to get single frame from mov file
            """
            pass
        return workFileAddrDic




class PictureFile(WorkFile):
    """
    the picture file object.
    picture file contains: '.exr', '.jpg', '.tif'
    """

    def __init__(self):
        WorkFile.__init__(self)



class WorkFileFactory(object):


    def __init__(self):
        self.workFileAddrDic = {}
        self.signName = ''


    def addWorkFileIntoAddrDic(self, filePath):
        """
        create workFile object by different file type.

        @param filePath: the file path
        @type filePath: string type

        @return: a WorkFile object or its subclass
        """
        VIDEO_SUFFIX = ['.mov', '.mkv']
        PICTURE_SUFFIX = ['.exr', '.jpg', '.tif']

        fileSuffix = os.path.splitext(filePath)
        fileSuffix = fileSuffix.lower()
        shotName = baseFileOper.ShotFileOperation().getShotName(filePath)


        if (fileSuffix in VIDEO_SUFFIX and 
            self.__isRepeatInAddrDic(shotName, '_video')):
            workFile = VideoFile()
        elif (fileSuffix in PICTURE_SUFFIX and 
              self.__isRepeatInAddrDic(shotName, '_picture')):
            workFile = PictureFile()
        else:
            workFile = None

        if workFile:
            self.workFileAddrDic[self.signName] = workFile


    def __isRepeatInAddrDic(self, shotName, fileType):
        self.signName = shotName + fileType
        if self.signName in self.workFileAddrDic:
            return False
        else:
            return True


    def getWorkFileAddrDic(self):
        return self.workFileAddrDic