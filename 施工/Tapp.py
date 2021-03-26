# -*- coding: utf-8 -*-
# author:tce
import sqlite3

# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
# c = conn.cursor()
# c.execute('''CREATE TABLE Msg
#        (ID  integer PRIMARY KEY autoincrement,
#        ctitle          varchar(64),
#        cmsg             blob default '',
#        cmake        varchar(128));''')
# print("Table created successfully")
# c.execute("INSERT INTO Msg (ID,ctitle,cmake) VALUES (1, 'Paul', 'California')")
# conn.commit()
# conn.close()
def CreatTable():
       conn = sqlite3.connect('test.db')
       c = conn.cursor()
       c.execute('''CREATE TABLE Msg
       (ID  integer PRIMARY KEY autoincrement,
       ctitle          varchar(64),
       cmsg             blob default '',
       cmake        varchar(128));''')
       conn.commit()
       conn.close()


def SaveData(ctitle,cmake):
       conn = sqlite3.connect('test.db')
       c = conn.cursor()
       c.execute("INSERT INTO Msg (ctitle,cmsg,cmake) VALUES (?,'sfdsfdsfsdfsfdsfsf', ?)",(ctitle,cmake))
       conn.commit()
       conn.close()
def GetData():
       conn = sqlite3.connect('test.db')
       c = conn.cursor()
       cursor = c.execute("SELECT id, ctitle, cmsg, cmake  from Msg")
       for row in cursor:
              print("ID=",row[0])
              print("ctitle=",row[1])
              print("cmsg=",row[2])
              print("cmake=",row[3])
       conn.close()
