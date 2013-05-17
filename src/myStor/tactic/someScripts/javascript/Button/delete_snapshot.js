var msg = 'Confirm to Delete it ?';
if (confirm(msg) ) {
	var sandbox = base_dirs.win32_sandbox_dir;
	var bk_path = sandbox + '/deleted_snapshots_file/'
	var server = TacticServerStub.get();
	var applet = spt.Applet.get();
	var sobject = server.get_by_search_key(bvr.search_key);
	var snapshot_sk = bvr.search_key;
	var snapshot_code = sobject.code;
	var snapshot_code_filters = [['snapshot_code',snapshot_code]];
	var files_obj = server.query('sthpw/file',{'filters':snapshot_code_filters});
	for(var i=0;i<files_obj.length;i++){
		var file_name = files_obj[i]['file_name'];
		var full_path = 'S:' + '/' + files_obj[i]['relative_dir'] + '/' + file_name;
		if(!(applet.exists(bk_path)))
			{applet.makedirs(bk_path);}
		applet.move_file(full_path,bk_path+file_name);
		server.delete_sobject(files_obj[i]['__search_key__']);}
	server.delete_sobject(snapshot_sk);
	spt.dg_table.search_cbk(evt,bvr);
}