#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-24

@author: lavenda
"""


class RequestHandler(object):
    """
    the base request handler class
    """
    
    def __init__(self, hint):
        self.hint = hint
    
    
    def handle(self):
        pass