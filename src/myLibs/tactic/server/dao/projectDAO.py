#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

'''
Created on 2013-7-9

@author: lavenda
'''


from odwlib.tactic.server.base import baseDAO
from odwlib.tactic.server.dao import projectConfig


class ProjectDAO(baseDAO.BaseDAO):
    
    def __init__(self):
        baseDAO.BaseDAO.__init__(self)
        self.__database = projectConfig.ProjectConfig.PROJECT
    
    
    def queryAll(self, table, columns='*', filters='1=1', extra=''):
        """
        use temporary
        """
        sql = 'select %s from %s where %s %s' % (columns, table, filters, 
                                                 extra)
        queryList = baseDAO.BaseDAO.queryItemsByXml(self, self.__database, sql)
        return queryList