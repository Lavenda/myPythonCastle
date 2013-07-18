# -*- Coding: Utf-8 -*- 
'''
Created on 2013-1-5

@author: huangchenqi
'''

import time, os, re
import yaml


class ReferenceFileData(object):
    def __init__(self):
        self.filename = ''        # save the file name
        self.filePath = ''        # save the relatived path of file
        self.topMayaFile = []     # the list of the file in the source folder which reference it
        self.toReferenceFileDatas = []    # the list which this file reference
        self.beReferencedFileDatas = []   # the list which reference this file
        self.isExist = True       # whether exists in server folder



class FindContainReference(object):
    '''
    the core is that find the reference in the server folder with the recursion method.
    the thinking is :
    1. get all maya files in source folder.
    2. get all the reference file from each in these maya files.
    3. create ReferenceFileData Ojbect for each reference file.
    4. get all the reference file from each reference file, and create ojbect too.
    5. each object has toReferenceFileDatas and beReferencedFileDatas to save reference data.
    6. add all ReferenceFileData objects to one addressDictionary for management.
    '''
    def __init__(self):
        self.allFilenameToItsAddress = {}   #AddressDictionary
    
    
    def genAYamlFile(self, srcPath):
        self.addAllFilePathsToAddressDictionary(srcPath)
        self._genAYamlFile()
    
    def _genAYamlFile(self):
        fileStream = open('D:/yamlTest.yaml', 'w')
        for fileName, referenceFileData in self.allFilenameToItsAddress.items():
#            print fileName
            fileStream.write(yaml.dump(referenceFileData))
            fileStream.write('---\n')
#            fileStream.write(yaml.dump(str(referenceFileData)))
#            fileStream.write(yaml.dump(str(referenceFileData.filename)))
#            fileStream.write(yaml.dump(str(referenceFileData.filePath)))
#            fileStream.write(yaml.dump(str(referenceFileData.topMayaFile)))
#            fileStream.write(yaml.dump(str(referenceFileData.toReferenceFileDatas)))
#            fileStream.write(yaml.dump(str(referenceFileData.beReferencedFileDatas)))
#            fileStream.write(yaml.dump(str(referenceFileData.isExist)))
        fileStream.close()
    
    
    def getGeneralTable(self, srcPath):
        '''
        This method will write an excel file that includes all reference files in this directory
        '''
        allTopMayaFilePaths = self.addAllFilePathsToAddressDictionary(srcPath)
        self.writeReferenceFileAndSrcFile(allTopMayaFilePaths)
    
    
    
    def addAllFilePathsToAddressDictionary(self, srcPath):
        '''
        Here, return allTopMayaFilePaths only for the method of 'writeReferenceFileAndSrcFile' use.
        '''
        allTopMayaFilePaths = []
        allReferenceData = {}
        
        allTopMayaFilePaths = self._findAllTopMayaFiles(srcPath)
        print len(allTopMayaFilePaths)
        self._addAllReferenceDataToAddressDictionary(allTopMayaFilePaths)
        print len(self.allFilenameToItsAddress) - len(allTopMayaFilePaths)
        return allTopMayaFilePaths
    
    
    def findAllFileReferenceThisFile(self, fileName, srcPath):
        ''' 
        temp use
        '''
        allTopMayaFilePaths = []
        allReferenceData = {}
        
        allTopMayaFilePaths = self._findAllTopMayaFiles(srcPath)
        print len(allTopMayaFilePaths)
        self._addAllReferenceDataToAddressDictionary(allTopMayaFilePaths)
        ReferenceFileDataGroup = self.allFilenameToItsAddress[fileName].beReferencedFileDatas
#        print [object.filePath for object in ReferenceFileDataGroup]


    def _findAllTopMayaFiles(self, srcPath):
        '''
        find all top mayaFiles in the folder
        '''
        allTopMayaFilePaths = []
        
        if os.path.isdir(srcPath):
            for dirPath, dirnames, filenames in os.walk(srcPath):
                allTopMayaFilePaths = self._findSuitableFiles(filenames, dirPath, allTopMayaFilePaths)
        elif os.path.isfile(srcPath):
            allTopMayaFilePaths.append(srcPath)
        else:
            print srcPath + ' is error!'
        return allTopMayaFilePaths
    
    
    def _findSuitableFiles(self, filenames, dirPath, suitableFilePaths):
        for filename in filenames:
            if self._isSuitable(filename):
                absolutePath = os.path.join(dirPath, filename)
                if absolutePath not in suitableFilePaths:
                    suitableFilePaths.append(absolutePath)
        return suitableFilePaths
    
    
    def _isSuitable(self, filename):
        SUITABLE_FILE_EXTENSION = '.ma'
        if filename.endswith(SUITABLE_FILE_EXTENSION):
            return True
        else:
            return False
    
    
    def _addAllReferenceDataToAddressDictionary(self, topMayaFilePaths):
        for topMayaFilePath in topMayaFilePaths:
#            print topMayaFilePath
            self._getReferenceDataAndAddReferenceDataToAddressDictionary(topMayaFilePath, topMayaFilePath)
    
    
    def _getReferenceDataAndAddReferenceDataToAddressDictionary(self, topMayaFilePath, referenceFilePath, upperReferenceFileData=None):
        '''
        get reference file object(ReferenceData) , and add it to addressDictionary(allFilenameToItsAddress)
        get whether reference file has been exist in address Dirctionary.If it exists, take it out. If not, create it
        '''
        if self._isExistInAddressDictionary(referenceFilePath):
            referenceFilename = os.path.basename(referenceFilePath)
            referenceFileData = self.allFilenameToItsAddress[referenceFilename]
            self._addToTopMayaFilenameAndUpperReferenceFileData(referenceFileData, topMayaFilePath, upperReferenceFileData)
        else:
            referenceFileData = self._createReferenceFileDataObject(topMayaFilePath, referenceFilePath, upperReferenceFileData)
            self._addReferenceFileDataToAddressDictionary(referenceFileData)
        return referenceFileData
    
    
    def _isExistInAddressDictionary(self, referenceFilePath):
        ReferenceFilename = os.path.basename(referenceFilePath)
        if ReferenceFilename in self.allFilenameToItsAddress.keys():
            return True
        else:
            return False
    
    
    def _addToTopMayaFilenameAndUpperReferenceFileData(self, referenceFileData, topMayaFilePath, upperReferenceFileData):
        '''
        assign data to topMayaFilename and UpperReferenceFile in object(referenceFileData)
        '''
        topMayaFilename = os.path.basename(topMayaFilePath)
        if topMayaFilename not in referenceFileData.topMayaFile:
            referenceFileData.topMayaFile.append(topMayaFilename)
        if upperReferenceFileData != None and upperReferenceFileData not in referenceFileData.beReferencedFileDatas:
            referenceFileData.beReferencedFileDatas.append(upperReferenceFileData)
        return referenceFileData
    
    
    def _createReferenceFileDataObject(self, topMayaFilePath, filePath, upperReferenceFileData=None):
        '''
        if the referenceFileData Object is not exist, will jump into this method
        '''
        referenceFileData = ReferenceFileData()
        referenceFileData.filename = os.path.basename(filePath)
        referenceFileData.filePath = filePath
        
        referenceFileData = self._addToTopMayaFilenameAndUpperReferenceFileData(
                                                            referenceFileData,
                                                            topMayaFilePath,
                                                            upperReferenceFileData)
        toReferenceFileDatas = self._getToReferenceFileDatas(topMayaFilePath, referenceFileData,
                                                             upperReferenceFileData)
        if toReferenceFileDatas and toReferenceFileDatas[0] == False:
            ' this context is using the unique method to get whether the file exist in server folder'
            referenceFileData.isExist = False
            toReferenceFileDatas.pop()
        referenceFileData.toReferenceFileDatas = toReferenceFileDatas
#        if referenceFileData.filename =='boat_berkdinghy_SET.ma':
#            print referenceFileData.isExist
#            assert 1==2
        return referenceFileData
    
    
    def _getToReferenceFileDatas(self, topMayaFilePath, referenceFileData, upperReferenceFileData):
        standardFilePath = ''
        containReferenceFileDatas = []
        filePath = referenceFileData.filePath
        
        if self._isTopMayaFilePath(topMayaFilePath, filePath):
            standardFilePath = filePath
        else:
            standardFilePath = self._replaceNonStandardFilePath(filePath)
        containReferenceFilePaths = self._getContainReferenceFilePaths(standardFilePath)
        if containReferenceFilePaths:
            if containReferenceFilePaths[0] != False:
                for containReferenceFilePath in containReferenceFilePaths:
                    containReferenceFileData = self._getReferenceDataAndAddReferenceDataToAddressDictionary(
                                                                                                topMayaFilePath,
                                                                                                containReferenceFilePath,
                                                                                                referenceFileData)
                    containReferenceFileDatas.append(containReferenceFileData)
            else:
                containReferenceFileDatas.append(False)
#                print '<- %s' % upperReferenceFileData.filePath
           
        return containReferenceFileDatas
    
    
    def _isTopMayaFilePath(self, topMayaFilePath, filePath):
        if topMayaFilePath == filePath:
            return True
        else:
            return False
    
    
    def _replaceNonStandardFilePath(self, nonStandardFilePath):
#        NONSTANDARD_PATH_PREFIXS = []
#        NONSTANDARD_PATH_PREFIXS = ['$JOB_ASSETS']
        NONSTANDARD_PATH_PREFIXS = ['S:/Dragon/_assets','$JOB_ASSETS','s:/Dragon/_assets','S:/dragon/_assets']
        STANDARD_RELATIVE_PATH_PREFIX = '_assets'
#        STANDARD_ABSOLUTE_PATH_PREFIX = r'S:\E020DW\Data_ from_DW\preAsset\20130701a\_assets'
#        STANDARD_ABSOLUTE_PATH_PREFIX = 'S:/E020DW/DWep20/_assets'
        STANDARD_ABSOLUTE_PATH_PREFIX = 'W:/dragon_mstr/_assets'
#        standardFilePath = nonStandardFilePath
        for NONSTANDARD_PATH_PREFIX in NONSTANDARD_PATH_PREFIXS:
            if NONSTANDARD_PATH_PREFIX in nonStandardFilePath:
                nonStandardFilePath = nonStandardFilePath.replace(NONSTANDARD_PATH_PREFIX, STANDARD_RELATIVE_PATH_PREFIX)
        standardFilePath = nonStandardFilePath.replace(STANDARD_RELATIVE_PATH_PREFIX, STANDARD_ABSOLUTE_PATH_PREFIX)
        return standardFilePath
    
    
    def _getContainReferenceFilePaths(self, standardFilePath):
        containReferenceFiles = []
#        if standardFilePath == r'S:/E020DW/DWep20/_assets/env/set_ext/beachgeneric/beachgeneric_ext/models/beachgeneric_ext_SET.ma':
#            return containReferenceFiles
#        fileStreamTmp = open(r'D:\findContainRefTest.txt','a')
#        fileStreamTmp.write(standardFilePath +'\n')
#        fileStreamTmp.close()
        
        REFERENCE_REGULAR_EXPRESSION = '^\t{0,2}.*"([a-zA-Z_/$0-9:]*\.ma)";'
        REFERENCE_END_REGULAR_EXPRESSION = '^requires.*'
        if not os.path.isfile(standardFilePath):
            print '<%s> is not find' % standardFilePath
            containReferenceFiles.append(False)
            return  containReferenceFiles
        fileStream = open(standardFilePath, 'r')
        try:
            for line in fileStream:
                suitableReferenceFilePath = re.findall(REFERENCE_REGULAR_EXPRESSION, line)
                if suitableReferenceFilePath:
                    containReferenceFiles.append(suitableReferenceFilePath[0])
                endReferenceFileTag = re.findall(REFERENCE_END_REGULAR_EXPRESSION, line)
                if endReferenceFileTag:
                    break
        finally:
            fileStream.close()
        return containReferenceFiles
    
    
    def _addReferenceFileDataToAddressDictionary(self, referenceFileData):
        referenceFliename = referenceFileData.filename
        if referenceFliename not in self.allFilenameToItsAddress.keys():
            self.allFilenameToItsAddress[referenceFliename] = referenceFileData
    
    
    def writeReferenceFileAndSrcFile(self, allTopMayaFilePaths):
        NOW = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        writtenFilePath = 'D:/ReferenceFileDetail/referenced_file_' + NOW + '.txt'
        fileStream = open(writtenFilePath, 'w')
        writtenTitleLine = self._compileWrittenTitleLine(allTopMayaFilePaths)
        try:
            fileStream.write(writtenTitleLine + '\n')
            for referenceFileData in self.allFilenameToItsAddress.values():
                writtenLine = self._compileWrittenLine(allTopMayaFilePaths, referenceFileData)
                fileStream.write(writtenLine)
        finally:
            fileStream.close()
    
    
    def _compileWrittenTitleLine(self, allTopMayaFilePaths):
        writtenTitleLine = 'CountOfContainReferenceFile\tbeReferencedFileDatas\tFileName\tIsExist\t'
        for allTopMayaFilePath in allTopMayaFilePaths:
            topMayaFilename = os.path.basename(allTopMayaFilePath)[10:18]
            writtenTitleLine = writtenTitleLine + '\t' + topMayaFilename
        writtenTitleLine = writtenTitleLine + '\t\tFilePath'
        return writtenTitleLine
    
    
    def _compileWrittenLine(self, allTopMayaFilePaths, referenceFileData):
        filename = referenceFileData.filename
        filePath = referenceFileData.filePath
        isExist = referenceFileData.isExist
        beReferencedFileDatas = self._delLayoutFile(referenceFileData.beReferencedFileDatas)
        countOfContainReferenceFile = self._getCountOfContainReferenceFile(filename)
        writtenLine = str(countOfContainReferenceFile) + '\t' + str(beReferencedFileDatas) + '\t' + filename + '\t' + str(isExist) + '\t'
        containTopMayaFiles = referenceFileData.topMayaFile
        for allTopMayaFilePath in allTopMayaFilePaths:
            topMayaFilename = os.path.basename(allTopMayaFilePath)
            if filename == topMayaFilename:
                return ''
            if  topMayaFilename in containTopMayaFiles:
                writtenLine = writtenLine + '\t1' 
            else:
                writtenLine = writtenLine + '\t'
        writtenLine = writtenLine + '\t\t' + filePath + '\n'
        return writtenLine
    
    
    def _delLayoutFile(self, beReferencedFileDatas):
        noLayoutFilenameList = []
        for beReferencedFileData in beReferencedFileDatas:
            filename = beReferencedFileData.filename
            if '_lay_' in filename.lower():
                continue
            noLayoutFilenameList.append(filename)
        return noLayoutFilenameList
    
    
    def _getCountOfContainReferenceFile(self, filename):
        referenceFileData = self.allFilenameToItsAddress[filename]
        countOfContainReferenceFile = len(referenceFileData.toReferenceFileDatas)
        return countOfContainReferenceFile


if __name__ == '__main__' :
    findContainReference = FindContainReference()
#    findContainReference.getGeneralTable(r'C:\Users\huangchengqi\Desktop\unStandardInS')
#    findContainReference.getGeneralTable(r'S:\E020DW\DWep20\_episodes\drgn_2015\s10\DRGN_2015_s10_A102\Scenes\LAY')
#    findContainReference.genAYamlFile(r'S:\E020DW\DWep20\_episodes\drgn_2015')
    findContainReference.getGeneralTable(r'C:\Users\huangchengqi\Desktop\b')
#    findContainReference.findAllFileReferenceThisFile('stalactite_double_MDL.ma',r'C:\Users\huangchengqi\Desktop\ma')
