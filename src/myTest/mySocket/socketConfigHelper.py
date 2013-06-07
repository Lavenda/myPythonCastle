#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-23

@author: lavenda
"""

import os
from xml.dom import minidom

class SocketConfigHelper(object):
    
    def __init__(self):
        self.root = self.__getRootNode()
    
    
    def __getRootNode(self):
        xmlPath = os.path.dirname(__file__)+'/socketConfig.xml'
        document = minidom.parse(xmlPath)
        root = document.documentElement
        return root
    
    
    def getGoalByHint(self, hint):
        socketDataNodeList = self.root.getElementsByTagName('socketData')
        
        for socketDataNode in socketDataNodeList:
            hintNode = socketDataNode.getElementsByTagName('hint')[0]
            hintNodeValue = hintNode.firstChild.nodeValue
            uhint = hint.decode('utf-8')
            print len(uhint), len(hintNodeValue)
            if not uhint == hintNodeValue:
                continue
            importValueNode = socketDataNode.getElementsByTagName('import')[0]
            importValue = importValueNode.firstChild.nodeValue
            goalNode = socketDataNode.getElementsByTagName('goal')[0]
            goalType = goalNode.getAttribute('type')
            goalValue = goalNode.firstChild.nodeValue
            print importValue, goalType, goalValue
            return importValue, goalType, goalValue
        return None, None, None

if __name__ == '__main__':
    sch = SocketConfigHelper()
    sch.getGoalByhint('system')