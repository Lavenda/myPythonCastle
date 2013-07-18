#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-7-4

@author: lavenda
"""
import os
from odwlib.tactic.server.biz import sthpwBiz
from odwlib.tactic.server.biz import shotBiz
from odwlib.tactic.server.dao import projectConfig

class TacticDataInfo(object):
    
    def __init__(self):
        self.__sthpwBiz = sthpwBiz.SthpwBiz()
        self.__shotBiz = shotBiz.ShotBiz()
    
    
    def setProject(self, projectCode):
        """
        set the project
        
        @param projectCode: the project code in tactic
        @type projectCode: string
        """
        projectConfig.ProjectConfig.setProjectCode(projectCode)
    
    
    def getCameraPathList(self, episode, sequence, rootPath):
        """
        get the shot camera path in db with episode and sequence
        
        @param episode: the episode info
        @type episode: string
        @param sequence: the sequence info
        @type sequence: string
        @param rootPath: root dir path in server
        @type rootPath: string
        @retrun: the camera path list
        @rtype: list
        """
        shotIdList = self.__shotBiz.getIdBySequence(episode, sequence)
        process = 'CAM'
        return self.__sthpwBiz.getProcessPathList(shotIdList, process, 
                                                  rootPath)
        
        
    def getCameraPathListBySeqs(self, episode, sequenceList, rootPath):
        """
        get the shot camera path in db with episode and sequence
        
        @param episode: the episode info
        @type episode: string
        @param sequence: the sequence info
        @type sequence: string
        @param rootPath: root dir path in server
        @type rootPath: string
        @retrun: the camera path list
        @rtype: list
        """
        shotIdList = self.__shotBiz.getIdsBySequences(episode, sequenceList)
        process = 'CAM'
        return self.__sthpwBiz.getProcessPathList(shotIdList, process, 
                                                  rootPath)
    
    
    def getAllSequenceByEpi(self, episode):
        """
        get all the sequence in db with episode
        
        @param episode: the episode info
        @type episode: string
        @return: the sequence in this episode list
        @rtype: list  
        """
        return self.__shotBiz.getAllSequenceByEpi(episode)
    
    
    def getAllEpisode(self):
        """
        get all the episode in db in this project
        """
        return self.__shotBiz.getEpisodeCodeList()
    
    
    def getLocationPath(self, shotName, episode='drgn_2015', rootPath='S:/'):
        pass
    
    
    def getFrameInfoByShotName(self, shotName):
        return self.__shotBiz.getFrameInfoByShotName(shotName)[0]



def main():
    projectCode = 'E008DW'
    episode = 'drgn_2015'
    sequenceList = ['s08']
    rootPath = 'S:/'
    tacticInfo = TacticDataInfo()
#    print tacticInfo.getAllEpisode()
#    projectConfig.ProjectConfig.EPISODE = 'dw09_episode'
#    tacticInfo.setProject(projectCode)
#    print tacticInfo.getCameraPathList(episode, sequence, rootPath)
    print tacticInfo.getCameraPathListBySeqs(episode, sequenceList, rootPath)
    print tacticInfo.getAllSequenceByEpi(episode)
    print tacticInfo.getAllEpisode()
    print tacticInfo.getFrameInfoByShotName('DRGN_2015_s10_A102')
    

if __name__ == '__main__':
    main()