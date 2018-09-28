#!/usr/bin/env python
#coding:utf-8
import json
HuaweiCommand = [
"screen-length 0 temporary",
"screen-length disable",
"display bgp peer",
"display ospf peer",
"display ospf brief",
"display version",
"display health",
"display fan",
"display power",
"display temperature",
"display temperature all",
"display device",
"display cpu-usage",
"display memory-usage",
"display interface",
"display ip interface",
"display interface brief",
"display counters",
"display counters error",
"display counters rate",
"display alarm statistics",
"display alarm information",
"display trapbuffer",
"display logbuffer",
]
with open('HuaweiCommand.txt', 'w') as f:
    json.dump(HuaweiCommand, f)
