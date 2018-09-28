#!/usr/bin/env python
#coding:utf-8
'''
自动化巡检网络设备，把获取到每个设备的巡检结果保存为以“IP-日期”为名称的文件
'''

import datetime, json, os, time, sys
'''
导入操作设备的模块:connDevice.py
'''
import connDevice, analyseMain

timeString = datetime.datetime.now().strftime('%Y-%m-%d')  #设置当前日期以年-月-日格式的字符串
flag = ''  #设置设备类型标志
baseDir = 'device'  #设置放置巡检结果文件的基础文件夹

def conn(deviceDir, ipList, flag):
    '''
    此函数用于调用connDevice.connDeivce()方法，操作目标网络设备。
    :deviceDir:不同设备类型的目录字符串，如（device/Nexus）。
    :ipList: IP地址列表
    :flag: 设备类型标志，如：nexus
    :return: None
    '''
    startTime = time.time() #设置设备巡检的开始时间
    existsFileCount = 0  #设置巡检文件已经存在的数量
    failedCount = 0  #设置巡检失败的数量
    newFileCount = 0  #设置新增巡检成功的数量
    for lineIP in ipList:  #遍历传进来的IP列表
        #设置保存设备巡检结果的文件名，格式：IP-日期.txt
        fileName = os.path.join(deviceDir, '.'.join(('-'.join((lineIP,timeString)), 'txt')))
        if os.path.exists(fileName): #判断文件是否存在，如果存在进行下一个IP的巡检，existsFileCount + 1
            existsFileCount += 1
            continue
        '''
        调用connDevice.connDevice()函数，传入的参数为：
        ｜lineIP：ipList列表中的每一个ip，类型：str。
        ｜flag：设备类型，类型：str。
        ｜fileName：保存设备巡检结果的文件名，格式：IP-日期.txt，类型：str。
        ｜failedCount：巡检失败计数参数，类型：int，初始值为：0
        ｜newFileCount：巡检成功计数参数，类型：int，初始值为:0
        ------------------------------------------------------------
        函数返回值：
        ｜failedCount：巡检失败计数参数，类型：int。
        ｜newFileCount：巡检成功计数参数，类型：int。        
        '''
        failedCount, newFileCount = connDevice.connDevice(lineIP, flag, fileName, failedCount, newFileCount)

    endTime = time.time()  #设置巡检结束时间
    delta = endTime - startTime  #计算巡检某一类设备所需要的总时间

    #打印巡检结果记录
    print('-' * 100)
    print(f'{flag} total used time {datetime.timedelta(seconds=delta)}')
    print(f'The {flag} device total count is: {len(ipList)}, exists file count is:{existsFileCount}, '
          f'New file count is {newFileCount}')
    print(f'The {flag} failed connection is {failedCount}')
    print('*' * 100)
    analyseMain.main(flag, timeString, baseDir)

def Nexus():
    '''
    处理巡检Nexus设置的具体参数信息。调用conn()方法，对Nexus设备进行巡检
    :return:None
    '''
    flag = 'Nexus'  #将标志位设置为Nexus

    #将Nexus设备IP以json格式导入，并赋值给nexusIP变量，类型：字典型
    with open(r'./conf_files/ciscoNexusIP.txt', 'r') as f:
      nexusIP = json.load(f)

    #设置放置Nexus设备巡检结果文件的文件夹：
    #baseDir: "device".
    #flag: "Nexus".
    #timeString: "当前日期，格式为：年-月-日".
    NexusDir = os.path.join(baseDir, flag, timeString)

    #判断文件夹是否存在，如果不存在就新建文件夹
    if not os.path.exists(NexusDir):
        os.makedirs(NexusDir)

    #获取字典nexusIP的值，并对其排序，赋值给变量ipList，类型为：列表。
    ipList = sorted(nexusIP.values())

    #调用conn()方法，传入处理过的参数：
    #NexusDir：放置Nexus设备巡检文件的目录，类型：str。
    #ipList：Nexus设备IP列表，类型：list
    #flag：Nexus设备标志，类型：str
    conn(NexusDir, ipList, flag)


def Ios():
    flag = 'IOS' #将标志位设置为IOS

    # 将IOS设备IP以json格式导入，并赋值给IosIP变量，类型：字典型
    with open(r'./conf_files/ciscoIosIP.txt', 'r') as f:
      IosIP = json.load(f)

    # 设置放置IOS设备巡检结果文件的文件夹：
    # baseDir: "device".
    # flag: "IOS".
    # timeString: "当前日期，格式为：年-月-日".
    IosDir = os.path.join(baseDir, flag, timeString)

    # 判断文件夹是否存在，如果不存在就新建文件夹
    if not os.path.exists(IosDir):
        os.makedirs(IosDir)

    # 获取字典IosIP的值，并对其排序，赋值给变量ipList，类型为：列表。
    ipList = sorted(IosIP.values())

    # 调用conn()方法，传入处理过的参数：
    # IosDir：放置IOS设备巡检文件的目录，类型：str。
    # ipList：IOS设备IP列表，类型：list
    # flag：IOS设备标志，类型：str
    conn(IosDir, ipList, flag)


def huawei():
    flag = 'Huawei'  #将标志位设置为IOS

    # 将Huawei设备IP以json格式导入，并赋值给HuaweiIP变量，类型：字典型
    with open(r'./conf_files/HuaweiIP.txt', 'r') as f:
      HuaweiIP = json.load(f)

    # 设置放置Huawei设备巡检结果文件的文件夹：
    # baseDir: "device".
    # flag: "Huawei".
    # timeString: "当前日期，格式为：年-月-日".
    HuaweiDir = os.path.join(baseDir, flag, timeString)

    # 判断文件夹是否存在，如果不存在就新建文件夹
    if not os.path.exists(HuaweiDir):
        os.makedirs(HuaweiDir)

    # 获取字典HuaweiIP的值，并对其排序，赋值给变量ipList，类型为：列表。
    ipList = sorted(HuaweiIP.values())

    # 调用conn()方法，传入处理过的参数：
    # HuaweiDir：放置Huawei设备巡检文件的目录，类型：str。
    # ipList：Huawei设备IP列表，类型：list
    # flag：Huawei设备标志，类型：str
    conn(HuaweiDir, ipList, flag)

if __name__== '__main__':

    startTime = time.time()  #设置程序开始日间
    Nexus()  #调用Nexus()方法，对Nexus设备进行巡检，无返回值
    Ios()    #调用Ios()方法，对IOS设备进行巡检，无返回值
    huawei() #调用huawei()方法，对Huawei设备进行巡检，无返回值
    endTime = time.time()  #设置程序结束时间
    delta = endTime - startTime  #计算程序整体运行时间
    print('*' * 100)
    analyseMain.main('Nexus')
    analyseMain.main('IOS')
    analyseMain.main('Huawei')
    #以可读格式打印程序整体运行所需时间
    print(f'Total used time {datetime.timedelta(seconds=delta)}')

