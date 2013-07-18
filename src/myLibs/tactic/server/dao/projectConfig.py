#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

'''
Created on 2013-7-9

@author: lavenda
'''

class ProjectConfig(object):

    SHOT = 'shot'
    SEQUENCE = 'sequence'
    EPISODE = 'episode'
    FILE = 'file'
    SNAPSHOT = 'snapshot'

    STHPW = 'sthpw'
    PROJECT = 'e020dw'


    def __init__(self):
        pass
    
    
    @staticmethod
    def setProjectCode(projectCode):
        ProjectConfig.PROJECT = projectCode
