#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

'''
Created on 2013-7-9

@author: lavenda
'''
import os
from odwlib.tactic.server.dao import sthpwDAO
from odwlib.tactic.server.dao import projectConfig


class SthpwBiz(object):

    def __init__(self):
        self.__sthpwDAO = sthpwDAO.SthpwDAO()


    def getFileInfoBySnapshotCode(self, snapshotCode):
        """
        get shot by sequence info
        """
        table = projectConfig.ProjectConfig.FILE
        columns = 'relative_dir, file_name'
        filters = "snapshot_code='%s'" % snapshotCode
        queryList = self.__sthpwDAO.queryAllNoProject(table, columns, filters)
        if queryList:
            codeList = [item for item in queryList]
        else:
            return None
        return codeList
    
    
    def getFilesInfoBySnapshotCode(self, snapshotCodeList):
        """
        get shot by sequence info
        """
        table = projectConfig.ProjectConfig.FILE
        columns = 'relative_dir, file_name'
        snapshotCodeListStr = "','".join(snapshotCodeList)
        filters = "snapshot_code in ('%s')" % snapshotCodeListStr
        queryList = self.__sthpwDAO.queryAllNoProject(table, columns, filters)
        if queryList:
            codeList = [item for item in queryList]
        else:
            return None
        return codeList
    
    
    def getProcessPathList(self, shotIdList, process, rootPath):
        """
        get processPath
        """
        snapshotCodeListSql = self.getCurrentCodeBySIdsAndProcess(shotIdList, 
                                                               process)
        layoutFilePathList = self.getFilesInfoBySnapshotCode(snapshotCodeList)
        return [os.path.normpath(os.path.join(rootPath, item[0], item[1])) \
                for item in layoutFilePathList]
        
    
    def getCurrentCodeBySIdAndProcess(self, searchId, process):
        """
        get shot by sequence info
        """
        table = projectConfig.ProjectConfig.SNAPSHOT
        columns = 'code'
        filters = "version=0 and search_id=%s and process='%s'" \
                  % (searchId, process)
        queryList = self.__sthpwDAO.queryAll(table, columns, filters)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList
    
    
    def getCurrentCodeBySIdsAndProcess(self, searchIdList, process):
        """
        get shots by sequence info
        """
        table = projectConfig.ProjectConfig.SNAPSHOT
        columns = 'code'
        searchIdStringList = [str(item) for item in searchIdList]
        searchIdListStr = ','.join(searchIdStringList)
        filters = "version=0 and search_id in (%s) and process='%s'" \
                  % (searchIdListStr, process)
        queryList = self.__sthpwDAO.queryAll(table, columns, filters)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList



def main():
    sb = SthpwBiz()
    print sb.getCurrentCodeBySIdsAndProcess((839,838),'LAY')
    print sb.getCurrentCodeBySIdAndProcess(839,'LAY')
    print sb.getFileInfoBySnapshotCode('SNAPSHOT00058436')
    print sb.getFilesInfoBySnapshotCode(('SNAPSHOT00058436', 'SNAPSHOT00058438'))


if __name__ == '__main__':
    main()