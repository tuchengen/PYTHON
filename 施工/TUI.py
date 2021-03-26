#-*- coding utf-8 _*_
#author: 涂成恩

import tkinter as tk
import Tapp

class From:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("词汇查询工具_v1.0")
        screenwidth = self.root.winfo_screenwidth() #屏幕宽度
        screenheight = self.root.winfo_screenheight() #屏幕高度
        width = 1200
        height= 900
        x= int((screenwidth - width) / 2)
        y= int((screenheight - height) / 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y)) #大小以及位置
        L1 = tk.Label(self.root, text="关键字")
        L1.pack()
        E1 = tk.Entry(self.root, bd =5)
        E1.pack()
        cv = tk.Canvas(self.root,bg = '#DDDDDD')
        self.oo="ada"
        cv.create_text(100, 50, text=self.oo)
        cv.pack()
        self.oo="dadada"
        self.root.mainloop()

if __name__=="__main__":
    form=From()
    Tapp.GetData()