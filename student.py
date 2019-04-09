# -*- coding:utf-8 -*-
import os
import sys
from namespace import students
import tkinter

student_data_dir = sys.path[0]+"\\student\\"
student_data = "data.md"
student_data_name = student_data_dir + student_data

def student_data_init():
    if os.path.isfile(student_data_name) == 0: #判断文件是否存在
        f = open(student_data_name,'w+',encoding='utf-8') #创建文件，兼容性较好的方案
        f.close()
    if os.path.getsize(student_data_name) == 0: #判断文件是否非空
        root=tkinter.Tk()
        tkinter.Message(root,text='暂时没有学生信息',aspect = 400).pack()
        root.mainloop()
    else:
        for info in open(student_data_name,encoding='utf-8'):
            data_list=info.rstrip('\n').split(':')
            students[data_list[0]]=data_list[1:3]
            students[data_list[0]].append(data_list[3:])

def student_data_add():
    with open(student_data_name,'a',encoding='utf-8') as f:
        while True:
            name=input("学生名：")
            if name in students:
                sel=input("学生已经存在,按任意键继续")
                continue
            sex=input("性别：")
            age=input("年龄：")
            src_ch=input("语文成绩：")
            math_src=input("数学成绩：")
            en_src=input("英语成绩")
            s=name+':'+sex+':'+age+':'+src_ch+':'+math_src+':'+en_src+'\n'
            f.write(s)
            students[name]=s
            sele=input('是否继续录入n/[y]:')
            if 'y' ==  sele or 'Y' == sele or '' == sele:
               continue
            else:
               break;

def student_data_show(name='NULL'):
    if name == 'NULL':
        print('姓名\t性别\t年龄\t语文\t数学\t英语\n')
        for key in students:
            print(key,"\t",students[key][0],"\t",students[key][1],"\t",students[key][2][0],"\t",students[key][2][1],"\t",students[key][2][2])
    else:
        if name not in students:
            print("不存在",name,"的相关信息")
        else:
            print('姓名\t性别\t年龄\t语文\t数学\t英语\n')
            key=name
            print(key,"\t",students[key][0],"\t",students[key][1],"\t",students[key][2][0],"\t",students[key][2][1],"\t",students[key][2][2])

def student_data_del():
    while True:
        if not students: 
            print("目前暂时没有学生")
            break
        del_student = input("请输入需要删除的学生：")
        if del_student not in students:  #判断输入是否存在
            print("输入学生"+del_student+"不存在")
        else:
            info=''
            f = open(student_data_name,'w',encoding='utf-8')
            for key in students: #删除指定行
                if key != del_student:
                    info +=''.join((key+":"+students[key][0]+":",students[key][1]+":",students[key][2][0]+":",students[key][2][1]+":",students[key][2][2] +"\n"))
            f.write(info)
            f.close()
            del students[del_student] #更新已经导入的用户信息表
            print("删除成功")
        sele = input("是否继续删除学生信息y/n:")
        if 'y' ==  sele or 'Y' == sele or '' == sele:
            continue
        else:
            break;
        
def student_data_modify():
    while True:
        if not students: 
            print("目前暂时没有学生")
            break
        modify_student = input("请输入需要修改的学生：")
        if modify_student not in modify_student:  #判断输入是否存在
            print("输入学生"+del_student+"不存在")
        else:
            info=''
            f = open(student_data_name,'w',encoding='utf-8')
            for key in students: #删除指定行
                if key != modify_student:
                    info +=''.join((key+":"+students[key][0]+":",students[key][1]+":",students[key][2][0]+":",students[key][2][1]+":",students[key][2][2] +"\n"))
           
            sex=input("性别：")
            age=input("年龄：")
            src_ch=input("语文成绩：")
            math_src=input("数学成绩：")
            en_src=input("英语成绩")
            s=modify_student+':'+sex+':'+age+':'+src_ch+':'+math_src+':'+en_src+'\n'
            info+=s
            
            f.write(info)
            f.close()
    
            data_list=s.rstrip('\n').split(':')
            students[data_list[0]]=data_list[1:3]
            students[data_list[0]].append(data_list[3:])
            
            print("修改成功")
        sele = input("是否继续修改学生信息y/n:")
        if 'y' ==  sele or 'Y' == sele or '' == sele:
            continue
        else:
            break;