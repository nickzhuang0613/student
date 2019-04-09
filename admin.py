# -*- coding:utf-8 -*-
from namespace import user
import os
import sys
from de_en_code import *

config_dir = sys.path[0]+"\\config\\"
config_file = "config.ini"
config_file_name = config_dir + config_file

def add_admin(): #添加管理员
    with open(config_file_name,'a',encoding='utf-8') as f:
        name=(input("请输入用户名："))
        while True:
            if name in user:
                name = input("用户已经存在，请重新输入：")
            else:
                break
        passwd = input("请输入密码：")
        while True:
            if 'non_compliant_agreement_eof' == en_code(passwd): #密码有效性检查
                passwd = input("密码不符合加密协议，请重新输入:")
            else:
                break
        while True:
            if passwd == input("请再次输入密码："):
                break
            else:
                passwd = input("密码不一致，请重新设置：")
        passwd = en_code(passwd) #密码存档
        f.write(name+':'+passwd+'\n')
        user[name]=passwd
        print("添加成功")
        
def del_admin(): #删除管理员
    while True:
        if not user: #判断是否非空
            print("目前暂时没有用户")
            break
        del_user = input("请输入需要删除的用户：")
        if del_user not in user:  #判断输入是否存在
            print("输入用户"+del_user+"不存在")
        else:
            info = ''
            for key in user: #删除指定行
                if key != del_user:
                    info += (key + ':' + user[key] + '\n')
            f = open(config_file_name,'w',encoding='utf-8')
            f.write(info)
            f.close()
            del user[del_user] #更新已经导入的用户信息表
            print("删除成功")
        sele = input("是否继续删除用户信息y/n:")
        if 'y' ==  sele or 'Y' == sele or '' == sele:
            continue
        else:
            break;

def modify_admin(): #删除管理员
    while True:
        if not user: #判断是否非空
            print("目前暂时没有用户")
            break
        modify_user = input("请输入需要修改的用户：")
        if modify_user not in user:  #判断输入是否存在
            print("输入用户"+modify_user+"不存在")
        else:
            passwd=input('请输入新的密码:')
            while True:
                if 'non_compliant_agreement_eof' == en_code(passwd): #密码有效性检查
                    passwd = input("密码不符合加密协议，请重新输入:")
                else:
                    break
            while True:
                if passwd == input("请再次输入密码："):
                    break
                else:
                    passwd = input("密码不一致，请重新设置：")
            info = ''
            for key in user: 
                if key != modify_user:
                    info += (key + ':' + user[key] + '\n')
            passwd = en_code(passwd) #密码存档
            info+=(modify_user+':'+passwd+'\n')
            user[modify_user] = passwd
            f = open(config_file_name,'w',encoding='utf-8')
            f.write(info)
            f.close()
            print("修改成功")
        sele = input("是否继续修改其他用户信息y/n:")
        if 'y' ==  sele or 'Y' == sele or '' == sele:
            continue
        else:
            break;

def get_admin_info():
    if os.path.isfile(config_file_name) == 0: #判断文件是否存在
        f = open(config_file_name,'w+',encoding='utf-8') #创建文件，兼容性较好的方案
        f.close()
    if os.path.getsize(config_file_name) == 0: #判断文件是否非空
        print("使用学生信息管理系统之前,请画几分钟根据提示完成必要的初始化")
        while True:
            add_admin()
            sele = input("是否继续录入管理员信息y/n:")
            if 'y' ==  sele or 'Y' == sele or '' == sele:
                continue
            else:
                break;
    for info in open(config_file_name,encoding='utf-8'):
        l = info.split(":")
        user[''.join(l[0])] = (''.join(l[1])).rstrip('\n')  #去掉换行


def show_admin():
    if not user:
        print("暂时没有添加任何用户。")
        return
    print('账号','\t','--->\t','密码')
    for key in user:
        print(key,'\t','--->\t',de_code(user[key]))
        
def log_in():
    get_admin_info()
    while True:
        name = str(input("账户："))
        if name not in user:
            print("没有用户:[",name,"],请重新输入")
            continue
        else:
            passwd = str(input("请输入密码："))
            if passwd != de_code(user[name]):
                print("密码错误，请重新输入。")
                continue
            else:
                print("欢迎使用学生信息管理系统。")
                break