#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
"""
Created on 2013-5-13

@author: lavenda
"""


import os
import ctypes
import shutil
import filecmp
import getpass
import re
from ctypes.wintypes import MAX_PATH
from odwlib.deadline.envPreCheck import fileOper


class EnvPrecheck(object):
    """the deadline env precheck"""
    
    SERVER = ['//server-cgi/project']
    MAYA_ENV_FILE = ['//server-cgi/workflowtools_ep20/Install/Maya.env']
    SHAVENODE_FILE = [('C:/Program Files/JoeAlter/shaveHaircut/'
                       'maya2012/plug-ins/shaveNode.mll')]
    SOURCEIMAGE_FOLDER = ['//server-cgi/Project/E020DW/DWep20/sourceimages']
    CACHE_FOLDER = ['//server-cgi/Project/E020DW/DWep20/cache/alembic']
    PLUGIN_FOLDER = ['//server-cgi/workflowtools_ep20']
    
    MAYA_VERSION = '2012-x64'
    STANDARD_ACCOUNTS = ['renderfarm', 'huangchengqi']
    HOSTNAME_RE = '^render-[0-9]{2,3}$'
    MAYABATCH_PATH = '"C:/Program Files/Autodesk/Maya2012/bin/mayabatch.exe"'
    
    
    def __init__(self):
        self.resultStrList = []


    def precheck(self):
        """
        Precheck the maya environment and maya file whether is right.
        There are five steps:
            1. check whether can connect the Server.
            2. check whether the maya env file is right.
            3. check whether the ShaveNode.mll file is right.
            4. check whether the texture files is readable.
            5. check whether the plugin folder is readable.
            6. remove the 'prefs' directory, when the hostname is render-XXX
        And a single step:
         - check whether the maya file is readable.
        
        @return: a string type, contains all the results from every check.
        """
        isAllRight = True
#        if not self._checkServer():
#            self._writeIntoResultStringByType('SdiskConnectError')
#            return 'SdiskConnectError'
#            return False
        self._writeIntoResultStringByType('*********************'
                                          '*********************')
        self._showMayaVersion()
        userName, hostname = self._getAndShowUserAndHostname()
        mayaDocumentsPath = self._getMayaDocumentsPath()
        if not self._checkRenderMayaEnvFile(userName, mayaDocumentsPath):
            self._writeIntoResultStringByType('MayaEnvError', 
                                              'error')
            isAllRight = False
        if not self._checkMayaShaveNodeFile():
            self._writeIntoResultStringByType('ShaveNodeFileError', 
                                              'error')
            isAllRight = False
        if not self._checkCacheFolderOnServer():
            self._writeIntoResultStringByType('CacheFolderOnServerError', 
                                              'error')
            isAllRight = False
        if not self._checkSourceImagesOnServer():
            self._writeIntoResultStringByType('SourceImagesOnServerError', 
                                              'error')
            isAllRight = False
        if not self._checkPluginFolderOnServer():
            self._writeIntoResultStringByType('PluginFolderError', 
                                              'error')
            isAllRight = False
        if self._isRenderHost(hostname):
            isAllRight = self._removePrefs(mayaDocumentsPath)
        self._writeIntoResultStringByType('*********************'
                                          '*********************')
        
        return isAllRight
    
    
    def _showMayaVersion(self):
        command = self.MAYABATCH_PATH + ' -v'
        result = os.popen(command).read().strip()
        self._writeIntoResultStringByType('*** <%s> ***'
                                          % result)
    
    
    def _getAndShowUserAndHostname(self):
        """
        get and print current account and hostname in command line
        """
        currentAccount = self._getUserName()
        hostName = self._getHostname()
        
        self._writeIntoResultStringByType('*** <%s> is current account. ***' 
                                    % currentAccount)
        self._writeIntoResultStringByType('*** <%s> is the hostname. ***' 
                                    % hostName)
        return currentAccount, hostName
    
    
    def _getUserName(self):
        """
        get the user name
        
        @return: string type
        """
        return getpass.getuser()
    
    
    def _getHostname(self):
        """
        get the hostname
        
        @return: string type
        """
        return os.getenv('computername')
    
    
    def _getMayaDocumentsPath(self):
        """
        get user's documents:
        Example: C:\Users\username\Documents
        """
        dll = ctypes.windll.shell32
        buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
        if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
            return os.path.join(buf.value, 'maya', self.MAYA_VERSION)
        else:
            self._writeIntoResultStringByType('get user documents Failure!',
                                              'error')
            return None
    
    
    def backResultStrList(self):
        """
        back a list of the every check result. 
        """
        return self.resultStrList
    
    
    def _writeIntoResultStringByType(self, resultStr, strType='root'):
        """
        take the result string into a result list by its type
        
        @param resultStr: a result string from a check
        @type resultStr: string type L{fileOper}
        @param strType:  a type string of messages to print style.
        @type strType: string type
        
        """
        if strType == 'l1':
            self.resultStrList.append('    ' + resultStr)
        elif strType == 'l2':
            self.resultStrList.append('        ' + resultStr)
        elif strType == 'error':
            self.resultStrList.append('Error: ' + resultStr)
        elif strType == 'warning':
            self.resultStrList.append('Warning: ' + resultStr) 
        else:
            self.resultStrList.append(resultStr)


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
                self._writeIntoResultStringByType('<%s> ......READ OK' 
                                                  % path, 'l2')
                return path
            else:
                self._writeIntoResultStringByType('<%s> ......READ Failure' 
                                                  % path, 'error')
        return None 
    
    
    def _checkRenderMayaEnvFile(self, currentAccount, mayaDocumentsPath):
        """
        only check the maya env file in render farm account.
        """
        
        myMayaEnvFile = os.path.join(mayaDocumentsPath, 'maya.env')
        
        self._writeIntoResultStringByType('-> check the Maya Env File', 'l1')
        self._checkAndCopyMayaEnvFile(myMayaEnvFile)
        
        isRight = self._checkMayaEnvFile(myMayaEnvFile)
        if isRight:
            return isRight
        else:
            if self._isStandardAccount(currentAccount):
                if self._copyAndBackupMayaEnvFile(myMayaEnvFile):
                    isRight = self._checkMayaEnvFile(myMayaEnvFile)
            else:
                self._writeIntoResultStringByType(('the current account is '
                                                  'not <STANDARD_ACCOUNT>'),
                                                  'warning')
        
        return isRight
    
    
    def _checkAndCopyMayaEnvFile(self, myMayaEnvFile):
        """
        check the maya env file is exist or not.
        if not exist, will copy it from server.
        """
        if not os.path.isfile(myMayaEnvFile):
            self._writeIntoResultStringByType('<%s> is not exist'
                                        % myMayaEnvFile, 'error')
            self._copyMayaEnvFile(myMayaEnvFile)
    
    
    def _checkMayaEnvFile(self, myMayaEnvFile):
        """
        check whether the maya env file is right.
        """
        if not fileOper.isExistAndOpen(myMayaEnvFile):
            return False
        mayaEnvFile = self._isExistAndOpenInList(self.MAYA_ENV_FILE)
        if not mayaEnvFile:
            return False
        
        try:
            isSame = filecmp.cmp(mayaEnvFile, myMayaEnvFile)
            if not isSame:
                self._writeIntoResultStringByType('<%s> is not right' 
                                                  % myMayaEnvFile, 'error')
                return False
        except Exception:
            self._writeIntoResultStringByType('open maya env error', 'error')
        self._writeIntoResultStringByType('<%s> ...... CHECK OK' 
                                                % myMayaEnvFile, 'l2')
        return True
    
    
    def _isStandardAccount(self, currentAccount):
        """
        check the current account is a standrad account or not.
        
        @param userDocumentsPath: user document path
        @type userDocumentsPath: string type
        
        @return: boolean type
        """
        if currentAccount in self.STANDARD_ACCOUNTS:
            return True
        else:
            return False
    
    
    def _copyAndBackupMayaEnvFile(self, myMayaEnvFile):
        """
        backup the local maya env file,
        and copy the maya env file from server to local
        """
        try:
            reName = myMayaEnvFile + '.bak'
            shutil.move(myMayaEnvFile, reName) 
        except Exception:
            self._writeIntoResultStringByType('backup maya env file error',
                                              'error')
            return False
        
        return self._copyMayaEnvFile(myMayaEnvFile)

    
    def _copyMayaEnvFile(self, myMayaEnvFile):
        """
        copy the maya env file from server to local
        """
        try:
            shutil.copy(self.MAYA_ENV_FILE[0], myMayaEnvFile)
        except Exception:
            self._writeIntoResultStringByType('copy maya env file error',
                                              'error')
            return False
        self._writeIntoResultStringByType('<%s> copy completed' % myMayaEnvFile,
                                          'warning')
        return True
    
    
    def _checkMayaShaveNodeFile(self):
        """
        check whether the ShaveNode.mll file is right.
        """
        self._writeIntoResultStringByType('-> check Maya ShaveNode File', 'l1')
        return self._isExistAndOpenInList(self.SHAVENODE_FILE)
    
    
    def _checkCacheFolderOnServer(self):
        """
        check whether the cache files is readable.
        """
        self._writeIntoResultStringByType('-> check Cache Folder On Server',
                                          'l1')
        return self.__checkFolderOnServer(self.CACHE_FOLDER)
    
    
    def _checkSourceImagesOnServer(self):
        """
        check whether the texture files is readable.
        """
        self._writeIntoResultStringByType('-> check Source Images On Server',
                                          'l1')
        return self.__checkFolderOnServer(self.SOURCEIMAGE_FOLDER)
    
    
    def __checkFolderOnServer(self, folderList):
        """
        check whether the folder list is readable. 
        """
        folderOnServer = self._isExistAndOpenInList(folderList)
        if not folderOnServer:
            return False
        for element in os.listdir(folderOnServer):
            elementPath = os.path.join(folderOnServer, element)
            if not fileOper.isExistAndOpen(elementPath): 
                return False
            
        return True
    

    def _checkPluginFolderOnServer(self):
        """
        check whether the plugin folder is readable.
        """
        self._writeIntoResultStringByType('-> check Plugin Folder On Server',
                                          'l1')
        return self._isExistAndOpenInList(self.PLUGIN_FOLDER)
    
    
    def _isRenderHost(self, hostname):
        """
        judge this is render host or not
        """
        self._writeIntoResultStringByType('-> check the prefs dir',
                                          'l1')
        if re.match(self.HOSTNAME_RE, hostname.lower()):
            return True
        else:
            self._writeIntoResultStringByType('<%s> is not Render computer'
                                              % hostname, 'warning')
            return False
        
    
    def _removePrefs(self, mayaDocumentsPath):
        """
        remove the prefs directory in user documents.
        """
        prefsDir = os.path.join(mayaDocumentsPath, 'prefs')
        if os.path.isdir(prefsDir):
            backupPrefsDir = os.path.join(mayaDocumentsPath,
                                          'prefs_backUp')
            if os.path.isdir(backupPrefsDir):
                try:
                    shutil.rmtree(backupPrefsDir)
                except Exception, e:
                    print e
                    return False
            try:
                os.rename(prefsDir, backupPrefsDir)
            except Exception, e:
                print e
                return False
            try:
                os.makedirs(prefsDir)
            except Exception, e:
                print e
                return False
        
        self._writeIntoResultStringByType('<%s> ...... REMOVE OK' % prefsDir,
                                          'l2')
        return True
    
    
    def checkMayaFile(self, mayaFile):
        """ 
        check whether the maya file is readable.
        """
        if not self._checkMayaFile(mayaFile):
            self._writeIntoResultStringByType('<%s>MayaFileError' 
                                              % mayaFile, 'error')
            return False
        
        return True

    
    def _checkMayaFile(self, mayaFile):
        """
        check whether the maya file is readable.
        """
        return fileOper.isExistAndOpen(mayaFile)
    


def main():
    epCls = EnvPrecheck()
    print epCls.precheck() 
    print '\n'.join(epCls.backResultStrList())

if __name__ == '__main__':
    main()