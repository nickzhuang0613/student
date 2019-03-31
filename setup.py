# -*- coding:utf-8 -*-
import admin
from namespace import *

def test():
    admin.show_admin()
    admin.add_admin()
    admin.show_admin()
    admin.del_admin()
    admin.show_admin()
    
if __name__ == "__main__":
    admin.log_in()
