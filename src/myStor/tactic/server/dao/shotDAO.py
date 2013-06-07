#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""


from odwlib.tactic.server.base import baseDAO

class ShotDAO(baseDAO.BaseDAO):
    
    def __init__(self):
        baseDAO.BaseDAO.__init__(self)
    
    
    def queryAll(self, database='e020dw', columns='*', filters='1=1'):
        """
        use temporary
        """
        sql = 'select %s from shot where %s' % (columns, filters)
        queryList = baseDAO.BaseDAO.queryItemsByXml(self, database, sql)
        return queryList
        
