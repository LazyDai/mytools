#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""A Effective Tools by Dzy"""

# 版本说明：2021.02.20 增加init_chdir,2020.10.05 增加ip格式判断功能,2020.10.01 修改为PEP8风格；2019.06.05,增加myNowTime
# 功能说明：基于python3此py为自定义的工具集，可以实现自己想要的功能，可以被import
# 备注说明：部分功能可以在linux下运行
# 环境要求：windows系统
# 设备要求：无

import os
import sys
import time
import datetime
import threading
import subprocess
import platform
import random
import json
import shutil


# 自定义的Print功能，可以输出格式化时间和内容
def myPrint(string):
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(time.time()))+" "
    print(nowTime, string)


# 自定义的Print功能，
def myPrint2(var, all_var=locals()):
    """打印变量名和变量值,暂时不能被引用，请直接复制使用

    Args:
        var (any): 任何变量均可以
        all_var (any, optional): 所有变量. Defaults to locals().
    """
    varName = [var_name for var_name in all_var if all_var[var_name] is var][0]

    nowTime = time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(time.time()))+" "
    print(nowTime, varName, '=', var)


# 获取当前的时间,可以自定义时间格式
def myNowTime(time_format='%Y-%m-%d %H:%M:%S'):
    '''
    输出当前时间，可以自定义时间格式
    '''
    return time.strftime(time_format, time.localtime(time.time()))
    # return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


# 复制文件
def myCopyFile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath = os.path.dirname(srcfile)  # 获取文件路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 没有就创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件到默认路径
        print("copy %s -> %s" % (srcfile, os.path.join(fpath, dstfile)))


# 获取当前的时间,可以自定义时间格式
def getNowTime(time_format='%Y-%m-%d %H:%M:%S') -> str:  # 输出当前时间，可以自定义时间格式
    return time.strftime(time_format, time.localtime(time.time()))
    # return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def getNowTimestamp(digits=13) -> str:
    """获取当前时间戳, 返回为指定位数的字符串时间戳

    Args:
        digits (int, optional): 定义要几位数的时间戳. Defaults to 13.

    Returns:
        str: 返回字符串
    """
    time_stamp = time.time()
    digits = 10 ** (digits - 10)
    time_stamp = int(round(time_stamp*digits))
    return str(time_stamp)


# 判断当前时间字符串是否是今天,
def is_Today(timestr='2019-11-27 11:35:00'):
    # demostr='2019-11-27 11:35:00'
    stru = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')
    # print(stru,type(stru),dir(stru))
    if (datetime.datetime.now()-stru).days == 0:
        print("经过判断 '%s' 是今天" % timestr)
        return True
    else:
        print("'%s' 不是当天" % timestr)
        return False
    pass


# 计算时间差,还不能用
def timedifferent():
    print('系统自动进入监听模式')
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    end = datetime.datetime.now()
    interval = (end-start).seconds
    return interval


# 自定义的log功能，可以格式化输出时间及内容并写入文件
def myLog(filename, string):
    strTime = time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(time.time()))+" "
    with open(filename, 'a+', encoding='utf-8') as f:
        f.write(strTime+' '+string+"\n")


# 用于蜂鸣器哔哔提示
def beep():
    try:
        import ctypes  # 用于哔哔
        if sys.platform == "win32" or sys.platform == "win64":
            player = ctypes.windll.kernel32
            player.Beep(1000, 200)
    except Exception as e:
        print("import ctypes Error!")
        print(e)
    else:
        pass
    finally:
        pass


# 判断word是否符合ip格式
def is_ipaddr(ipAddr):
    """
    判断word是否符合ip格式,比如"192.168.1.1"
    返回值为:True/False
    """
    import re
    check_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if check_ip.match(ipAddr):
        return True
    else:
        return False


# 判断word是否中文
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True  # 是中文就True
    return False


def get_current_OS():
    """判断当前作业环境的操作系统名字,一般linux结果为linux*，windows为win32/64
    platform.platform() #获取操作系统名称及版本号，'Windows-7-6.1.7601-SP1'
    platform.version() #获取操作系统版本号，'6.1.7601'
    platform.architecture() #获取操作系统的位数，('32bit', 'WindowsPE')
    platform.machine() #计算机类型，'x86'
    platform.node() #计算机的网络名称，'hongjie-PC'
    platform.processor() #计算机处理器信息，'x86 Family 16 Model 6 Stepping 3, AuthenticAMD'
    platform.uname() #包含上面所有的信息汇总，uname_result(system='Windows', node='hongjie-PC',
    release='7', version='6.1.7601', machine='x86', processor='x86 Family
    16 Model 6 Stepping 3, AuthenticAMD')
    还可以获得计算机中python的一些信息：
    platform.python_build()
    platform.python_compiler()
    platform.python_branch()
    platform.python_implementation()
    platform.python_revision()
    platform.python_version()
    platform.python_version_tuple()
    """
    currentOS = platform.platform()
    cpubit = platform.architecture()
    cpubit = platform.node()
    print("Current OS: %s, devicesName:%s" % (currentOS, cpubit))
    return currentOS  # 返回类型为str


def get_cpubit():
    currentOS = platform.platform()
    cpubit = platform.architecture()
    print("Current OS: %s, cpubit:%s" % (currentOS, cpubit))
    return cpubit  # 返回类型为str


# 自定义的threading工具
def myThread(funtion, postargs):
    """封装多线程threading.Thread

    Args:
        funtion (函数名): 函数名
        postargs ([type]): 参数, 记得最后要一个逗号, 比如(,)

    Returns:
        [thread]: 返回线程对象
    """
    t = threading.Thread(target=funtion, args=(postargs))
    t.setDaemon(True)  # 调用b.setDaemaon(True),则主线程结束时，会把子线程B也杀死。
    t.start()
    myPrint(t)
    return t


# 获取本机第一个网卡的mac地址
def get_mac_address(ip='local'):
    # 根据系统不同使用不同的命令
    envOS = get_current_OS()
    print('获取到的系统名称为', envOS)
    if ip == "local":
        if 'Windows-10' in envOS:
            print('当前系统为win10系统,采用win10风格g命令')
            result = os.popen("getmac |findstr Device").read()
            result = result.split('   ')[0]
            print("本地mac地址为:", result)
            return result
        elif 'debian' in envOS:
            # 树莓派的envOS
            print('当前系统为树莓派系统,暂无Linux风格命令')
    else:
        if 'Windows-10' in envOS:
            print('当前系统为win10系统,采用win10风格命令')
            # result = os.popen("arp -a |findstr %s |findstr 动态 " % ip).read()
            # arp -a |findstr  "[a-f0-9][a-f0-9][-:]" |findstr /c:".1 "
            result = os.popen(
                'arp -a |findstr "[a-f0-9][a-f0-9][-:]" |findstr /c:"%s " ' % ip).read()
            print('result popen', result)
            if result is None or result == '':
                print("获取结果为空,没有获取%s到对应的mac地址" % ip)
                return False
            print(result.split('\n'))
            result = result.split('%s ' % ip)[1][-33:-15]
            print("%s 对应的mac地址为:" % ip, result)
            return result
        elif 'debian' in envOS:
            # 树莓派的envOS
            print('当前系统为树莓派系统,采用Linux风格命令')
            # arp -a |egrep -i [A-F0-9]{2}[-:] |grep 192.168.58.103\)
            result = os.popen("arp -a |egrep -i [A-F0-9]{2}[-:] |grep %s\)  " % ip).read()
            print('result1=', result)
            if result is None or result == '':
                print("获取结果为空,没有获取%s到对应的mac地址" % ip)
                return False
            else:
                # print('result', result)
                result = result.split('at ')[1][:17]
                print("%s 对应的mac地址为:" % ip, result)
                return result
        return False


# 用于装逼用,启动多个cmd窗口进行运行多个脚本
def colorcmd(color, title, python_file):
    os.system("start  cmd.exe @cmd /k \"color %s&&title %s &&python %s\"" %
              (color, title, python_file))
    pass


# 获取本机本地ip
def get_local_ip():
    try:
        import socket
        # 获取本机电脑名
        myPCname = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        myipaddr = socket.gethostbyname(myPCname)
        print("本机电脑名：%s" % myPCname)
        print("本地IP：%s" % myipaddr)
    except Exception as e:
        myPrint("出现异常，没有通过socket获取到ip")
        print(e)
        print("自动通过ipconfig智能获取ip")
        # 用于智能获取ip，当socket无法使用的时候
        myipaddr = os.popen("ipconfig |findstr IPv4").read().split(": ")[
            1].strip()
        # pingIP("%s.%s.%s"%(ipv4.split(".")[0],ipv4.split(".")[1],ipv4.split(".")[2]),1,255)
    else:
        pass
        # # 可以通过socket正常获取到ip
        # pingIP("%s.%s.%s"%(myipaddr.split(".")[0],myipaddr.split(".")[1],myipaddr.split(".")[2]),1,255)
    finally:
        print("获取本机ip结束,返回ip地址")
        return myipaddr


# 在win10中测试可以用
def pingdevice(ip):
    """pingdevice使用说明:
    ping单个设备单次,判断是否ping通,参数为ip地址,例:192.168.1.101
    返回值: ping通则返回True,ping不通返回值为False,
    在win10家庭版中测试通过
    """
    # 备注:不同的操作系统ping命令格式不一样
    envOS = get_current_OS()
    print('获取到的系统名称为', envOS)
    if 'Windows-10' in envOS:
        print('当前系统为win10系统,采用win10风格ping命令')
        cmd = 'ping -n 1 %s '
        normal = '(0% 丢失)'
        normal2 = '无法访问目标主机'
        child = subprocess.Popen(cmd % ip, shell=False, stdout=subprocess.PIPE)
        childresult = child.stdout.read()
        result = childresult.decode("gbk")
        # print(result)
        if normal in result and normal2 not in result:
            print(ip, '发现【%s】 ping正常' % normal)
            return True
        else:
            print(ip, '没有发现【%s】网络异常！！' % normal)
            return False
    elif 'debian' in envOS:
        # 树莓派的envOS
        print('当前系统为树莓派系统,采用Linux风格ping命令')
        cmd = 'ping -c 1 %s '
        keyword = '1 packets transmitted, 1 received'
        child = subprocess.Popen(cmd % ip, shell=True, stdout=subprocess.PIPE)
        childresult = child.stdout.read()
        result = childresult.decode("gbk")
        # print(result)
        if keyword in result:
            print(ip, '发现【%s】 ping正常' % keyword)
            return True
        else:
            print(ip, '没有发现【%s】, 网络异常！！' % keyword)
            return False
        pass
    else:
        print('没有获取系统版本,or没有对应的ping命令', envOS)
        return False


# 生成整型随机数，参数为定义随机数的范围
def suijishu(start=0, end=9):
    """
    生成整型的随机数，可以定义开始和结束值
    :param start:int
    :param end:int
    """
    return random.randint(start, end)


# 修改工作目录到py文件当前目录,init前缀为初始化过程
def init_chdir():
    print('获取当前工作目录路径', os.getcwd())  # 获取当前工作目录路径
    print("初始化工作目录,避免在CLI中出现相对路径的运行错误问题")
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    os.chdir(dirname)
    print("修改工作目录为", dirname)


# 2021.02.25 做一个基础类，提供classprint功能
class basicClass:
    # class attribute
    # className = 'mytools基类：'

    # instance attribute
    def __init__(self):
        self.instanceName = 'mytools基类：'  # 默认的实例名字,可以通过nickname进行修改
        self.debugSwitch = 1  # debug模式开关,1为进入,0为正常模式
        # print("from = %s 实例化中...." % self.instanceName)

    # 设置一个实例的名字
    def setNickname(self, instanceName):
        self.classPrint("%s 更名为 %s" % (self.instanceName, instanceName))
        self.instanceName = instanceName

    # 类的打印方法,用于区分是哪个实例打印的,当debugSwitch==1时候才会打印
    def classPrint(self, *strings):
        if self.instanceName and self.debugSwitch:
            print(self.instanceName, *strings)

    # 设置是否进入debug模式,如果进入debug模式就会有classPrint信息
    def debugMode(self, onoff):
        if onoff in [1, "1", "on"]:
            self.classPrint("Debug Mode is ON now!")
            self.debugSwitch = 1
        elif onoff in [0, "0", "off"]:
            self.classPrint("Debug Mode is OFF now!")
            self.debugSwitch = 0
        else:
            self.classPrint("Debug Mode agrv Error")


# 获取目录下所有文件,返回文件们列表
def get_file_path(root_path, file_list=[], dir_list=[]):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            get_file_path(dir_file_path, file_list, dir_list)
        else:
            file_list.append(dir_file_path)
    return file_list


# json的读取
def readJsonFile(jsonFile) -> dict:
    # 读取json文件
    print('读取json文件', jsonFile)
    with open(jsonFile, mode='r', encoding='utf-8') as readf:
        load_dict = json.load(readf)
        print(load_dict)
    return load_dict


# json的写入
def writeJsonFile(jsonFile, load_dict: dict):
    # 写入到json文件中,记得要ensure_ascii=False 这样才不会出现中文乱码
    print('写入json文件', jsonFile)
    with open(jsonFile, "w", encoding='utf-8') as f:
        json.dump(load_dict, f, indent=4, sort_keys=True, ensure_ascii=False)


def checkKeyWord(valueString: str, keywordList: list):  # 检查valueString中是否包含keywordList关键字们之一
    """ # 检查valueString中是否包含keywordList关键字们之一

    Args:
        valueString (str): 要被检查的字符串
        keywordList (list): 关键字列表

    Returns:
        [bool]: [description]
    """
    findCount = 0
    if not isinstance(valueString, str):
        # print('类型不对', type(valueString))
        return False
    for keyword in keywordList:
        if keyword in valueString:  # 看看valueString中是否有该关键字
            print(f'{__name__}:值【{valueString}】,包含关键字【{keyword}】')
            findCount += 1
        # else:
        #     print("\r", valueString, end="", flush=True)
    if findCount > 0:
        return True
    else:
        return False


def checkExtension(filePath: str, keywordList: list):  # 检查filePath中是否包含keywordList关键字们之一
    """ # 检查filePath中是否包含keywordList关键字们之一

    Args:
        filePath (str): 要被检查的字符串
        keywordList (list): 关键字列表

    Returns:
        [bool]: [description]
    """
    extName = os.path.splitext(filePath)[1]
    if not isinstance(filePath, str):
        # print('类型不对', type(filePath)/)
        return False
    if extName not in keywordList:
        # 如果扩展名不在列表中就false
        # print()
        return False
    print(f'{__name__}:值【{filePath}】,包含扩展名【{extName}】')
    return True


def findFilesPath(foldersDir, includeValue=['.xlsx'], excludeValue=['~$']) -> list:
    """搜索目录下的所有满足条件（扩展名）的文件的路径，返回路径们列表,固定不搜索~$临时文件

    Args:
        foldersDir (str): 要搜索的文件目录
        includeValue (list, optional): 搜索包含的关键字列表，关键字之间为或关系. Defaults to ['.xlsx'].
        excludeValue (list, optional): 搜索结果不包含的关键字列表. Defaults to [].

    Returns:
        list: 返回路径们列表
    """
    print(f'开始寻找扩展名包含{includeValue}, 但文件路径不包含{excludeValue}')
    fileList = []
    for root, dirs, files in os.walk(foldersDir):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for item in files:
            oldname = os.path.join(root, item)
            if os.path.isfile(oldname) and checkExtension(item, includeValue):  # 扩展名包括
                # print(oldname)
                if not checkKeyWord(item, excludeValue):  # 不包含那些
                    # print(len(fileList), oldname)
                    fileList.append(oldname)
                pass
    print(__name__, f'找到 {len(fileList)} 个满足{includeValue}条件的文件Path')
    return fileList


if __name__ == '__main__':
    # is_Today('2019-11-24 11:10:15')
    # beep()
    get_local_ip()
    # print(type(test))
    # pingdevice('192.168.31.147')
    # print(pingdevice.__doc__)
    # print(is_ipaddr('192.168.1.22'))
    beep()
    print(suijishu())
    print(myNowTime('%d%H%M%S'))
    Eric = basicClass()
    # Eric.name("E")
    Eric.debugMode(0)
    Eric.classPrint("go home")
