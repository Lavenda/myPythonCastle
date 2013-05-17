var CONTEXT = "LAY_Sound";

var PLAYER = "explorer";
var EXPRESSION = "@SOBJECT(sthpw/snapshot['context', '"+CONTEXT+"']['is_current',1])";
var applet = spt.Applet.get();
var server = TacticServerStub.get();

var sobject = server.get_by_search_key(bvr.search_key);
var code = sobject.code;
var code_sk = sobject.__search_key__;

var snapshot = server.eval(EXPRESSION, {'search_keys': bvr.search_key});
if (snapshot[0]==null || snapshot[0]=='')
{
    alert(code  + ":NO "+CONTEXT+" found");
}
else
{
    var tasks = server.get_all_children(code_sk,'sthpw/task');
    for(var i=0;i<tasks.length;i++)
    {
        if(task.process == CONTEXT && task.status == 'assigned')
        {
            data = {'status':'InProgress'};
            server.update(task.__search_key__,data);
        }
    }
    var path = server.get_path_from_snapshot(snapshot[0].code);
    var sandbox_dir = server.get_client_dir(snapshot[0],{mode:'sandbox'});
    var basename = spt.path.get_basename(path);
    sandbox_path = sandbox_dir+ '/' +basename;
    applet.copytree(path,sandbox_path);
    var parts = sandbox_dir.split(/[\/\\]/);
    var path2 = parts.join("\\");
    var exec = PLAYER + ' "' +path2+ '"';
    applet.exec_shell(exec, false);
}