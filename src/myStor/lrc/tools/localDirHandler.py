#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""

import sys

sys.path.append(r'//server-cgi/workflowtools_ep20')
sys.path.append(r'//server-cgi/workflowtools_ep20/lib')
# sys.path.append(r'D:\myPython\DW_EP20\digital37')
# sys.path.append(r'D:\myPython\DW_EP20\digital37\lib')

from odwlib.lrc.tools import baseHanlder

class LRCDirHandler(baseHanlder.BaseHandler):
    
    STANDARD_DIR_LIST = ['review', 'to_dw']

    def __init__(self):
        baseHanlder.BaseHandler.__init__(self)


    def _handlerUnStandardObj(self, unStandardObjList):
        """
        rename the unstandard file and copy them to a standard dir
        """
        baseHanlder.BaseHandler._handlerUnStandardObj(self, unStandardObjList)
        self._printAndWrite('what name suffix you want to add:')
        nameSuffix = raw_input()
        self._printAndWrite('\n\n*** IS REANMING THE FILES ***')
        for workFileObj in unStandardObjList:
            self._printAndWrite('----------------')
            self._printAndWrite(workFileObj.filePath)
            standardPath = workFileObj.renameFileName(nameSuffix)
            if standardPath:
                self._printAndWrite('-> ' + str(standardPath))
                handlerSuccessFileNameList.append(workFileObj.standardName)

        return handlerSuccessFileNameList



def main(path):
    """
    the enterance of progarm
    """
    lrcDirHandler = LRCDirHandler()
    lrcDirHandler.run(path)


if __name__ == '__main__':
   main(sys.argv[1])