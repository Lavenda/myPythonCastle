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



class VideoFile(WorkFile):
    """
    the video file object.
    video file contains: '.mov', '.mkv'
    """

    def __init__(self):
        WorkFile.__init__(self)



class PictureFile(WorkFile):
    """
    the picture file object.
    picture file contains: '.exr', '.jpg', '.tif'
    """

    def __init__(self):
        WorkFile.__init__(self)



class WorkFileFactory(object):

    def __init__(self):
        self.workFileDic = {}


    def createWorkFile(self, filePath):
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

        if fileSuffix in VIDEO_SUFFIX:
            return self.__createVideoFile(filePath)
        elif fileSuffix in PICTURE_SUFFIX:
            return self.__createPictureFile(filePath)
        else:
            return WorkFile()


    def __createVideoFile(self, filePath):
        """
        create the video file
        """
        shotName = baseFileOper.ShotFileOperation().getShotName(filePath)
        



    def __createPictureFile(self, filePath):
        """
        create the video file
        """
        pass