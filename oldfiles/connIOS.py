#!/usr/bin/env python
#coding:utf-8

from netmiko import ConnectHandler
import datetime, json, os

timeString = datetime.datetime.now().strftime('%Y-%m-%d')

with open('ciscoIosIP.txt', 'r') as f:
  ciscoIP = json.load(f)
with open('IosCommand.txt', 'r') as f:
  ciscoCommand = json.load(f)

ciscoIosDir = 'cisco_device/IOS/' + timeString + '/'

if not os.path.exists(ciscoIosDir):
    os.mkdir(ciscoIosDir)

for lineIP in ciscoIP.values():
    ciscoDevice = {
        'device_type': 'cisco_ios',
        'ip': lineIP,
        'username': 'zybank15',
        'password': 'Zbnet!1126',
        'port': 22,
        'secret': 'secret',
        'verbose': False,
        }

    netConn = ConnectHandler(**ciscoDevice)
    fileName = '.'.join(('-'.join((ciscoDevice.get('ip'),timeString)), 'txt'))
    with open(ciscoIosDir + fileName,'w', encoding = "utf-8") as f:
        for line in ciscoCommand:    
            output = netConn.send_command(line)
            f.write(output)
    print(f'{fileName} success!')
    netConn.disconnect()
