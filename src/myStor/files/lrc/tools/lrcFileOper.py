#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

"""
Created on 2013-6-4

@author: lavenda
"""

import os
import time
from odwlib.lrc import workFileData

class LrcQcOperation(object):
    """
    docstring for LrcQcOperation
    """

    LIGHTING_QC_ROOT_PATH = 'D:/test/qc/lighting'
    DW_APPROVED_SEQUENCE_PENDING = ('D:/test/QC/lighting/'
                                    'DW_approved/DRGN_2007/Sequence/Pending')
    DW_APPROVED_SINGLE_FRAME_PENDING = ('D:/test/QC/lighting/DW_approved'
                                        '/DRGN_2007/Single_Frame/Pending')

    def __init__(self):
        pass


    def run(self, dealedDate=None):
        """
        the sign of the progarms start

        @param dealedDate: a date string, likes 20121212.
        @type dealedDate: string type(default:None)
        """
        dealedPath = self.__getDealedPath(dealedDate)
        workFileAddrDic = self._getAllWorkFileAddrDic(dealedPath)

        for signName, workFile in workFileAddrDic.items():
            workFileAddrDic = workFile.initBeforeCopy(workFileAddrDic)
            
            print workFileAddrDic
#            workFile.checkBeforeCopy()
#            workFile.copyToTarget()


    def __getDealedPath(self, dealedDate):
        if not dealedDate:
            dealedDate = time.strftime('%Y%m%d',time.localtime(time.time()))
        if len(dealedDate) == 8:
            return os.path.join(self.LIGHTING_QC_ROOT_PATH, dealedDate)


    def _getAllWorkFileAddrDic(self, dealedDatePath):
        workFileFactory = workFileData.WorkFileFactory()

        for rootDir, dirList, fileList in os.walk(dealedDatePath):
            for fileName in fileList:
                filePath = os.path.join(rootDir, fileName)
                workFileFactory.addWorkFileIntoAddrDic(filePath)

        return workFileFactory.getWorkFileAddrDic()