inst_context = input['sobject'].get('context')
inst_search_type = input['sobject'].get('search_type')
f = open('/home/apache/text.txt','a')
f.write(str(input))
f.close()
if(inst_context in ['LGT_Frame','LGT_Mov'] and inst_search_type=='E008DW/dw09_shot?project=E008DW'):
    sobject = input['sobject']
    inst_note = sobject.get('note')
    inst_login = sobject.get('login')
    inst_project_code = sobject.get('project_code')
    inst_sk = sobject.get('__search_key__')
    
    data = {'project_code':inst_project_code,'search_type':'sthpw/snapshot','login':inst_login,'context':inst_context,\
    'note':inst_note}
    
    item = server.get_parent(search_key=inst_sk)
    item_sk = item['__search_key__']
    snapshot = server.get_snapshot(search_key=item_sk, context=inst_context, version='-1')
    snapshot_sk = snapshot['__search_key__']
    server.insert(search_type='sthpw/note', data=data, parent_key=snapshot_sk, triggers=False)

elif(inst_context in ['LGT_Frame','LGT_Mov'] and inst_search_type=='sthpw/snapshot'):
    sobject = input['sobject']
    inst_note = sobject.get('note')
    inst_login = sobject.get('login')
    inst_project_code = sobject.get('project_code')
    inst_sk = sobject.get('__search_key__')
    
    item = server.get_parent(search_key=inst_sk)
    item_id = item['id']
    item_sk = item['__search_key__']
    data = {'project_code':inst_project_code,'search_type':'E008DW/dw09_shot','login':inst_login,'context':inst_context,\
    'note':inst_note,'search_id':item_id}   
    inst_note = server.insert(search_type='sthpw/note', data=data, parent_key=item_sk, triggers=False)