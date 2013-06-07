
#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2013-6-4

@author: lavenda
"""

import unittest
from odwlib.lrc.lrcQcFileOper import lrcFileOper

class LrcQcOperationTest(unittest.TestCase):


    def setUp(self):
        self.lqo = lrcFileOper.LrcQcOperation()
    
    def tearDown(self):
        pass

    def testRun(self):
        self.lqo.run()
    
    
if __name__ == '__main__':
    unittest.main()