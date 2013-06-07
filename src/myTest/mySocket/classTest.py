#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-23

@author: lavenda
"""

import os

def handleCommand(command):
    back = os.system(command)
    return back