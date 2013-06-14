#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-3-21

@author: lavenda
"""

import os
from odwlib.lrc import baseLrcFileOper


class WorkFile(object):
    """the file object"""
    
    namingSuffix = ''
    
    sequenceDir = ('//server-cgi/qc/lighting/DW_approved'
                       '/DRGN_2007/Sequence')
    singleFrameDir = ('//server-cgi/qc/lighting/DW_approved'
                          '/DRGN_2007/Single_Frame')
    dwIntegrate = ('//server-cgi/qc/lighting/DW_Integrate'
                   '/Single_Frame/frames/DRGN_2007')
    
    
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
        self.standardName = standardName + self.namingSuffix + self.fileExt
        self.sequenceName = self.standardName.split('_')[2]
    
    
    def checkNaming(self):
        """
        check the file name is standard or not
        """
        if self.fileName != self.standardName:
            return False
        suffixName = self.fileName[len(self.shotName):]
        if suffixName.startswith(self.namingSuffix):
            return True
        else:
            return False


    def renameFileName(self, nameSuffix):
        """
        rename the file in this object and copy it to a standard directory
        """
        if nameSuffix:
            fileBaseName = os.path.splitext(self.standardName)[0]
            tagFileName = fileBaseName + '_' + nameSuffix + self.fileExt
        else:
            tagFileName = self.standardName
        return baseLrcFileOper.renameFile(self.dirPath, self.fileName,
                                         tagFileName)
    
    
    def copyFiles(self, workFileAddrDic):
        """
        copy the files
        @param workFileAddrDic: the L{WorkFile} object addres dictionary
        @type workFileAddrDic: a dictionary type.
        @return: boolean type, list type
        """
        self._preprocessBeforeCopy(workFileAddrDic)
        return True, []
    
    
    def _preprocessBeforeCopy(self, workFileAddrDic):
        """
        before the copy, have some preprocess
        @param workFileAddrDic: the address dictionary of the workFile object 
        @type workFileAddrDic: dictionary type
        """
        pass



class VideoFile(WorkFile):
    """
    the video file object.
    video file contains: '.mov'
    """
    namingSuffix = '_CMP'
    
    def __init__(self):
        WorkFile.__init__(self)
        self.hasFrameFile = True

    
    def copyFiles(self, workFileAddrDic):
        WorkFile.copyFiles(self, workFileAddrDic)
        
        videoTagPath, pictureTagPath = self._chooseAndCompareFile()
        if not (videoTagPath and pictureTagPath):
            return False, '-> this file is not the lastest version.'
        
        if not baseLrcFileOper.copyFile(self.filePath, videoTagPath):
            return False, '-> copy file error'
        
        if self.hasFrameFile:
            return True, [videoTagPath]
        
        if baseLrcFileOper.getSingleFrame(videoTagPath, pictureTagPath):
            pictureStandardName = os.path.basename(pictureTagPath)
            framesPath = os.path.join(self.dwIntegrate, self.sequenceName,
                                      pictureStandardName)
            
            if not baseLrcFileOper.copyFile(pictureTagPath, framesPath):
                return False, '-> copy file error' 
            
            return True, [videoTagPath, '->'+pictureTagPath, '->'+framesPath]
        else:
            return False, '-> get Single Frame error'
    
    
    def _chooseAndCompareFile(self):
        pictureStandardName = self.standardName.replace(self.namingSuffix, 
                                                    PictureFile.namingSuffix)
        pictureStandardName = pictureStandardName.replace(self.fileExt,
                                                          '.tga')
        dirName = 'approved'
        
        videoTagPath = os.path.join(self.sequenceDir, dirName, 
                                    self.standardName)
        
        if not (os.path.isfile(videoTagPath) and 
                baseLrcFileOper.compareFiles(self.modifyTime, videoTagPath)):
            dirName = 'pending'
            videoTagPath = os.path.join(self.sequenceDir, dirName, 
                                            self.standardName)
            if (os.path.isfile(videoTagPath) and 
                not baseLrcFileOper.compareFiles(self.modifyTime, 
                                                 videoTagPath)):
                return None, None
            
        pictureTagPath = os.path.join(self.singleFrameDir, dirName, 
                                      pictureStandardName)
        return videoTagPath, pictureTagPath
    
    
    def _preprocessBeforeCopy(self, workFileAddrDic):
        WorkFile._preprocessBeforeCopy(self, workFileAddrDic)
        baseName = os.path.splitext(self.standardName)[0]
        baseName = baseName.split(self.namingSuffix)[0]
        pictureSignName = baseName + '_picture'
        
        if not pictureSignName in workFileAddrDic:
            self.hasFrameFile = False



class PictureFile(WorkFile):
    """
    the picture file object.
    picture file contains: '.exr', '.tif'
    """
    namingSuffix = '_LGT'
    
    def __init__(self):
        WorkFile.__init__(self)
    
    
    def copyFiles(self, workFileAddrDic):
        WorkFile.copyFiles(self, workFileAddrDic)
        
        pendingPath = self._chooseAndCompareFile()
        if not pendingPath:
            return False, '-> this file is not the lastest version.'
        resultTupleFrist = self._compareAndCopyFile(self.filePath, 
                                                     pendingPath)
        if not resultTupleFrist[0]:
            return False, resultTupleFrist[1]
            
        dwIntegratePath = os.path.join(self.dwIntegrate, 
                                       self.sequenceName,
                                       self.standardName)
        resultTupleSecond = self._compareAndCopyFile(self.filePath, 
                                                      dwIntegratePath)
        if not resultTupleSecond[0]:
            return False, '%s\n%s' % (resultTupleFrist[1], 
                                      resultTupleSecond[1])
        
        return True, [resultTupleFrist[1], resultTupleSecond[1]]
        
        
    def _chooseAndCompareFile(self):
        dirName = 'approved'
        pictureTagPath = os.path.join(self.singleFrameDir, dirName, 
                                    self.standardName)
        if not (os.path.isfile(pictureTagPath) and 
                baseLrcFileOper.compareFiles(self.modifyTime, pictureTagPath)):
            dirName = 'pending'
            pictureTagPath = os.path.join(self.singleFrameDir, dirName, 
                                          self.standardName)
            if (os.path.isfile(pictureTagPath) and 
                not baseLrcFileOper.compareFiles(self.modifyTime, 
                                                 pictureTagPath)):
                return None
        return pictureTagPath
    
        
    def _compareAndCopyFile(self, srcPath, tagPathPlaned):
        fileExtList = ['.exr', '.tif', '.tga', '.jpg']
        tagFilePathList = []
        tagPathExceptExt = os.path.splitext(tagPathPlaned)[0]
        
        for fileExt in fileExtList:
            tmpTagPath = tagPathExceptExt + fileExt
            if os.path.isfile(tmpTagPath):
                tagFilePathList.append(tmpTagPath)
        
        isLatter = True
        for tagFilePath in tagFilePathList:
            if not os.path.isfile(tagFilePath):
                continue
            
            if baseLrcFileOper.compareFiles(self.modifyTime, tagFilePath):
                if baseLrcFileOper.removeFile(tagFilePath):
                    return False, '-> remove file error'
            else:
                isLatter = False
                
        if not isLatter:
            return False, '-> this file is not the lastest version.'
        
        if baseLrcFileOper.copyFile(srcPath, tagPathPlaned):
            return True, tagPathPlaned
        else:
            return False, '-> copy file error'
