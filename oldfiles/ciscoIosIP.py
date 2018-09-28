#!/usr/bin/etc python
#coding:utf-8

import json

ciscoIosIP = {
    "ZZDC4F29SWH601-M2" : "172.31.253.90",
}

with open('ciscoIosIP.txt', 'w') as f:
    json.dump(ciscoIosIP, f)

