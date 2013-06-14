#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-10

@author: lavenda
"""
import sys
sys.path.append(r'//server-cgi/workflowtools_ep20')
sys.path.append(r'//server-cgi/workflowtools_ep20/lib')


import os
from odwlib.lrc.tools import localDirHandler

class QCFileHandler(localDirHandler.LRCDirHandler):
    """the lrc qc file handler"""
    
    def __init__(self):
        localDirHandler.LRCDirHandler.__init__(self)
    
    
    def _handlerUnStandardObj(self, unStandardObjList):
        """
        rename and copy the lrc qc file to two spaces
        """
        handlerErrorFilePath = []
        copyedSequenceList = []
        
        self._printAndWrite('\n\n*** IS COPYING THE FILES ***')
        workFileAddrDic = self.workFileFactory.getWorkFileAddrDic()
        for workFileObj in workFileAddrDic.values():
            self._printAndWrite('----------------')
            self._printAndWrite(workFileObj.filePath)
            resultTuple = workFileObj.copyFiles(workFileAddrDic)
            
            if workFileObj.sequenceName not in copyedSequenceList:
                copyedSequenceList.append(workFileObj.sequenceName)
                
            if resultTuple[0]:
                copyedPathList = resultTuple[1]
                
                for copyedPath in copyedPathList:
                    self._printAndWrite('-> ' + str(copyedPath))
            else:
                errorMsg = resultTuple[1]
                handlerErrorFilePath.append(workFileObj.filePath)
                self._printAndWrite('*-> ' + str(errorMsg))
        self._printList(handlerErrorFilePath, 'THESE FILES HANDLER ERROR')
        
        dwIntegrate = self.workFileFactory.getDwIntegrateDir()
        for copyedSequence in copyedSequenceList:
            batName = 'DRGN_2007_%s.bat'% copyedSequence
            batPath = os.path.join(dwIntegrate, copyedSequence, batName)
            os.popen(batPath)


def main(localPath):
    qcFileHandler = QCFileHandler()
    qcFileHandler.run(localPath)
    

if __name__ == '__main__':
    main(r'D:\test\qc\lighting\20130611')