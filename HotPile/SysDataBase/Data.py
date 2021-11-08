# -*- coding: utf-8 -*-
import sys
import os
import sqlite3



def app_path():
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        # print("sfsfs",os.path.dirname(sys.executable))
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)  

    # 连接数据库
def connetDB(str):
    path=app_path()+"\\"+str
    con = sqlite3.connect(path)
    return con
    
    # 返回游标
def getcur(con):
    cur = con.cursor()
    return cur


#查询所有语句
def GetAll(cur,tablename):
    # sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
    # cur.execute(sql)
    sql="select * from "+tablename
    cur.execute(sql)
    return cur.fetchall()

#关闭游标
def closecur(cur):
    cur.close();

#关闭数据库连接
def closeconnet(con):
    con.close();

