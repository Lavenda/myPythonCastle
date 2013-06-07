#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-5-23

@author: lavenda
"""


def _main(*args, **kwargs):
    _sub(*args, **kwargs)

def _sub(*args, **kwargs):
    print args, kwargs

def newMethodTest():
    _main(3,2,4)

def zipTest():
    a = [1,2,3,4]
    b = [1,2,3]
    for a1, b1 in zip(a, b):
        print a1, b1
        
def maxTest():
    a = [1,2,3,4]
    b = [1,2,3]
    c = max(len(a),len(b))
    print c

def openTest():
    a = open(r'C:\Users\lavenda\Documents\maya\2012-x64\maya.env', 'r')
    print a.next()
    print a.next()
    a.close()

def linefeedTest():
    print ('this is a test, test the line that more than 80 chars will '
     'not pass the pylint check how to pass the pylint with linefeed.')
    a = ('a'
        'b')
    print a

def timeTest():
    import time
    print type(time.strftime('%Y%m%d',time.localtime(time.time())))
    
def fileSuffixTest():
    import os
    path = r's05_A058_CMP_V01.mov.txt'
    print os.path.splitext(path)
    
def osStatTest():
    import os
    path = r'C:\Users\lavenda\Desktop\a\DRGN_2007_s05_A058_CMP_V01.mov'
    print os.stat(path)
    path = r'C:\Users\lavenda\Desktop\a\DRGN_2007_s05_A058_CMP_V02.mov'
    print os.stat(path)
    
    
def osGetmtimeTest():
    import os 
    path = r'C:\Users\lavenda\Desktop\a\DRGN_2007_s05_A058_CMP_V01.mov'
    print os.path.getmtime(path)
    path = r'C:\Users\lavenda\Desktop\a\DRGN_2007_s05_A058_CMP_V02.mov'
    print type(os.path.getmtime(path))
    print type(0.0)
    
def sequenceTest():
    import os
    path = r'C:\Users\lavenda\Desktop\a\DRGN_2007_s05_A058_CMP_V01.mov'
    fileName = os.path.basename(path)
    shotName = fileName[0:17]
    sequence = shotName.split('_')[2]
    print sequence
    
def tupleTest():
    tupleSet = ()
    tupleSet.extend('a')
    print tupleSet
    
def addIntoListWithItsLoop():
    numList = [1,3,4]
    count = 0
    for num in numList:
        if count < 9 :
            numList.append(count)
        count += 1
        print numList
        
def listMergeTest():
    list1 = [1,2,3]
    list2 = [1,2,3]
    list3 = list1+list2
    print list3

def stringListTest():
    a = 'DRGN_2007_S09_A142_CMP_v01.0100.tif'
    print a[0:18]

def reTest():
    import re
    shotName = 'DRG09A142LMP01.0100.tif'
    SHOT_RE = '^.*([0-9]{2}).*([A-Z][0-9]{3}[a-z]?).*$'
    result = re.findall(SHOT_RE, shotName)
    print result
    
if __name__ == '__main__':
    reTest()