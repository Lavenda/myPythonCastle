#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2012-10-24

@author: lavenda
"""



from odwlib.tactic.server.base import dbHelper

class BaseDAO(object):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        pass
    
    
    def queryItemsByXml(self, database, sql):
        """
        connect to database with xml configuration and query datas from it
        @param database: the name of the database you want to connect
        @type database: string type
        @param sql: the sql you need query
        @type sql: string type
        
        @return the query set
        """
        conn = dbHelper.DBHelper.getConnectionByXml(database=database)
        return self.__queryItemsProcess(conn, sql)
    
    
    def qureyItems(self, database, host, user, password, port, sql):
        """
        connect to database with your configuration and query datas from it
        
        @param database: the name of the database you want to connect
        @type database: string type
        @param host: the Ip of the database
        @type host: string type
        @param user: the username of the database
        @type user: string type
        @param password: the password of the database
        @type password: string type
        @param port: the public port of the computer the database in
        @type port: int type
        @param sql: the sql you need query
        @type sql: string type
        
        @return: the query set
        """
        conn = dbHelper.DBHelper.getConnection(host, database, user, 
                                                 password, port)
        return self.__queryItemsProcess(conn, sql)
    
    
    def __queryItemsProcess(self, conn, sql):
        """
        connect to the sql with 
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    
def main():
    a = BaseDAO()
    database = 'e020dw'
    sql = 'select * from shot'
    print a.queryItemsByXml(database, sql)


if __name__ == '__main__':
    main*()