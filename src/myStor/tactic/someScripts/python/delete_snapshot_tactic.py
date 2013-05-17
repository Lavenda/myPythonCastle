
snapshot_code = snapshot_obj['code']
snapshot_sk = snapshot_obj['__search_key__']
snapshot_code_filters = [('snapshot_code',snapshot_code)]

files_obj = self.server.query( search_type ='sthpw/file',filters=snapshot_code_filters)

for file_obj in files_obj:
    full_path = '/home/apache/assets' + '/' + file_obj['relative_dir'] + '/' + file_obj['file_name']

    if(not os.path.exists('/home/apache/deleted_snapshot_file')):
        os.mkdir('/home/apache/deleted_snapshot_file')
    shutil.copy(full_path,'/home/apache/deleted_snapshot_file')
    os.remove(full_path)
    self.server.delete_sobject(search_key = file_obj['__search_key__'])
self.server.delete_sobject(search_key = snapshot_sk)
