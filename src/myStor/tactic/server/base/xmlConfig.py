#!/usr/bin/env python2.6
#  -*- coding: utf-8 -*-

#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

"""
Created on 2012-10-09

@author: lavenda
"""



import os
from xml.dom import minidom

class XmlConfig(object):
    """
    classdocs
    """

    def __init__(self,project_name=None):
        self.project_name = project_name
        self.xmlPath = os.path.dirname(__file__)+'/config/tactic_config.xml'

        
        
    def getServerData(self):
        """
        get the server data from xml
        
        @return: dictionary type, means serverData.
        """
        doc = minidom.parse(self.xmlPath)
        root = doc.documentElement
        
        tactic_server = root.getElementsByTagName('tactic_server')[0]
        server_ip = tactic_server.getElementsByTagName('server_ip')[0].firstChild.nodeValue
        login_user = tactic_server.getElementsByTagName('login_user')[0].firstChild.nodeValue
        login_password = tactic_server.getElementsByTagName('login_password')[0].firstChild.nodeValue
        
        if(tactic_server==None or server_ip==None or login_user==None or login_password==None):
            print("tactic_Config.xml error,server None!")
            return None
        
        serverData = {'server_ip':server_ip,'login_user':login_user,'login_password':login_password}
        return serverData
    
    
    def getDBData(self):
        """
        get the database data from xml
        
        @return: dictionary type, means database data.
        """
        doc = minidom.parse(self.xmlPath)
        root = doc.documentElement
        
        tactic_DB = root.getElementsByTagName('tactic_DB')[0]
        db_type = tactic_DB.getElementsByTagName('db_type')[0].firstChild.nodeValue
        host = tactic_DB.getElementsByTagName('host')[0].firstChild.nodeValue
        user = tactic_DB.getElementsByTagName('user')[0].firstChild.nodeValue
        password = tactic_DB.getElementsByTagName('password')[0].firstChild.nodeValue
        port = tactic_DB.getElementsByTagName('port')[0].firstChild.nodeValue
        
        if (tactic_DB==None or db_type==None or host==None or 
            user==None or password==None or port==None):
            print("tactic_Config.xml error,DB None!")
            return None
        
        DBData = {'db_type':db_type,'host':host,'user':user,'password':password,'port':port}
        return DBData
    
    
    def getMainProjectName(self):
        """
        get the main project name
        @return: string type, means the main project
        """
        root =  minidom.parse(self.xmlPath)
        projectMainName = root.getElementsByTagName('main_project_name')[0].firstChild.nodeValue
        if(self.project_name == None):
            self.project_name = projectMainName
        return projectMainName
    
    
    def getProjectData(self,pluginType=None):
        """
        get the project data from xml
        """
        doc = minidom.parse(self.xmlPath)
        root = doc.documentElement
        
        projectData={}
        project_details = root.getElementsByTagName('project_detail')
        for project_detail in project_details:
            project_name = project_detail.getAttribute('name')
            if(project_name != self.project_name):
                continue
            projectData={}
            asset_schemas = project_detail.getElementsByTagName('asset_schema')
            for asset_schema in asset_schemas:
                asset_schema_type = asset_schema.getAttribute('pluginType')
                if(asset_schema_type != pluginType):
                    continue
                schema_name = asset_schema.getElementsByTagName('schema_name')[0].firstChild.nodeValue
                schema_libs = asset_schema.getElementsByTagName('schema_lib')
                lib_nameTOcolumn_name = {}
                for schema_lib in schema_libs:
                    lib_name = schema_lib.getElementsByTagName('lib_name')[0].firstChild.nodeValue
                    column_name = schema_lib.getElementsByTagName('column_name')[0].firstChild.nodeValue
                    lib_nameTOcolumn_name[lib_name]=column_name
                projectData[schema_name]={'schema_lib':lib_nameTOcolumn_name,'schema_name':schema_name}
        print projectData
        return projectData
    
    
    
    #获取XML上translate的资料
    def translateData(self):
        """
        the translate data that the EN to CN
        """
        doc = minidom.parse(self.xmlPath)
        root = doc.documentElement
        translateData = {}
        project_details = root.getElementsByTagName('project_detail')
        for project_detail in project_details:
            asset_schemas = project_detail.getElementsByTagName('asset_schema')
            for asset_schema in asset_schemas:
                schema_name = asset_schema.getElementsByTagName('schema_name')[0]
                translateData[schema_name.firstChild.nodeValue] = schema_name.getAttribute('CN_name')
                schema_libs = asset_schema.getElementsByTagName('schema_lib')
                for schema_lib in schema_libs:
                    lib_name = schema_lib.getElementsByTagName('lib_name')[0]
                    translateData[lib_name.firstChild.nodeValue] = lib_name.getAttribute('CN_name')
                    column_name = schema_lib.getElementsByTagName('column_name')[0]
                    translateData[column_name.firstChild.nodeValue] = column_name.getAttribute('CN_name')
        return translateData


def main():
    pass

if __name__ == '__main__':
    main()
