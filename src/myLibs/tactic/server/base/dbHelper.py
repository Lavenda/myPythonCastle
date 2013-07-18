#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
'''
Created on 2012-10-24

@author: lavenda
'''

from lib import psycopg2
from odwlib.tactic.server.base import xmlConfig


class DBHelper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    @staticmethod
    def getConnection(host, database, user, password, port='5432'):
        try:
            conn = psycopg2.connect(database=database, user=user, 
                                    password=password, host=host, port=port)
        except Exception, e:
            print e.pgerror
            print 'Connect to DB(%s) error!' % host
            return None
        if(conn==None):
            print 'Connect to DB(%s) None!' % host
            return None
        return conn
    
    
    @staticmethod
    def getConnectionByXml(database):
        project_name = xmlConfig.XmlConfig().getMainProjectName()
        dbData = xmlConfig.XmlConfig(project_name=project_name).getDBData()
        host = dbData['host']
        user = dbData['user']
        password = dbData['password']
        port = dbData['port']
        conn = DBHelper.getConnection(host=host, database=database,
                                       user=user, password=password, port=port)
        return conn
    
    
    @staticmethod
    def closeAll(cursor=None, conn=None):
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.close()
            
            
