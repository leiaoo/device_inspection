#!/usr/bin/env python
#coding:utf-8
import json
ciscoCommand = [
'ter length 0',
'show version',
'show env',
'show env fex all ',
'show module',
'show processes cpu',
'show processes cpu history',
'show system resource ',
'show interface',
'show inter statu',
'show inter status | in "a-100 "',
'show inter status err-dis',
'show vpc brief',
'show hsrp brief',
'show ip ospf nei',
'show ip bgp nei',
'show spanning-tree root',
'show port-channel sum',
'show logging',
]
with open('NexusCommand.txt', 'w') as f:
    json.dump(ciscoCommand, f)
