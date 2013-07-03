import os, sys
import re

def DW_compareFileTexPath(fileList):
    
    f = open(fileList, 'r')
    f2 = open("D:/dw_lookupTexture.log", 'w')
    lines = f.readlines()
    for l in lines:
        bool = False
        print l.strip()
        try:
            f1 = open(l.strip(), 'r')
        except:
            print l, " dont live"
            continue
            
        lines1 = f1.readlines()

        for ll in lines1:

            if(".ftn" in ll):

                temp = re.findall("\$JOB_ASSETS.*sourceimages[\w\W/_][^\"]*|[\w]:[\w\W/_][^\"]*", ll)
#                print temp
                try:
                    temp = os.path.normpath(temp[0])
                except:
                    continue

                if(not re.findall("[\w]:", temp)):
#                    temp = "S:\E020DW\DWep20\\" + temp
                    temp = temp.replace("$JOB_ASSETS", "S:\E020DW\DWep20\sourceimages")
#                    print temp
                    
                if(os.path.isfile(temp)):
                    #print "file exists!"
                    pass
                else:
                    print temp
                    bool = True
                    f2.write(temp+"\n")
#                    f2.write("\r\n")
                    
        if(bool):
#            print bool
#            print l.split("\r\n")[0]
#            f2.write(l.split("\r\n")[0]+"\n")
#            pass
            pass
        
        f1.close()

    f.close()
    f2.close()

DW_compareFileTexPath(r"C:\Users\huangchengqi\Desktop\drgn2015\TEXHIFilesFullPathInE020DW.txt")