#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-7-15

@author: lavenda
"""
import yaml
#from myTest.yamlTest import author
    
class ReferenceFileData(object):
    def __init__(self):
        self.filename = ''        # save the file name
        self.filePath = ''        # save the relatived path of file
        self.topMayaFile = []     # the list of the file in the source folder which reference it
        self.toReferenceFileDatas = []    # the list which this file reference
        self.beReferencedFileDatas = []   # the list which reference this file
        self.isExist = True       # whether exists in server folder



class YamlTest(object):
    
    def __init__(self):
        self.document = """
name: Vorlin Laruknuzum
sex: Male
class: Priest
title: Acolyte
hp: [32, 71]
sp: [1, 13]
gold: 423
inventory:
- a Holy Book of Prayers (Words of Wisdom)
- an Azure Potion of Cure Light Wounds
- a Silver Wand of Wonder
"""
    def getAuthor(self):
#        self.author = author.Author()
#        self.author.setAuthor('man1', 10, 'address1')
        pass
        
    
    def dump(self, author):
        self.getAuthor()
        print yaml.dump(author)
        
    def load(self):
        fileStream = open(r'D:\yamlTest3.yaml', 'r')
        for item in yaml.load_all(fileStream):
            if item:
                print '----'
                print item.filename
                print item.filePath
                print item.topMayaFile
            break
        fileStream.close()
        
        
def main():
    yamlTest = YamlTest()
    yamlTest.load()


if __name__ == '__main__':
    main()