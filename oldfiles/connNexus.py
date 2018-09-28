#!/usr/bin/env python
#coding:utf-8

from netmiko import ConnectHandler
import datetime, json, os

#
timeString = datetime.datetime.now().strftime('%Y-%m-%d')

with open('ciscoNexusIP.txt', 'r') as f:
  ciscoIP = json.load(f)
with open('NexusCommand.txt', 'r') as f:
  ciscoCommand = json.load(f)

ciscoNexusDir = 'cisco_device/Nexus/' + timeString + '/'

if not os.path.exists(ciscoNexusDir):
    os.mkdir(ciscoNexusDir)

print(f'The device count is: {len(ciscoIP)}')
for lineIP in ciscoIP.values():
    ciscoDevice = {
        'device_type': 'cisco_nxos',
        'ip': lineIP,
        'username': 'zybank15',
        'password': 'Zbnet!1126',
        'port': 22,
        'secret': 'secret',
        'verbose': False,
        }
    fileName = '.'.join(('-'.join((ciscoDevice.get('ip'),timeString)), 'txt'))
    if os.path.exists(ciscoNexusDir + fileName):
        continue
    else:
        netConn = ConnectHandler(**ciscoDevice)
        with open(ciscoNexusDir + fileName,'w', encoding = "utf-8") as f:
            for line in ciscoCommand:    
                output = netConn.send_command(line)
                f.write(line + '\n' + output)
        print(f'{fileName} success!')
    netConn.disconnect()
