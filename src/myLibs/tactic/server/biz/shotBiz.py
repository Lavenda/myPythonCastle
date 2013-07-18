#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""

from odwlib.tactic.server.dao import projectDAO
from odwlib.tactic.server.dao import projectConfig

class ShotBiz(object):
    
    def __init__(self):
        self.__projectDAO = projectDAO.ProjectDAO()
        
    
    def getShotCodeList(self, columns='code'):
        """
        get all the shots' code in the tactic database
        
        @param columns: the columns you want to query
        @type columns: string type(default:'code')
        
        @return: list type or None, the code list in db
        """
        table = projectConfig.ProjectConfig.SHOT
        extra = 'order by code'
        queryList = self.__projectDAO.queryAll(table, columns,
                                               extra=extra)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList
    
    
    def getIdBySequence(self, episode, sequence):
        """
        get shot by sequence info
        @param episode: the episode info
        @type episode: string
        @param sequence: the sequence info
        @type sequence: string
        @retrun: list type or None, the code list in db
        """
        table = projectConfig.ProjectConfig.SHOT
        columns = 'id'
        filters = "episode='%s' and sequence='%s'" % (episode, sequence)
        queryList = self.__projectDAO.queryAll(table, columns, filters)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList
    
    
    def getIdsBySequences(self, episode, sequenceList):
        """
        get shot by sequence info
        @param episode: the episode info
        @type episode: string
        @param sequence: the sequence info
        @type sequence: string
        @retrun: list type or None, the code list in db
        """
        table = projectConfig.ProjectConfig.SHOT
        columns = 'id'
        sequenceListStr = "','".join(sequenceList)
        filters = "episode='%s' and sequence in ('%s')" % (episode, 
                                                           sequenceListStr)
        queryList = self.__projectDAO.queryAll(table, columns, filters)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList
    
    
    def getAllSequenceByEpi(self, episode):
        """
        get all the sequence in db with episode
        @param episode: the episode info
        @type episode: string
        @return: list type or None, the code list in db
        """
        table = projectConfig.ProjectConfig.SHOT
        columns = 'sequence'
        filters = "episode='%s'" % episode
        extra = 'order by sequence'
        noRepeatSequenceList = []
        
        queryList = self.__projectDAO.queryAll(table, columns, 
                                               filters, extra)
        if queryList:
            sequenceList = [item[0] for item in queryList]
        else:
            return None
        
        for sequence in sequenceList:
            if sequence not in noRepeatSequenceList:
                noRepeatSequenceList.append(sequence)
                
        return noRepeatSequenceList


    def getEpisodeCodeList(self, columns='code'):
        """
        get all the shots' code in the tactic database
        
        @param columns: the columns you want to query
        @type columns: string type(default:'code')
        
        @return: list type or None, the code list in db
        """
        table = projectConfig.ProjectConfig.EPISODE
        extra = 'order by code'
        queryList = self.__projectDAO.queryAll(table, columns,
                                               extra=extra)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList
    
    
    def getLocationNameByShotName(self, shotName, columns='shot_to_location'):
        table = projectConfig.ProjectConfig.SHOT
        extra = 'order by code'
        filter = "code='%s'" % shotName
        queryList = self.__projectDAO.queryAll(table, columns,
                                               filter, extra)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList
    
    
    def getFrameInfoByShotName(self, shotName):
        table = projectConfig.ProjectConfig.SHOT
        extra = 'order by code'
        filter = "code='%s'" % shotName
        columns = 'tc_frame_start, tc_frame_end'
        queryList = self.__projectDAO.queryAll(table, columns,
                                               filter, extra)
        if queryList:
            codeList = [(item[0],item[1]) for item in queryList]
        else:
            return None
        return codeList


def main():
    sb = ShotBiz()
    print sb.getFrameInfoByShotName('DRGN_2015_s10_A102')


if __name__ == '__main__':
    main()