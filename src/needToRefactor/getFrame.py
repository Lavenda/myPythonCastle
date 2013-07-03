#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-7-3

@author: lavenda
"""
import os
import re

def getFrameInfo(filePath):
    logPath = r'D:/frameInfo.txt'
    FARME_RE = '\tsetAttr.*"playbackOptions -min ([0-9]{2,3}) -max ([0-9]{2,3}) -as.*'
    fileExt = '_LAY.ma'
    shotFrameInfoDic = {}
    
    for rootDir, dirs, files in os.walk(filePath):
        for file in files:
            if not file.endswith(fileExt):
                continue
            print file
            filePath = os.path.join(rootDir, file)
            fileStream = open(filePath, 'r')
            for line in fileStream:
                reResult = re.findall(FARME_RE, line)
                if reResult:
                    shotFrameInfoDic[file] = reResult[0]
            fileStream.close()
    
    fileStream = open(logPath, 'w')
    fileStream.write('shotName\tstartFrame\tendFrame')
    for shotName, frameInfo in shotFrameInfoDic.items():
        if not frameInfo:
            continue
        shotName = shotName.replace('_LAY.ma','')
        context = '%s\t%s\t%s' % (shotName, frameInfo[0], frameInfo[1])
        fileStream.write(context+'\n')
    fileStream.close()
        
    print shotFrameInfoDic
    
if __name__ == '__main__':
    getFrameInfo(r'S:\E020DW\DWep20\_episodes\drgn_2015')