snapshot_process = input['update_data'].get('process')
snapshot_description = input['update_data'].get('description')

item=  server.get_parent(input['search_key'])
tasks = server.get_all_children(item["__search_key__"],'sthpw/task')

for task in tasks:
    if (task['process'] == snapshot_process):
        server.update(task['__search_key__'], {'status': 'Updated'})
    if (task['process'] == 'ANI_Review'):
        sversion = int(item['ani_review_sversion']) + 1
        sversion_str = str(sversion)
        if(len(sversion_str)==1):
            sversion_str = '0'+sversion_str
        server.update(item['__search_key__'], {'ani_review_sversion': sversion_str})