

#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-6-5

@author: lavenda
"""

from odwlib.tactic.server.dao import shotDAO

class ShotBiz(object):
    
    def __init__(self):
        self.shotDAO = shotDAO.ShotDAO()
        
    
    def getShotCodeList(self, columns='code'):
        """
        get all the shots' code in the tactic database
        
        @param columns: the columns you want to query
        @type columns: string type(default:'code')
        
        @return: list type or None, the code list in db
        """
        queryList = self.shotDAO.queryAll(columns=columns)
        if queryList:
            codeList = [item[0] for item in queryList]
        else:
            return None
        return codeList


if __name__ == '__main__':
    sb = ShotBiz()
    print sb.getShotCodeList()