#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""

import sys
sys.path.append(r'//server-cgi/workflowtools_ep20')
sys.path.append(r'//server-cgi/workflowtools_ep20/lib')
#sys.path.append(r'D:\myPython\DW_EP20\digital37')
#sys.path.append(r'D:\myPython\DW_EP20\digital37\lib')


import os
from odwlib.lrc import baseWorkFileHandler

class CheckLocalDirNaming(object):

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
        
        for rootDir, dirNameList, fileNameList in os.walk(localPath):
            for fileName in fileNameList:
                
                filePath = os.path.join(rootDir, fileName)
                if self.workFileFactory.isIllegalFileAndDir(fileName, rootDir):
                    continue
                if not self.workFileFactory.isInDBAndGetStandardName(filePath):
                    filePathNotInDBList.append(filePath)
                    continue
                workFile = self.workFileFactory.createWorkFile(filePath)
                if workFile:
                    workFileObjList.append(workFile)
                else:
                    repeatFilePathList.append(filePath)

        unStandardObjList = self.__printErrorFilePathAndGetIntoList(workFileObjList)
        
        if self.__isStartRenameAndCopy():
            self.__renameAndCopyUnStandardObj(unStandardObjList, localPath)
        
        self.__printFilePathNotInDB(filePathNotInDBList)
        self.__printRepeatFilePathList(repeatFilePathList)
        self.fileStream.close()


    def __printErrorFilePathAndGetIntoList(self, workFileObjList):
        """
        print the error file path list and add into a list
        """
        unStandardWorkFileObjList = []
        self.__printAndWrite('\n\n---------------------------------------')
        self.__printAndWrite('--         THE ERROR FILE PATH             --')
        self.__printAndWrite('------------------------------------------')
        for workFileObj in workFileObjList:
            if not workFileObj.checkNaming():
                unStandardWorkFileObjList.append(workFileObj)
                self.__printAndWrite(workFileObj.filePath)
        self.__printAndWrite('---------------------------------------------')
        return unStandardWorkFileObjList


    def __isStartRenameAndCopy(self):
        """
        want to start the rename and copy to the standard dir
        """
        self.__printAndWrite('Do you want to rename them?(yes/no):')
        answer = raw_input()
        self.__printAndWrite(answer)
        if answer == 'yes' or answer == 'y':
            return True
        else:
            return False

    def __renameAndCopyUnStandardObj(self, unStandardObjList, rootPath):
        """
        rename the unstandard file and copy them to a standard dir
        """
        self.__printAndWrite('\n\n*** IS REANMING THE FILES ***')
        for workFileObj in unStandardObjList:
            self.__printAndWrite('----------------')
            self.__printAndWrite(workFileObj.filePath)
            standardPath = workFileObj.renameFileName(rootPath)
            if standardPath:
                self.__printAndWrite('-> ' + str(standardPath))


    def __printFilePathNotInDB(self, filePathNotInDBList):
        """
        print the files not in database to command line and write into log
        """
        self.__printAndWrite('\n\n-----------------------------------------')
        self.__printAndWrite('--  THESE FILES ARE NOT IN DATABASE   --')
        self.__printAndWrite('---------------------------------------------')
        for filePath in filePathNotInDBList:
            self.__printAndWrite(filePath)
        self.__printAndWrite('---------------------------------------------')
        
        
    def __printRepeatFilePathList(self, repeatFilePathList):
        """
        print the repeat files to command line and write into log
        """
        self.__printAndWrite('\n\n-----------------------------------------')
        self.__printAndWrite('--      THESE FILES ARE REPEAT       --')
        self.__printAndWrite('---------------------------------------------')
        for filePath in repeatFilePathList:
            self.__printAndWrite(filePath)
        self.__printAndWrite('---------------------------------------------')
        
    
    def __printAndWrite(self, string):
        """
        print into command line and write into log
        """
        print string
        try:
            self.fileStream.write(string+'\n')
        except Exception, e:
            print 'write into the log error'
            print e
        


def main(path):
    """
    the enterance of progarm
    """
    checkLocalDirNaming = CheckLocalDirNaming()
    checkLocalDirNaming.run(path)


if __name__ == '__main__':
    main(sys.argv[1])