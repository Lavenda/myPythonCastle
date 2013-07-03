import os
import re

class Asset_Info():
    PROJECT = 'S:/E020DW/DWep20'
    
    def __init__(self):
        self.Assets = set()
        self.Assets_Info = dict()
        self.Miss = set()
        self.Assets_Tex = set()
        self.Assets_Path = set()

    def get_asset(self):
        with open(r'C:\Users\huangchengqi\Desktop\drgn2015\AllRefPath.txt','r') as f:
            for x in f:
                x = x.strip()
                # remove same asset
                self.Assets.add( os.path.join(Asset_Info.PROJECT,x) )
                
    def exists(self,f):
        if os.path.exists(f) :
            return '1'
        else:
            # no exists file list
            self.Miss.add(f)
            return '0'
        
    def write_file(self,fileName,content):
        f = open(fileName,'w')
        if content:
            for x in content:
                #f.write('%s\r\n' % x)
                f.write('%s\n' % x)
            f.close()
            
    def get_info(self):
        asset_list = set()
        self.get_asset()
        title_info = 'Asset\tPRX\tRIG_PRX\tRIG_HI\tTEX_HI\tCHRFX'
        #print title_info
        #asset_list.add(title_info)
        
        for x in self.Assets:
            
            # RIG
            #_assets/env/set_ext/berk_island/models/PRX/berk_island_PRX.ma
            # _assets/prop/foliage/tree/tree_burnt_01/models/tree_burnt_01_MSTR.ma
            #_assets/char/human/astrid/astrid_default/models/RIG/astrid_default_RIG_PRX.ma
            #_assets/env/ocean/ocean/models/PRX/ver/ocean_PRX_v01.ma
            #_assets/env/ocean/ocean/models/PRX/ocean_PRX.ma
                
            x_dir = os.path.dirname(x)
            x = os.path.basename(x)
            
            #asset_path = os.path.dirname( os.path.dirname(x_dir) ).replace('%s\\' % Asset_Info.PROJECT,'').replace('_assets/','')
            
            # IMPORTANT: case:
            if x_dir.endswith('models'):
                # case for: _assets/env/landscape/groundscape/groundscape_cliff_01/models/groundscape_cliff_01_MSTR.ma
                asset_path = os.path.dirname(x_dir).replace('%s\\' % Asset_Info.PROJECT,'')
            else:
                # case for: _assets/char/human/astrid/astrid_default/models/RIG/astrid_default_RIG_PRX.ma
                asset_path = os.path.dirname( os.path.dirname(x_dir) ).replace('%s\\' % Asset_Info.PROJECT,'')
            print 'Asset:\t%s' % asset_path
            
            x_no_ext = os.path.splitext(x)[0]
            
            # if has key then skip, else process
            if not self.Assets_Info.has_key(x_no_ext):
                
                self.Assets_Info[x_no_ext] = dict()
                self.Assets_Path.add(asset_path)
                
                print 'Source:\t%s' % x
                # get RIG_HI
                if x.endswith('_MDL_PRX.ma'):
                    x_dir = x_dir.replace('MDL','RIG')
                    x = x.replace('_MDL_PRX.ma','_RIG_HI.ma')
                elif x.endswith('_RIG_LW.ma'):
                    x_dir = x_dir.replace('RIG','RIG')
                    x = x.replace('_RIG_LW.ma','_RIG_HI.ma')
                elif x.endswith('_PRX.ma'):
                    if x.endswith('_RIG_PRX.ma'):
                        x_dir = x_dir.replace('RIG','RIG')
                        x = x.replace('_RIG_PRX.ma','_RIG_HI.ma')
                    else:
                        x_dir = x_dir.replace('PRX','RIG')
                        x = x.replace('_PRX.ma','_RIG_HI.ma')
                elif x.endswith('_MDL.ma'):
                    x_dir = x_dir.replace('MDL','RIG')
                    x = x.replace('_MDL.ma','_RIG_HI.ma')
                elif x.endswith('_MDL_HI.ma'):
                    x_dir = x_dir.replace('MDL','RIG')
                    x = x.replace('_MDL_HI.ma','_RIG_HI.ma')
                elif x.endswith('_MSTR.ma'):
                    x_dir = '%s/RIG' % x_dir
                    x = x.replace('_MSTR.ma','_RIG_HI.ma')
                elif x.endswith('_TEX_HI.ma'):
                    x_dir = x_dir.replace('TEX','RIG')
                    x = x.replace('_TEX_HI.ma','_RIG_HI.ma')
                elif x.endswith('_chrFX.ma'):
                    x_dir = x_dir.replace('chrFX','RIG')
                    x = x.replace('_chrFX.ma','_RIG_HI.ma')
                else:
                    print 'error extension'
                    print x
                
                #print 'dir name:\t%s' % x_dir
                #print 'file name:\t%s' % x
                x = os.path.join(x_dir,x).replace('\\','/')
                print 'full path:\t%s' % x
                self.Assets_Info[x_no_ext]['RIG_HI'] = x
                print 'RIG_HI:\t%s' % self.Assets_Info[x_no_ext]['RIG_HI']
                
                # get PRX
                self.Assets_Info[x_no_ext]['PRX'] = x.replace('RIG_HI','PRX').replace('RIG','PRX')
                print 'PRX:\t%s' % self.Assets_Info[x_no_ext]['PRX']
                
                # get RIG_PRX
                self.Assets_Info[x_no_ext]['RIG_PRX'] = x.replace('RIG_HI','RIG_PRX')
                print 'RIG_PRX:\t%s' % self.Assets_Info[x_no_ext]['RIG_PRX']
                
                # get TEX_HI
                self.Assets_Info[x_no_ext]['TEX_HI'] = x.replace('RIG_HI','TEX_HI').replace('RIG','TEX')
                print 'TEX_HI:\t%s' % self.Assets_Info[x_no_ext]['TEX_HI']
                
                # 
                self.Assets_Tex.add( self.Assets_Info[x_no_ext]['TEX_HI'] )
                
                # get chrFX
                self.Assets_Info[x_no_ext]['chrFX'] = x.replace('RIG_HI','chrFX').replace('RIG','chrFX')
                print 'chrFX:\t%s' % self.Assets_Info[x_no_ext]['chrFX']
                
                # get chrFX
                self.Assets_Info[x_no_ext]['MSTR'] = x.replace('RIG_HI','MSTR').replace('RIG','')
                print 'MSTR:\t%s' % self.Assets_Info[x_no_ext]['MSTR']
                
                
                w = '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (asset_path, self.exists(self.Assets_Info[x_no_ext]['PRX']),\
                                                self.exists(self.Assets_Info[x_no_ext]['RIG_PRX']),\
                                            self.exists(self.Assets_Info[x_no_ext]['RIG_HI']),\
                                           self.exists(self.Assets_Info[x_no_ext]['TEX_HI']),\
                                           self.exists(self.Assets_Info[x_no_ext]['chrFX']),\
                                           self.exists(self.Assets_Info[x_no_ext]['MSTR'])) 
                print w
                asset_list.add(w)
            
        # write info to file
        asset_list = list(asset_list)
        asset_list.sort()
        asset_list.insert(0, title_info)
        self.write_file('d:/drgn/asset/assetInfo.txt', asset_list)
            
        self.Miss = list(self.Miss)
        self.Miss.sort()
        
        self.write_file('d:/drgn/asset/assetMissInfo.txt', self.Miss)
        
        # write tex file
        self.write_file('d:/drgn/asset/assetTex.txt', self.Assets_Tex)
        
        # write asset path file
        self.write_file('d:/drgn/asset/assetPath.txt', self.Assets_Path)
        
        print 'asset_list'
        print asset_list
                
def main():
    Asset_Info().get_info()
    
if __name__=='__main__':
    main()

    