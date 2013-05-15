'''
Created on 2013-5-6

@author: lavenda
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-
def timer(func, count=1, every=1, *args, **kwargs):
    '''
    This method is used to calculate time of the progarm you run.
    But this time is only to calculate the CPU time which your program has used.
    
    @param func: the function want to run.
    @type func: the method object.
    @param count: how many times you want to run this program.
    @type count: int(default:1)
    @param every: how many rounds you want to run this program in one time.
    @type every: int(default:1)
    
    @see: you can use it like as follows:
        'a=1000, b=100' is the attributes of the testTimer
        e.g:
            from normal import tools
            tools.timer(func=testTimer, count=3, every=100, a=1000, b=100)
        
    '''
    
    import time
    funcName = func.__name__
    runTimeGroup = []
    
    for i in range(count):
        startTime = time.clock()
        
        for j in range(every):
            apply(func, args, kwargs)
        endTime = time.clock()
        runTime = endTime-startTime
        runTimeGroup.append(runTime)
        print '%s: Running <%s> %s times uses <%s seconds>' %(str(i), funcName, str(every), runTime)
        
    returnData = func(*args, **kwargs)
    print runTimeGroup
    return returnData
