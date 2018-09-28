#!/usr/bin/env python
#coding:utf-8
'''
此模块作用为连接设备，对设备进行一系列巡检命令操作的模块
'''
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import logging, json
#设置日志格式及保存日志的文件，在日志中，记录所有设备巡检失败的信息
logging.basicConfig(filename=r'./logfiles/failconn.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connDevice(IP, flag, fileName, failedCount, newFileCount):
    '''
    此函数用于被调用，作用是连接网络设备，发送巡检命令，把巡检结果保存为文件
    :param IP: 设备IP，类型：str。
    :param flag: 设备类型， 类型：str。
    :param fileName: 保存设备巡检结果的文件名，类型：str。
    :param failedCount: 统计设备巡检失败的数量，初始为0, 类型：int。
    :param newFileCount: 统计新增设备巡检成功的数量，初始为0, 类型：int。
    :return: failedCount和newFileCount
    '''
    device_type = 'cisco_nxos'  #将设备类型默认设置为Nexus类型
    Command = 'show run'  #将巡检命令默认设置为“show run”
    delays = 2   #默认将每一个命令的延迟设置为2秒
    loops = 1000 #默认对每一个要巡检的设备进行1000次循环
    '''
    判断flag标志类型，以对相应类型的设备进行巡检
    '''
    if 'nexus' == flag.lower():
        device_type = 'cisco_nxos'  #设置要连接巡检的设备类型
        #获取相应类型的巡检命令，以json格式导入，并赋值给Command变量，类型为：dict
        with open(r'./conf_files/NexusCommand.txt', 'r') as f:
            Command = json.load(f)
    elif 'ios' == flag.lower():
        device_type = 'cisco_ios'  #设置要连接巡检的设备类型
        #获取相应类型的巡检命令，以json格式导入，并赋值给Command变量，类型为：dict
        with open(r'./conf_files/IosCommand.txt', 'r') as f:
            Command = json.load(f)
    elif 'huawei'  == flag.lower():
        device_type = 'huawei'  #设置要连接巡检的设备类型
        #获取相应类型的巡检命令，以json格式导入，并赋值给Command变量，类型为：dict
        with open(r'./conf_files/HuaweiCommand.txt', 'r') as f:
           Command = json.load(f)
    #设置要连接设备的详细参数：
    Device = {
        'device_type': device_type,  #设备类型
        'ip': IP,                    #设备IP
        'username': 'zybank15',      #用户名
        'password': 'Zbnet!1126',    #密码
        'port': 22,                  #端口
        'secret': 'Zbtec@1126',      #特权密码
        'verbose': False,            #是否显示连接设备的详细信息
        }
    try:
        #连接设备
        netConn = ConnectHandler(**Device)
    except (EOFError, NetMikoTimeoutException):
        #当连接设备超时时，进行日志记录，failedCount加1
        logging.error(f'The {flag} device {IP} is connect failed!')
        failedCount += 1
    except (EOFError, NetMikoAuthenticationException):
        #当登录设备认证失败时，进行日志记录，failedCount加1
        logging.error(f'The {flag} device {IP} is authentication failed!')
        failedCount += 1
    except (ValueError, NetMikoAuthenticationException):
        # 当进入特权模式认证失败时，进行日志记录，failedCount加1
        logging.error(f"The {flag} device {IP}'s enable password is failed!")
        failedCount += 1
    except Exception as e:
        #发生其它错误时，进行日志记录，failedCount加1
        logging.error(f"The {flag} device {IP} is error: {Exception}----{e}")
        failedCount += 1

    #当连接并登录成功时，进行巡检操作
    else:
        if flag.lower() == 'ios':  #判断设备类型为IOS设备时，进入特权模式
            netConn.enable()

        #以写模式，打开保存巡检结果的文件，编码为：utf8
        with open(fileName,'w', encoding = "utf-8") as f:

            #遍历命令列表，对已经连接登录成功的设备进行巡检操作
            for line in Command:
                #发送相应的巡检命令，结果赋值给output变量
                output = netConn.send_command(line, max_loops=loops, delay_factor=delays)
                #将巡检结果写入文件，格式：先把已经操作的巡检命令写入，再把命令的结果写入
                f.write('\n' + line + '\n' + output)
            #在巡检结果最后，写入一行‘-’，表示巡检结束
            f.write('\n' + '-' * 100)
        #打印每个巡检成功的设备及已经写入成功的文件
        print(f'{fileName} success!')
        #巡检成功时，newFileCount加1
        newFileCount += 1
        #每当一个设备巡检成功并结束时，就断开与该设备的连接
        netConn.disconnect()

    #返回failedCount和newFileCount的计数, 类型：int
    return failedCount, newFileCount
