sthpw/snapshot
snapshot_layout
@SOBJECT(sthpw/snapshot['context','LGT_Frame'])
tactic.ui.panel.TableLayoutWdg


{@GET(sthpw/snapshot['is_current','1']['context','LGT_Mov'].version)}


LGT_MovDW <br/>
last_version:   {@GET(sthpw/snapshot['is_current','1']['context','LGT_MovDW'].version)}<br/>
time:   {@FORMAT(@GET(sthpw/snapshot['is_current','1']['context','LGT_MovDW'].timestamp),'1999-12-31')}<br/><br/>
LGT_FrameDW <br/>
last_version:   {@GET(sthpw/snapshot['is_current','1']['context','LGT_FrameDW'].version)}<br/>
time:   {@FORMAT(@GET(sthpw/snapshot['is_current','1']['context','LGT_FrameDW'].timestamp),'1999-12-31')}<br/>



tactic.ui.filter.DateFilterElementWdg
tactic.ui.filter.DateRangeFilterElementWdg