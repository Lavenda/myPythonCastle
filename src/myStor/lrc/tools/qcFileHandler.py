#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-10

@author: lavenda
"""
import sys
sys.path.append(r'//server-cgi/workflowtools_ep20')
sys.path.append(r'//server-cgi/workflowtools_ep20/lib')
# sys.path.append(r'D:\myPython\DW_EP20\digital37')
# sys.path.append(r'D:\myPython\DW_EP20\digital37\lib')

import os
import subprocess
from odwlib.lrc.tools import baseHanlder

class QCFileHandler(baseHanlder.BaseHandler):
    """the lrc qc file handler"""
    
    def __init__(self):
        baseHanlder.BaseHandler.__init__(self)
    
    
    def _handlerUnStandardObj(self, unStandardObjList):
        """
        rename and copy the lrc qc file to two spaces
        """
        baseHanlder.BaseHandler._handlerUnStandardObj(self, unStandardObjList)
        handlerErrorFilePath = []
        copyedSequenceList = []
        
        self._printAndWrite('\n\n*** IS COPYING THE FILES ***')
        workFileAddrDic = self.workFileFactory.getWorkFileAddrDic()
        for workFileObj in workFileAddrDic.values():
            self._printAndWrite('----------------')
            self._printAndWrite(workFileObj.filePath)
            resultTuple = workFileObj.copyFiles(workFileAddrDic)
            
            
                
            if resultTuple[0]:
                if workFileObj.sequenceName not in copyedSequenceList:
                    copyedSequenceList.append(workFileObj.sequenceName)
                copyedPathList = resultTuple[1]
                
                for copyedPath in copyedPathList:
                    self._printAndWrite('-> ' + str(copyedPath))
                handlerSuccessFileNameList.append(workFileObj.standardName)
            else:
                errorMsg = resultTuple[1]
                handlerErrorFilePath.append(workFileObj.filePath)
                self._printAndWrite('*-> ' + str(errorMsg))
        self._printList(handlerErrorFilePath, 'THESE FILES HANDLER ERROR')
        
        dwIntegrate = self.workFileFactory.getDwIntegrateDir()

        self._runNukeBat(copyedSequenceList, dwIntegrate)
        return handlerSuccessFileNameList


    def _runNukeBat(self, sequenceList, dwIntegrate):
        self._printAndWrite('\n\n-----------------------------------------')
        self._printAndWrite('--        RUNNING THE NUKE BAT           --')
        self._printAndWrite('------------------------------------------')
        for sequence in sequenceList:
            self._printAndWrite('%s:\n' % sequence)
            batName = 'DRGN_2007_%s.bat' % sequence
            batPath = os.path.join(dwIntegrate, sequence, batName)
            popen = subprocess.Popen(batPath, stdout=subprocess.PIPE)
            result = popen.read().strip()
            self._printAndWrite(result)
        self._printAndWrite('------------------------------------------')



def main(localPath):
    qcFileHandler = QCFileHandler()
    qcFileHandler.run(localPath)
    

if __name__ == '__main__':
    main(sys.argv[1])