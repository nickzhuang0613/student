# -*- coding:utf-8 -*-
import admin
import student
        
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
        sel=int(input("请选择"))
        if sel == 9:
            admin.show_admin()
        elif sel == 8:
            admin.modify_admin()
        
if __name__ == "__main__":
    admin.log_in()
    student.student_data_init()
    menu()