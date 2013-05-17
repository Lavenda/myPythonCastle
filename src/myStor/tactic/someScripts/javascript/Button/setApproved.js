var applet = spt.Applet.get();
var server = TacticServerStub.get();

var sobject = server.get_by_search_key(bvr.search_key);
var sk = bvr.search_key;
var context = sobject.context;
var toContext = context+'DW';
var code = sobject.code;
var path = server.get_path_from_snapshot(code)
var msg = 'Confirm to approved it ?';
if (confirm(msg) ) {
    var item_sk = server.get_parent(sk).__search_key__;
    var snapshots = server.get_all_children(item_sk,'sthpw/snapshot');

    var i;
    for(i in snapshots)
    {
        if(snapshots[i].context == context)
        { 
            var snapshot_sk = snapshots[i].__search_key__;
            snapshot_data={'isapproved':'Pending'};
            server.update(snapshot_sk,snapshot_data);
        }
    }
    server.start();
    try
    {
    var new_snapshot = server.create_snapshot(item_sk,toContext);
    var result = server.add_file(new_snapshot.code,path);
    }
    catch(e) {
           alert(spt.exception.handler(e));
           server.abort();

        }
    server.finish();
    if(result != null)
    {
        alert('Success');
        data={'isapproved':'Approved'};
    }
    else
    {
        alert('Failure');
        data={'isapproved':'Unupload'};
    }
    server.update(sk,data);
    spt.dg_table.search_cbk(evt,bvr);
}