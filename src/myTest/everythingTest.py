'''
Created on 2013-5-23

@author: lavenda
'''

import os

def main(*args, **kwargs):
    sub(*args, **kwargs)


def sub(*args, **kwargs):
    print args, kwargs
    

if __name__ == '__main__':
    print type(os.system)