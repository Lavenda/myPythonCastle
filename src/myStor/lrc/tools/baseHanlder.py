#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-20

@author: lavenda
"""

import os
from odwlib.lrc import baseWorkFileHandler

class BaseHandler(object):
    
    STANDARD_DIR_LIST = ['review', 'to_dw']

    def __init__(self):
        self.workFileFactory = baseWorkFileHandler.WorkFileFactory()
        self.fileStream = None


    def run(self, localPath):
        """
        1. check file(such as .mov or .exr/.tif) naming is right or 
        not in the local directory.
        2. write out a log file in the local path.
        3. rename the unstandard file
        4. copy the unstandard file has been renamed into a standard dir.
        """
        recordTxtPath = os.path.join(localPath, 'Log.txt')
        self.fileStream = open(recordTxtPath, 'w')
        filePathNotInDBList = []
        workFileObjList = []
        repeatFilePathList = []
        
        isHandleReviewDir = self._isHandleReviewDir()
        
        for rootDir, dirNameList, fileNameList in os.walk(localPath):
            

            if self._isStandardDir(rootDir):
                isStandardDir = 1
            else:
                isStandardDir = -1
                
            if isHandleReviewDir * isStandardDir == -1:
                continue
            
            for fileName in fileNameList:
                filePath = os.path.join(rootDir, fileName)
                if self.workFileFactory.isIllegalFile(fileName):
                    continue
                if not self.workFileFactory.isInDBAndGetStandardName(fileName):
                    filePathNotInDBList.append(filePath)
                    continue
                workFile = self.workFileFactory.createWorkFile(filePath)
                if workFile:
                    workFileObjList.append(workFile)
                else:
                    repeatFilePathList.append(filePath)

        unStandardObjList = self._printErrorPathAndGetIntoList(workFileObjList)
        
        if self._isStartRenameAndCopy():
            handleSuccessList = self._handleUnStandardObj(unStandardObjList)
            self._printList(handleSuccessList, 
                            title='THESE FILES ARE HANDLED SUCCESS')
        
        self._printList(filePathNotInDBList, 
                        title='THESE FILES ARE NOT IN DATABASE')
        self._printList(repeatFilePathList, 
                        title='THESE FILES ARE REPEAT')
        self.fileStream.close()
    
    
    def _isHandleReviewDir(self):
        """
        handle all files or the files in standard dir
        """
        self._printAndWrite('Do you want to handle the'
                            '[review,to_dw] directory?(yes/no):')
        answer = raw_input()
        self._printAndWrite(answer)
        if answer == 'yes' or answer == 'y':
            return 1
        else:
            return -1
    
    
    def _isStandardDir(self, dirPath):
        isStandard = False
        for standardDir in self.STANDARD_DIR_LIST:
            if dirPath.endswith(standardDir):
                print dirPath
                isStandard = True
        return isStandard
    
    
    def _printErrorPathAndGetIntoList(self, workFileObjList):
        """
        print the error file path list and add into a list
        """
        unStandardWorkFileObjList = []
        self._printAndWrite('\n\n---------------------------------------')
        self._printAndWrite('--         THE ERROR FILE PATH             --')
        self._printAndWrite('------------------------------------------')
        for workFileObj in workFileObjList:
            if not workFileObj.checkNaming():
                unStandardWorkFileObjList.append(workFileObj)
                self._printAndWrite(workFileObj.filePath)
        self._printAndWrite('---------------------------------------------')
        return unStandardWorkFileObjList


    def _isStartRenameAndCopy(self):
        """
        want to start the rename and copy to the standard dir
        """
        self._printAndWrite('Do you want to rename/copy them?(yes/no):')
        answer = raw_input()
        self._printAndWrite(answer)
        if answer == 'yes' or answer == 'y':
            return True
        else:
            return False


    def _handleUnStandardObj(self, unStandardObjList):
        """
        rename the unstandard file and copy them to a standard dir
        """
        handleSuccessFileNameList = []
    
    
    def _printAndWrite(self, string):
        """
        print into command line and write into log
        """
        print string
        try:
            self.fileStream.write(string+'\n')
        except Exception, error:
            print 'write into the log error'
            print error
    
    
    def _printList(self, pathList, title):
        """
        print the list of some file path
        """
        self._printAndWrite('\n\n-----------------------------------------')
        self._printAndWrite('--\t%s\t\t--' % title)
        self._printAndWrite('---------------------------------------------')
        for filePath in pathList:
            self._printAndWrite(filePath)
        self._printAndWrite('---------------------------------------------')