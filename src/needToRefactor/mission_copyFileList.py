#  -*- coding: utf-8 -*-
'''
Created on 2012-12-12

@author: luxun
'''
import os, time, ConfigParser, re, shutil


class core:
    mode = 'ma'
    doCopy = False
    
    def getVersion(self, filename):
        v = 0
        try:
            buf = filename.lower().split('.')
            buf = buf[0].rsplit('_',1)
            v = int( buf[-1][1:] )
        except:
            pass
        return v
    
    def getFile(self, dir, file):
        array = []
        base = file.split('.')#.lower()
        if not os.path.exists(dir):
            return ''
        files = os.listdir(dir)
        for f in files:
            if self.getVersion(f)>=100:
                continue
            b = f.split('.')#.lower()
            if len(b)==2:
                #if b[1].lower()==base[1].lower() and b[0].lower().startswith(base[0].rsplit('_',1)[0].lower()):
                if b[1].lower()==base[1].lower() and b[0].lower().startswith(base[0].lower()):
                    path = os.path.join(dir,f)
                    #array.append(os.path.normcase(path))
                    array.append( path )
        array.sort()
        if array:
            return array[-1]
        else:
            return ''
    def getLocalPath(self, sourcePath):
        return sourcePath.replace( SOURCE_FOLDER, TARGET_FOLDER )
        #return os.path.normcase(sourcePath).replace( os.path.normcase(SOURCE_FOLDER), TARGET_FOLDER )
    
    def sameStat(self, f1, f2):
        value = False
        try:
            value = os.stat(f1).st_mtime<=os.stat(f2).st_mtime
        except:
            pass
        return value
    
    def do(self):
        total = 0
        zero = 0
        lost = 0
        exists = 0
        copied = 0
        noCopy = 0
        con = []
        noExistsFileList = []
        zeroFileList = []
        failedCopyList = []
        
        f1 = open(ALL_FILE,'r')
        #lines = f1.readlines()
        lines = [line.strip() for line in f1.readlines() if line.strip()]
        f1.close()
        
        total = len(lines)
        for index, line in enumerate(lines):
            print (total-index)
#            if not line.strip():
#                continue
#            
#            total += 1
            path = os.path.join( SOURCE_FOLDER, line.strip() )
            path_orig = line.strip()
            
            dir, file = os.path.split(path)
            if self.mode != 'images':
                ### Add ver folder -------------------------------------
                if not os.path.normcase(dir).endswith('models'):
                    dir = os.path.join(dir, 'ver')
                ### ----------------------------------------------------
                
                ### Get Last version file ------------------------------
                path = self.getFile(dir, file)
                ### ----------------------------------------------------
            print path

            if not os.path.exists(path):
                lost += 1
                print 'No exists file:', path
                noExistsFileList.append('%s\n' % path_orig)
            elif not os.path.getsize(path):
                zero += 1
                print 'Zero file:', path
                zeroFileList.append('%s\n' % path_orig)
            else:
                localPath = self.getLocalPath(path)
                if not self.sameStat(path, localPath):
                    try:
                        localDir = os.path.dirname(localPath)
                        if self.doCopy:
                            ### Copy file --------------------
                            if not os.path.exists( localDir ):
                                os.makedirs(localDir)
                                print 'Make Dir:', localDir
                            shutil.copy2(path, localPath)
                            copied += 1
                            print 'Copy file:', localPath
                            ### ------------------------------
                        
                    except:
                        noCopy += 1
                        failedCopyList.append('%s\n' % path_orig)
                        print 'Failed copy file:', path
                else:
                    exists += 1
                    print 'Exists file:', localPath

        str = '\nTotal file: %s\nLost file: %s\nZero file: %s\n\nExists file: %s\nCopy file: %s\nFailed copy: %s' % (total, lost, zero, exists, copied, noCopy)
        print str
        
        noExistsFileList.sort()
        zeroFileList.sort()
        failedCopyList.sort()

        if noExistsFileList:
            con.append('No exists file:\n')
            con.extend(noExistsFileList)
        if zeroFileList:
            con.append('Zero file:\n')
            con.extend(zeroFileList)
        if failedCopyList:
            con.append('Failed copy:\n')
            con.extend(failedCopyList)

        con.append( str )
        f2 = open(LOG_FILE,'w')
        f2.writelines(con)
        f2.close()
            
obj = core()

# Copy images
SOURCE_FOLDER = r'W:\dragon_mstr'
TARGET_FOLDER = r'S:\E008DW\Data_ from_DW\preAsset\20130704\sourceimages_noMap'
ALL_FILE = r'C:\Users\huangchengqi\Desktop\drgn2015\genericjim_aNoMap.txt'
LOG_FILE = r'S:\E008DW\Data_ from_DW\preAsset\20130704\sourceimages_noMap\list_info.txt'
obj.mode = 'images'

# Copy ma 相对路径、无ver、无版本号
#SOURCE_FOLDER = r'W:\dragon_mstr'
#TARGET_FOLDER = r'S:\E008DW\Data_ from_DW\preAsset\20130703'
#ALL_FILE = r'C:\Users\huangchengqi\Desktop\drgn2015\needCopyFromServer4.txt'
#LOG_FILE = r'S:\E008DW\Data_ from_DW\preAsset\20130703\list_info.txt'
#obj.mode = 'ma'

obj.doCopy = True
obj.do()

