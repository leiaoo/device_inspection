#!/usr/bin/env python
#coding:utf-8
import json
ciscoCommand = [
'ter length 0',
'show version',
'show env all',
'show module',
'show process cpu',
'show process cpu history',
'show proc mem',
'show interface',
'show inter status',
'show inter status | i (a-100 )',
'show inter status err-disabled',
'show hsrp brief',
'show spanning tree root',
'show port-channel sum',
'show logging',
]
with open('IosCommand.txt', 'w') as f:
    json.dump(ciscoCommand, f)
