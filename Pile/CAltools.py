# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import xlrd
import math


class Tools(object):
    def __init__(self):
        pass

    # 插值计算  arrX：匹配列  arrY：目标值列 insertV：插入值
    def GetInsrtValue(self,arrX:list,arrY:list,insertV:float)->float:
        f=interpolate.interp1d(arrX,arrY,kind="slinear")
        ynew=f(insertV)
        return ynew
    
    # 读取excel表工作簿1的第icol列。去掉第一个元素
    def GetValueFromXls(self,filepath,icol)->list:
        print(filepath)
        workbook = xlrd.open_workbook(filepath)
        sheet= workbook.sheet_by_index(0)
        cols = sheet.col_values(icol) 
        cols.pop(0)
        return cols
    
    def pp(self,f):
        print(f)
        f.write( "www.runoob.com!\nVery good site!\n")
        return 
    
    # 计算配筋率 d钢筋直径 n钢筋根数 D桩直径
    def Getphg(self,d,n,D):
        As=math.pi*pow(d,2)/4*n
        A=math.pi*pow(D,2)/4
        pg=As/A
        msg="当前桩配筋面积：%s mm^2;\n桩截面积：%s mm^2;\n配筋率：%s"%(As,A,pg)
        res={"AS":As,"A":A,"pg":pg,"msg":msg}
        return res

    #获取混凝土参数
    def GetHnt(self,cHntCleavel):
        Hnt={
            'C15':{'E':2.20*1e4},
            'C20':{'E':2.55*1e4},
            'C25':{'E':2.80*1e4},
            'C30':{'E':3.00*1e4},
            'C35':{'E':3.15*1e4},
            'C40':{'E':3.25*1e4},
            'C45':{'E':3.35*1e4},
            'C50':{'E':3.45*1e4},
            'C55':{'E':3.55*1e4},
            'C60':{'E':3.60*1e4},
            'C65':{'E':3.65*1e4},
            'C70':{'E':3.70*1e4},
            'C75':{'E':3.75*1e4},
            'C80':{'E':3.80*1e4},
        }  
        return Hnt[cHntCleavel]
    
    #获取钢筋参数
    def GetGj(self,cGjleavel):
        Gj={
            'HPB300':{'E':2.10*1e5},
            'HRB335':{'E':2.00*1e5},
            'HRB400':{'E':2.00*1e5},
            'HRBF400':{'E':2.00*1e5},
            'RRB400':{'E':2.00*1e5},
            'HRB500':{'E':2.00*1e5},
            'HRBF500':{'E':2.00*1e5},
        }
        return Gj[cGjleavel]
        
    # 桩身截面受拉的截面模量
    def GetW0(self,d,ae,phg,d0):
        W0=math.pi*d*(d*d+2*(ae-1)*phg*d0*d0)/32
        return W0



def main():
    tools=Tools()
    tools.GetValueFromXls('E:\\pp.xls',0)
    f=open("E:\\foo.txt", "w")
    tools.pp(f)
    f.close()

if __name__ == "__main__":
    main()
