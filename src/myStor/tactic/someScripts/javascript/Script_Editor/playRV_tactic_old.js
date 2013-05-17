var server = TacticServerStub.get();
var base_dirs = server.get_base_dirs();
var sandbox = base_dirs.win32_sandbox_dir;

var bat_path2 = sandbox + '/rv/tactic_rv.txt';
alert(bat_path2);
var bat_path = 'D:/tactic_rv.txt';
var bvr = input[0];
var context = input[1];
var server = TacticServerStub.get();
var applet = spt.Applet.get();
var activator = spt.smenu.get_activator(bvr);
var layout = activator.getParent('.spt_layout');
spt.table.set_layout(layout);
var table = spt.get_cousin( activator, '.spt_table_top', '.spt_table_table' );
var selected_rows = spt.table.get_selected_rows();
var cmd = 'py-interp.exe S:/workflowtools/digital37/RV/RVQC_LGT_TARTIC.py -t '+ bat_path2;
var paths_txt=[];
for(var i=0;i<selected_rows.length;i++)
{
    item_sk = selected_rows[i].getAttribute('spt_search_key');
    snapshots = server.get_all_children(item_sk, 'sthpw/snapshot');
    for(var j=0;j<snapshots.length;j++)
    {
        var snapshot = snapshots[j];
        if(snapshot.context == context && snapshot.version!='0' && snapshot.version!='-1' )
        { 
            var snapshot_code = snapshot.code;
            var path = server.get_path_from_snapshot(snapshot_code);
            if(path != '')
            {paths_txt.push(path);}
        }
    }
}
alert(paths_txt.length);
paths_txt = paths_txt.join("\n\r");
alert(paths_txt);
applet.create_file(bat_path2,paths_txt);
alert(cmd);
var a = applet.exec_shell(cmd, true);
alert(a);