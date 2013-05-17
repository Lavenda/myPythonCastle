var title = 'Downloading';
var msg = 'is downloading all the file...';
spt.app_busy.show(title,msg);

var applet = spt.Applet.get();
var server = TacticServerStub.get();
var PLAYER = "explorer";
var sobject = server.get_by_search_key(bvr.search_key);
var code = sobject.code;
var snapshotGroup = server.get_all_children(bvr.search_key,'sthpw/snapshot');

for (var i = 0; i < snapshotGroup.length; i++) {
	snapshot = snapshotGroup[i];
	if (snapshot['is_current'] != true)
		continue;
	snapshotCode = snapshot['code'];
	var path = server.get_path_from_snapshot(snapshotCode);
	var sandbox_dir = server.get_client_dir(snapshotCode,{mode:'sandbox'});
	var basename = spt.path.get_basename(path);
	sandbox_path = sandbox_dir+ '/' +basename;
	applet.copytree(path,sandbox_path);
}

var parts = sandbox_dir.split(/[\/\\]/);
parts.pop();
parts.pop();
var path2 = parts.join("\\");
var exec = PLAYER + ' "' +path2+ '"';
applet.exec_shell(exec, false);
spt.app_busy.hide();