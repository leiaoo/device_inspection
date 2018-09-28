#!/usr/bin/env python
#coding:utf-8
import json
ciscoCommand = [
'ter length 0',
'show version',
'show env ',
'show module',
'show process cpu',
'show process cpu history',
'show proc mem',
'show interface',
'show inter statu',
'show inter status | in "a-100 "',
'show inter status err-dis',
'show hsrp brief',
'show spanning tree root',
'show port-channel sum',
'show logging'
]
with open('IosCommand.txt', 'w') as f:
    json.dump(ciscoCommand, f)
