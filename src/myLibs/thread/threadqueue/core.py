'''
Created on 2013-5-2

@author: lavenda
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import myCommand.MyCommand as MyCommand
import myCommandQueue.MyCommandQueue as MyCommandQueue
import myThread.MyThread as MyThread
import threading
import types 

class Core(object):
    '''
    This class is the core of the process queue tool.
    It contains most of the local codes, but also part of code in other classes.
    The problem of getting commands from the myCommandQueue has not been solved, 
    which will make the dependency relationship between the MyThread and the MyCommandQueue.
    It also will make other unknow problem, such as making every thread in a mess between method and method.
    
    - methodNameToLock: It is a static dictionary type. There are many detail of which method needs to be lock.
    '''

    methodNameToLock = {}

    def __init__(self, count=100):
        '''
        @param count: means how many command you want to run
        @type count: int type(default:100)
        - commandQueue: It is a MyCommandQueue object.
        
        '''
        self.commandQueue = MyCommandQueue(count)
    
    
    def build(self, methodObject, isLock=False, priority=3, *args, **kwargs):
        '''
        This method is used to init the command queue.
        It will create a Command object and take it into a command queue.
        
        @param methodObject: as its name, it must be a method object.
        @type methodObject: method object
        @param isLock: means whether this method needs to be synchronization.
        @type isLock: boolean type
        @param priority: means the priority of commands.
        @type priority: int type 
        
        @return: a boolean type, means whether putting a command into the queue is successful.
        
        '''
        
        if isinstance(methodObject, types.MethodType) or isinstance(methodObject, types.FunctionType):
            command = self._createCommand(methodObject, isLock, priority, args, kwargs)
            isPutSuccess = self.commandQueue.put(command)
        else:
            isPutSuccess = False
            
        return isPutSuccess
    
    
    def run(self, threadCount=4):
        '''
        This method is used to run all commands in queue with difference threads after the build method.
        
        @param threadCount: means how many thread you need to run.
        @type threadCount: int type(default:4)
        
        @return: an boolean type, means whether all the comannds run accurately.
        '''
        threads = []
        for i in range(threadCount):
            try:
                thread = MyThread(self.commandQueue)
            except:
                continue
            threads.append(thread)
            
        for thread in threads:
            try:
                thread.start()
            except:
                continue
        
#        for thread in threads:
#            thread.join()
        return True
    
    
    def _createCommand(self, methodObject, isLock, priority, args, kwargs):
        '''
        - A private method.
        This method is used to create a Command object.
        
        @param methodObject: as its name, it must be a method object.
        @type methodObject: method object
        @param isLock: means whether this method needs to be synchronization.
        @type isLock: boolean type,
        @param priority: means the priority of commands.
        @type priority: int type
        @param args: means the attributes of the method you want to run.
        @type args: list type
        @param kwargs: means the attributes of the method you want to run.
        @type kwargs: dictionary type
        
        @return: a command object.
        '''
        command = MyCommand()
        if isLock:
            lock = self._getLock(methodObject)
        else:
            lock = None
        command.setCommand(methodObject, lock, priority, args, kwargs)
        
        return command
    
    
    def _getLock(self, methodObject):
        '''
        - A private method.
        This method is used to get a Lock object when the method needs to be locked.
        
        @param methodObject: method type
        @type methodObject: method type
        
        @return: a Lock object.
        
        '''
        methodName = methodObject.__name__
        lock = self.methodNameToLock.get(methodName, None)
        if not lock:
            lock = threading.Lock()
            self.methodNameToLock[methodName] = lock
            
        return lock 
    


#just to test
if __name__ == '__main__':
    import test as t
    
    test = t.Test()
    range10000 = t.range10000
    core = Core(100)
    for i in range(50):
        core.build(methodObject=range10000, isLock=False, priority=3, str='aaa')
    for j in range(10):
        core.build(methodObject=range10000, isLock=False, priority=2.5, str='bbb')
    core.run()
    for k in range(10):
        core.build(methodObject=range10000, isLock=False, priority=2, str='cccccc')
