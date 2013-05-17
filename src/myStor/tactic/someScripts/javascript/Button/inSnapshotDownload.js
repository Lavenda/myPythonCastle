var PLAYER = "explorer"
var applet = spt.Applet.get();
var server = TacticServerStub.get();

var sobject = server.get_by_search_key(bvr.search_key);
var code = sobject.code;
var path = server.get_path_from_snapshot(code);
var sandbox_dir = server.get_client_dir(sobject,{mode:'sandbox'});
var basename = spt.path.get_basename(path);

sandbox_path = sandbox_dir+ '/' +basename;
applet.copytree(path,sandbox_path)
var parts = sandbox_dir.split(/[\/\\]/);
var path2 = parts.join("\\");
var exec = PLAYER + ' "' +path2+ '"';
applet.exec_shell(exec, false);