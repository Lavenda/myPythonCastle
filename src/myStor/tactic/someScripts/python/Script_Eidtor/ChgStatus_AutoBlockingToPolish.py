chg_assigned = input['sobject'].get('assigned')
chg_process = input['sobject'].get('context')
chg_sk = input['sobject'].get('__search_key__')


item = server.get_parent(search_key=chg_sk)
item_sk = item['__search_key__']
tasks_list = server.get_all_children(search_key=item_sk, child_type='sthpw/task',columns=['assigned','process'])
for task in tasks_list:
    data = {'assigned':chg_assigned}
    if(task['process'] == 'ANI_polish'):
        server.update(search_key=task['__search_key__'], data=data)
        break