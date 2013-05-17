chg_start_date = input['sobject'].get('bid_start_date')
chg_process = input['sobject'].get('context')
chg_sk = input['sobject'].get('__search_key__')
if(chg_process == 'ANI_Blocking' or chg_process == 'ANI_polish'):
    data = {'actual_start_date':chg_start_date}
    server.update(search_key=chg_sk, data=data)
           

