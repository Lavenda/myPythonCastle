#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""

import os
from odwlib.lrc import baseWorkFileHandler

class CheckLocalDirNaming(object):

    def __init__(self):
        self.workFileFactory = baseWorkFileHandler.WorkFileFactory()


    def run(self, localPath):
        """
        check file(such as .mov or .exr/.tif) naming is right or 
        not in the local directory
        """
        
        filePathNotInDB = []
        workFileObjList = []
        
        for rootDir, dirNameList, fileNameList in os.walk(localPath):
            for fileName in fileNameList:
                filePath = os.path.join(rootDir, fileName)
                if self.workFileFactory.isIllegalFile(fileName):
                    continue
                workFile = self.workFileFactory.createWorkFile(filePath)
                if workFile:
                    workFileObjList.append(workFile)
                else:
                    filePathNotInDB.append(filePath)

        unStandardObjList = self.__printErrorPathAndGetIntoList(workFileObjList)
        
        print 'Do you want to rename them?(yes/no):'
        answer = raw_input()
        if answer == 'yes' or answer == 'y':
            self.__renameUnStandardObj(unStandardObjList)
        
        self.__printFileNameNotInDB(filePathNotInDB)


    def __printErrorFilePathAndGetIntoList(self, workFileObjList):
        unStandardWorkFileObjList = []
        print '---------------------------------------------'
        print '--         THE ERROR FILE PATH             --'
        print '---------------------------------------------'
        for workFileObj in workFileObjList:
            if not workFileObj.checkNaming():
                unStandardWorkFileObjList.append(workFileObj)
                print workFileObj.filePath
        print '---------------------------------------------'
        return unStandardWorkFileObjList


    def __renameUnStandardObj(self, unStandardObjList):
        print '*** IS REANMING THE FILES ***'
        for workFileObj in unStandardObjList:
            print '---'
            wrokFileObj.renameFileName()


    def __printFileNameNotInDB(self, filePathNotInDB):
        print '---------------------------------------------'
        print '--    THESE FILE NAME NOT IN DATABASE     --'
        print '---------------------------------------------'
        for filePath in filePathNotInDB:
            print filePath
        print '---------------------------------------------'


def main(path):
    checkLocalDirNaming = CheckLocalDirNaming()
    checkLocalDirNaming.run(path)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])