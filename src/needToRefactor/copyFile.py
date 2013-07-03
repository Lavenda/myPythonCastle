'''
Created on 2013-7-1

@author: lavenda
'''
import shutil
import os

class CopyFiles(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def copys(self, filePathList):
        for filePath in filePathList:
            fileName = os.path.basename(filePath)
            tagPath = filePath.replace()
            shutil.copy(filePath)