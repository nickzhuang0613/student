# -*- coding:utf-8 -*-
import admin
import student
import tkinter

def op(cmd:int):
    if 1 == cmd:
        student.student_data_show()
    elif 2 == cmd:
        name=input("请输入查询姓名：")
        student.student_data_show(name)
    elif 3 == cmd:
        student.student_data_add()
    elif 4 == cmd:
        student.student_data_del()
    elif 5 == cmd:
        student.student_data_modify()
    elif 6 == cmd:
        admin.add_admin()
    elif 7 == cmd:
        admin.del_admin()
    elif 8 == cmd:
        admin.modify_admin()
    elif 9 == cmd:
        admin.show_admin()
    else:
        print("输入错误")
        
def menu():
    while True:
        print('1:全部学生信息查看')
        print('2:学生信息查看')
        print('3:添加学生信息')
        print('4:删除学生信息')
        print('5:修改学生信息')
        print('6:添加管理员')
        print('7:删除管理员')
        print('8:修改管理员信息')
        print('9:显示管理员信息')
        print('10:退出')
        sel=int(input("请选择"))
        if sel == 10:
            break
        op(sel)

if __name__ == "__main__":
    admin.log_in()
    student.student_data_init()
    menu()
    root=tkinter.Tk()
    tkinter.Message(root,text='欢迎下次使用',aspect = 400).pack()
    root.mainloop()