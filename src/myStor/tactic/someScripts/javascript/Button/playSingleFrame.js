PLAYER = "explorer"
var CONTEXT = "LGT_Mov";
var EXPRESSION = "@SOBJECT(sthpw/snapshot['context', '"+CONTEXT+"']['version','>',0])"

//var EXPRESSION = "@SOBJECT(di/job.sthpw/snapshot)"

//-------Setup------------------------------------

var applet = spt.Applet.get();
var server = TacticServerStub.get();
var sobject = server.get_by_search_key(bvr.search_key);
var code = sobject.code;
//alert(bvr.search_key)


var cmd = []
cmd.push("rv -tile")
var snapshot = server.eval(EXPRESSION, {'search_keys': bvr.search_key})
//alert(snapshot)
if (!snapshot[0]){
//alert(code  + ":NO Review found");

}
else
{

	for (var i = 0; i < snapshot.length; i++ ) 
	{
	var path = server.get_path_from_snapshot(snapshot[i].code);
	
	cmd.push(path);
	}
	cmd = cmd.join(" ")
//	spt.app_busy.show("Loading Tweak RV", "...")
	// Execute the command
//	alert(cmd)
	applet.exec_shell(cmd, false);
	//applet.exec_shell(cmd);
//	spt.app_busy.hide();
}
