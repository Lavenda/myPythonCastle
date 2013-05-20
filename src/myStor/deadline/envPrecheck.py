"""
Created on 2013-5-13

@author: lavenda
"""

#!/usr/bin/env python2.6
# -*- coding:utf-8 -*-

import os, hashlib
import fileOper
import ctypes
from ctypes.wintypes import MAX_PATH

class EnvPrecheck(object):
    
    SERVER = ['//server-cgi/project'] 
    MAYA_ENV_FILE = ['//server-cgi/workflowtools_ep20/Install/Maya.env']
    SHAVENODE_FILE = ['C:/Program Files/JoeAlter/shaveHaircut/maya2012/plug-ins/shaveNode.mll']
    SOURCEIMAGE_FOLDER = ['//server-cgi/Project/E020DW/DWep20/sourceimages']
    PLUGIN_FOLDER = ['//server-cgi/workflowtools_ep20']
    
    MAYA_VERSION = '2012-x64'
    
    def __init__(self):
        pass
    
    
    def precheck(self):
        """
        Precheck the maya environment and maya file whether is right.
        There are six steps:
            1. check whether can connect the Server.
            2. check whether the maya env file is right.
            3. check whether the ShaveNode.mll file is right.
            4. check whether the texture files is readable.
            5. check whether the plugin folder is readable.
        And a single step:
         - check whether the maya file is readable.
            
        """
#        if not self._checkServer():
#            print 'SdiskConnectError'
##            return 'SdiskConnectError'
#            return False
        if not self._checkMayaEnvFile():
            print 'MayaEnvError'
#            return 'MayaEnvError'
            return False
        if not self._checkMayaShaveNodeFile():
            print 'ShaveNodeFileError'
#            return 'ShaveNodeFileError'
            return False
        if not self._checkSourceImagesOnServer():
            print 'SourceImagesOnServerError'
#            return 'SourceImagesOnServerError'
            return False
        if not self._checkPluginFolderOnServer():
            print 'PluginFolderError'
#            return 'PluginFolderError'
            return False
        return True
    
    
    
    def checkMayaFile(self, mayaFile):
        """
        check whether the maya file is readable. 
        """
        mayaFileName = os.path.basename(mayaFile)
        if not self._checkMayaFile(mayaFile):
            print '<%s>MayaFileError' % mayaFileName
#            return 'MayaFileError'
            return False
    
    
    
    def _checkServer(self):
        """
        check whether can connect the Server.
        """
        return self._isExistAndOpenInList(self.SERVER)
    
    
    def _isExistAndOpenInList(self, pathList):
        """
        Overwrite the isExistAndOpen function in fileOper.
        Now it is checking whether the path is readable.
        """
        for path in pathList:
            if fileOper.isExistAndOpen(path):
                return path
        return None
    
    
    def _checkMayaEnvFile(self):
        """
        check whether the maya env file is right.
        """
        userDocumentsPath = self._getUserDocuments()
        myMayaEnvFile = os.path.join(userDocumentsPath, 'maya', self.MAYA_VERSION, 'maya.env')
        if not fileOper.isExistAndOpen(myMayaEnvFile):
            return False
        mayaEnvFile = self._isExistAndOpenInList(self.MAYA_ENV_FILE)
        if not mayaEnvFile:
            return False
        
        serverMayaEnvStream = open(mayaEnvFile, 'r')
        myMayaEnvStream = open(myMayaEnvFile, 'r')
        try:
            for server, local in zip(serverMayaEnvStream, myMayaEnvStream):
                serverMD5 = hashlib.md5(server).digest()
                localMD5 = hashlib.md5(local).digest()
                if not (serverMD5 == localMD5):
                    return False
        except:
            print 'open maya env error'
        finally:
            serverMayaEnvStream.close()
            myMayaEnvStream.close()
        return True
    
    
    def _getUserDocuments(self):
        """
        get user's documents:
        Example: C:\Users\username\Documents
        """
        dll = ctypes.windll.shell32
        buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
        if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
            #print(buf.value)
            return buf.value
        else:
            print("get user documents Failure!")
            return None
    
    
    def _checkMayaShaveNodeFile(self):
        """
        check whether the ShaveNode.mll file is right.
        """
        return self._isExistAndOpenInList(self.SHAVENODE_FILE)
    
    
    def _checkSourceImagesOnServer(self):
        """
        check whether the texture files is readable.
        """
        sourceimagesFolder = self._isExistAndOpenInList(self.SOURCEIMAGE_FOLDER)
        if not sourceimagesFolder:
            return False
        for element in os.listdir(sourceimagesFolder):
            elementPath = os.path.join(sourceimagesFolder, element)
            if not fileOper.isExistAndOpen(elementPath):
                return False
        return True
    
    
    def _checkMayaFile(self, mayaFile):
        """
        check whether the maya file is readable.
        """
        return fileOper.isExistAndOpen(mayaFile) 
    
    
    def _checkPluginFolderOnServer(self):
        """
        check whether the plugin folder is readable.
        """
        return self._isExistAndOpenInList(self.PLUGIN_FOLDER)


if __name__ == '__main__':
    cls = EnvPrecheck()
    print cls.precheck() 
