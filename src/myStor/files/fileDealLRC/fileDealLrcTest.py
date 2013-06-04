"""
Created on 2013-6-4

@author: lavenda
"""

#!/usr/bin/env python2.6
#-*- coding:utf-8 -*-

import unittest
import lrcQcOper
import fileOper

class LrcQcOperationTest(unittest.TestCase):


    def setUp(self):
        self.lqo = lrcQcOper.LrcQcOperation()
    
    def tearDown(self):
        pass

    def testRun(self):
        self.lqo.run()
    
    def testFileOper(self):
        print fileOper.ShotFileOperation.getShotName(r'C:\Users\huangchengqi\Desktop\a\DRGN_2007_s05_A058_CMP_V01.mov')

if __name__ == '__main__':
    unittest.main()