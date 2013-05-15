'''
Created on 2013-5-6

@author: lavenda
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-
def timer(count=1, every=1):
    '''
    This method is used to calculate time of the progarm you run.
    But this time is only to calculate the CPU time which your program has used.
    
    @param count: how many times you want to run this program.
    @type count: int(default:1)
    @param every: how many rounds you want to run this program in one time.
    @type every: int(default:1)
    
    @see: you can use it like as follows:
        you can run the method straightly, and the result also print into the Console.
        e.g:
            from decorator import tools
            
            @tools.timer(count=3, every=100)
            def testTimer(a, b):
                ....
        
    '''
    import time
    def _timer(func):
        def __timer(*args, **kwargs):
            funcName = func.__name__
            runTimeGroup = []
            
            for i in xrange(count):
                startTime = time.clock()
                
                for j in xrange(every):
                    func(*args, **kwargs)
                endTime = time.clock()
                runTime = (endTime-startTime)
                runTimeGroup.append(runTime)
                print '%s: Running <%s> %s times uses <%s seconds>' %(str(i), funcName, str(every), runTime)
                
            returnData = func(*args, **kwargs)
            print runTimeGroup
            return returnData
        return __timer
    return _timer
