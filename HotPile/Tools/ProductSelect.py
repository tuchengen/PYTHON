# -*- coding: utf-8 -*-
import sys
from SysDataBase import Data

#从数据库获取产品信息
def GetProductInfo():
    con=Data.connetDB("sys.db")
    cur=Data.getcur(con)
    data=Data.GetAll(cur,"Product")
    Productlist=analysisData(data)
    Data.closecur(cur)
    Data.closeconnet(con)
    return Productlist

#情况数据库内容
def ClearTable(tablename):
    con=Data.connetDB("sys.db")
    cur=Data.getcur(con)
    sql="delete from "+tablename
    cur.execute(sql)
    con.commit()
    Data.closecur(cur)
    Data.closeconnet(con)
    return 

#产品数据库写入
def InsertIntoProduct(tablename,oData):
    con=Data.connetDB("sys.db")
    cur=Data.getcur(con)
    if tablename=="Product":
        sql1="insert into "+tablename+" (id,name,code,ishape,thickness,apptyle,wanqu,kongnum,prtkong20,midulinjie20,miduchongzhuang20,a,caoa,chongqiqianga,allowmaxa,aloowmaxp,chongzhuangdn,chongzhuangup) VALUES"
        for item in oData:
            sql2=""
            sql2="("+str(item["id"])+","+"'"+str(item["name"])+"'"+",'"+str(item["code"])+"','"+str(item["ishape"])+"',"+str(item["thickness"])+","+"'"+str(item["apptyle"])+"'"+","+"'"+str(item["wanqu"])+"'"+","+"'"+str(item["kongnum"])+"'"+","+str(item["prtkong20"])+","+str(item["midulinjie20"])+","+str(item["miduchongzhuang20"])+","+str(item["a"])+","+str(item["caoa"])+","+str(item["chongqiqianga"])+","+str(item["allowmaxa"])+","+str(item["allowmaxp"])+","+str(item["chongzhuangdn"])+","+str(item["chongzhuangup"])+");"
            cur.execute(sql1+sql2)
            con.commit()
    elif tablename=="Density":
        sql1="insert into "+tablename+" (id,temperature,liquiddensity,vapordensity) VALUES"
        for item2 in oData:
            sql2=""
            sql2="("+str(item2["id"])+","+str(item2["temperature"])+","+str(item2["liquiddensity"])+","+str(item2["vapordensity"])+");"
            print(sql1+sql2)
            cur.execute(sql1+sql2)
            con.commit()
    Data.closecur(cur)
    Data.closeconnet(con)




#从数据库获取产品信息 将从数据库获取的产品信息转换成数组
def analysisData(oData):
    Product=[]
    for i in oData:
        item={}
        item["id"]=i[0]#id
        item["name"]=i[1]#产品名称
        item["code"]=i[2]#产品代号
        item["ishape"]=i[3]#截面形状
        item["thickness"]=i[4]#厚度
        item["apptyle"]=i[5]#应用方式 
        item["wanqu"]=i[6]#弯曲情况
        item["kongnum"]=i[7]#孔数
        item["prtkong20"]=i[8]#20℃单孔最大传热能力
        item["midulinjie20"]=i[9]#20℃临界热流密度
        item["miduchongzhuang20"]=i[10]#20℃工况充装时热管线性密度
        item["a"]=i[11]#截面总面积
        item["caoa"]=i[12]#槽道面积
        item["chongqiqianga"]=i[13]#蒸汽腔面积
        item["allowmaxa"]=i[14]#允许最大回退面积
        item["allowmaxp"]=i[15]#最大回退百分比
        item["chongzhuangdn"]=i[16]#充装下限
        item["chongzhuangup"]=i[17]#充装上限
        Product.append(item)
    return Product
#通过id获取产品信息
def GetProductInfoById(id,oData):
    for item in oData:
        if id==item["id"]:
            return item
        else:
            pass
    return {}

#通过code获取产品星系
def GetProductInfoByCode(Code,oData):
    for item in oData:
        if Code==item["code"]:
            return item
        else:
            pass
    return {}

#从数据库获取密度信息 
def GetDensityInfo():
    con=Data.connetDB("sys.db")
    cur=Data.getcur(con)
    data=Data.GetAll(cur,"Density")
    Densitylist=analysisDensityData(data)
    Data.closecur(cur)
    Data.closeconnet(con)
    return Densitylist

#解析密度信息
def analysisDensityData(oData):
    Density=[]
    for i in oData:
        item={}
        item["id"]=i[0]
        item["temperature"]=i[1]
        item["liquiddensity"]=i[2]
        item["vapordensity"]=i[3]
        Density.append(item)
    return Density

#通过温度获取液体密度
def GetLiquiddensityByTemp(temp,Density):
    for item in Density:
        if abs(temp-item["temperature"])<1e-6:
            return item["liquiddensity"]
        else:
            pass
    #温度不在数据库序列内 返回-999999
    return -9999999

#通过温度获取气体密度
def GetVapordensityByTemp(temp,Density):
    for item in Density:
        if abs(temp-item["temperature"])<1e-6:
            return item["vapordensity"]
        else:
            pass
    #温度不在数据库序列内 返回-999999
    return -9999999

#根据选型参数计算产品表格中的液塞
def CalYeSaiByid(odata,productid,lenght,lenght1):
    if len(odata)<1:
        return ""
    else:
        dicshaixuanInfo=eval(odata)
        hightemp=float(dicshaixuanInfo["hightemp"]) 
        lowtemp=float(dicshaixuanInfo["lowtemp"])
        chongzhuangtemp=float(dicshaixuanInfo["chongzhuangtemp"])
        # chongzhaungtemp=float(dicshaixuanInfo["chongzhuangtemp"])
        productlist=GetProductInfo()
        productinfo=GetProductInfoById(productid,productlist)
        Densitylist=GetDensityInfo()
        p1=GetLiquiddensityByTemp(chongzhuangtemp,Densitylist)
        Sc=float(productinfo["caoa"])
        p2=GetVapordensityByTemp(chongzhuangtemp,Densitylist)
        sq=float(productinfo["chongqiqianga"])
        lim_dn=float(productinfo["chongzhuangdn"])
        lim_up=float(productinfo["chongzhuangup"])
        p3_high=GetLiquiddensityByTemp(hightemp,Densitylist)
        p4_high=GetVapordensityByTemp(hightemp,Densitylist)
        p3_low=GetLiquiddensityByTemp(lowtemp,Densitylist)
        p4_low=GetVapordensityByTemp(lowtemp,Densitylist)
        # 高温 充装上限
        le_1=data_hp(p1,Sc,p2,sq,lim_up,p3_high,p4_high)
        # 高温 充装下限
        le_2=data_hp(p1,Sc,p2,sq,lim_dn,p3_high,p4_high)
        # 低温 充装上限
        le_3=data_hp(p1,Sc,p2,sq,lim_up,p3_low,p4_low)
        # 低温 充装下限
        le_4=data_hp(p1,Sc,p2,sq,lim_dn,p3_low,p4_low)
        d=productinfo["allowmaxp"]
        #低温对应的充装下限满足不失效
        if le_4-d>1e-6:
            if le_1*lenght>lenght1:
                return str(round(le_1*lenght,2))+"突显"
            else:
                return str(round(le_1*lenght,2))
        #低温对应的充装下限满足失效
        else:
            return "失效"
        
#     #p1:充装温度对应的液体密度
#     #Sc：槽道面积
#     #p2：充装温度对应的气体密度
#     #sq：蒸气腔面积
#     #lim_l：充装量下\上限
#     #p3：低\高温对应的液体密度
#     #p4：低\高温对应的气体密度
def data_hp(p1,sc,p2,sq,lim_l,p3,p4):
    le_l=(((p1*sc+p2*sq)*lim_l)-(p3*sc+p4*sq))/p3/sq
    return le_l

def disp(jl,jh,d,lenght,lenght1):
    if jl>d:
        l=jh*lenght
        if l>lenght1:
            return str(round(l,2))#"液塞长度为"+str(round(l,2))+"mm,超过液塞容差，需要调整充装温度或是液塞容差"
        else:
            return str(round(l,2))#"液塞长度为"+str(round(l,2))+"mm,在液塞容差范围内"
    else:
        return "失效"#"在此充装温度下，低温热管失效，请调整充装温度"

#
# def disp(jl,jh,d,lenght,lenght1):

#     if jl>d:
#         l=jh*lenght
#         if l>=lenght1:
#             print('液塞长度为%.2fmm,超过液塞容差，需要调整充装温度或是液塞容差'%(l))
#         else:
#             print('液塞长度为%.2fmm,在液塞容差范围内'%(l))
#         
#     else:
#         print('在此充装温度下，低温热管失效，请调整充装温度')

#根据参数对产品表排序 selectData:控制信息 ProductData：产品信息
def sortProductList(selectData,ProductData):
    if len(selectData)<1:
        return []
    suitablelist=[]
    unsuitablelist=[]
    dicselectData=eval(selectData)

    for item in ProductData:
        #校核功率
        if item['prtkong20']-CalTotalgonglv(selectData)<1e-6:
            unsuitablelist.append(item)
            continue
        #校核热流密度
        if float(dicselectData['reliumidu'])-item["midulinjie20"]>1e-6:
            unsuitablelist.append(item)
            # print('reliumidu',item["id"])
            continue
        #校核重量
        if item['midulinjie20']*GetL(selectData)-float(dicselectData["weight"])>1e-6:
            unsuitablelist.append(item)
            # print('midulinjie20',item["id"])
            # print(item['midulinjie20']*GetL(selectData),dicselectData["weight"])
            continue
        #校核应用方式
        if dicselectData["type"] not in item['apptyle']:
            unsuitablelist.append(item)
            # print('type',item["id"])
            continue
        #校核弯曲
        if (dicselectData["wanqunum"]<1 and item['wanqu']=="可弯曲") or (dicselectData["wanqunum"]>0 and ("不可弯曲" in item['wanqu']) ):
            unsuitablelist.append(item)
            # print('wanqunum',item["id"])
            continue
        #校核液塞
        if ("失效" in CalYeSai(selectData,item['id'])) or ("突显" in CalYeSai(selectData,item['id'])):
            unsuitablelist.append(item)
            # print('CalYeSai',item["id"])
            continue
        suitablelist.append(item)
    return suitablelist+unsuitablelist

#     1功率，如果热管的本身的功率小于需求值就突出显示。
# 2热流密度，如果本身的热流密度小于需求值就突出显示。
# 3重量，如果重量大于需求值就突出显示
# 4应用方式：如果需要的应用方式不在热管允许应用范围内就突出显示
# 5弯曲，如果热管需要弯曲，那么不能弯曲的热管就突出显示
# 6液塞，如果计算的液塞大于液塞容差就突出显示


 #获取热管总长
def GetL(shaixuanInfo):
    if len(shaixuanInfo)==0:
        return 0.0
    else:
        dicshaixuanInfo=eval(shaixuanInfo)
        lis=[]
        for item in dicshaixuanInfo["tabledata"]:
            lis.append(item["juli"])
        l=max(lis)
        l=l+GetRongCha(shaixuanInfo)
        return l
    #获取液塞容差
def GetRongCha(shaixuanInfo):
    if len(shaixuanInfo)==0:
        return 0.0
    else:
        dicshaixuanInfo=eval(shaixuanInfo)
        return float(dicshaixuanInfo["rongcha"])

#计算液赛长度
def CalYeSai(shaixuanInfo,productid):
    lenght=GetL(shaixuanInfo)
    lenght1=GetRongCha(shaixuanInfo)
    result=CalYeSaiByid(shaixuanInfo,productid,lenght,lenght1)
    return result

#计算需求总功率
def CalTotalgonglv(shaixuanInfo):
    if len(shaixuanInfo)<1:
        return 0
    dicshaixuanInfo=eval(shaixuanInfo)
    if len(dicshaixuanInfo["tabledata"])==0:
        return 0
    reyuangonglv=0
    for  item in dicshaixuanInfo["tabledata"]:
        reyuangonglv=reyuangonglv+item["gonglv"]*item["juli"]
    if dicshaixuanInfo["wanqunum"]==0:
        return reyuangonglv*1e-3
    else:
        return reyuangonglv*(1+dicshaixuanInfo["wanqunum"]*0.1)*1e-3

#产品校核
def GetCheckData(oPara):
    res={}
    Productlist=GetProductInfo()
    product=GetProductInfoByCode(oPara["code"],Productlist)
    Density=GetDensityInfo()
    Vyeti_CaoDao=float(product["caoa"])*float(oPara["realL"])
    Vqiti=float(product["chongqiqianga"])*float(oPara["realL"])
    #计算高温液赛长度
    yesail_Up=0.0
    yesail_eDing=0.0
    yesail_dn=0.0
    print("------------------------------------------计算校核---------------------------------------")
    Vyeti_Up=float(oPara["realQ"])/GetLiquiddensityByTemp(float(oPara["tempup"]),Density)
    print("高温工况实际充装量：",float(oPara["realQ"]))
    print("高温工况液体密度：",GetLiquiddensityByTemp(float(oPara["tempup"]),Density))
    print("高温工况液体体积：",Vyeti_Up)
    print("高温工况槽道体积：",Vyeti_CaoDao)
    print("高温工况气腔体积：",Vqiti)
    # Vyeti_CaoDao=float(product["caoa"])*float(oPara["realL"])
    # Vqiti=float(product["chongqiqianga"])*float(oPara["realL"])
    if Vyeti_Up-Vyeti_CaoDao>1e-6:
        yesail_Up=(Vyeti_Up-Vyeti_CaoDao)/float(product["chongqiqianga"])
        print("高温工况液赛长度：",yesail_Up)
    else:
        yesail_Up=(Vyeti_Up-Vyeti_CaoDao)/float(product["caoa"])
        print("高温工况液赛长度：",yesail_Up)
    #计算额定温度液赛长度
    print("额定工况实际充装量：",float(oPara["realQ"]))
    print("额定工况液体密度：",GetLiquiddensityByTemp(float(oPara["tempeding"]),Density))
    print("额定工况液体体积：",Vyeti_Up)
    print("额定工况槽道体积：",Vyeti_CaoDao)
    print("额定工况气腔体积：",Vqiti)
    yesail_eDing=0.0
    Vyeti_eDing=float(oPara["realQ"])/GetLiquiddensityByTemp(float(oPara["tempeding"]),Density)
    # Vyeti_CaoDao=float(product["caoa"])*float(oPara["realL"])
    # Vqiti=float(product["chongqiqianga"])*float(oPara["realL"])
    if Vyeti_eDing-Vyeti_CaoDao>1e-6:
        yesail_eDing=(Vyeti_eDing-Vyeti_CaoDao)/float(product["chongqiqianga"])
        print("额定工况液赛长度：",yesail_Up)
    else:
        yesail_eDing=(Vyeti_eDing-Vyeti_CaoDao)/float(product["caoa"])
        print("额定工况液赛长度：",yesail_Up)
    #计算低温度液赛长度
    print("低温工况实际充装量：",float(oPara["realQ"]))
    print("低温工况液体密度：",GetLiquiddensityByTemp(float(oPara["tempdn"]),Density))
    print("低温工况液体体积：",Vyeti_Up)
    print("低温工况槽道体积：",Vyeti_CaoDao)
    print("低温工况气腔体积：",Vqiti)
    yesail_dn=0.0
    Vyeti_dn=float(oPara["realQ"])/GetLiquiddensityByTemp(float(oPara["tempdn"]),Density)
    # Vyeti_CaoDao=float(product["caoa"])*float(oPara["realL"])
    # Vqiti=float(product["chongqiqianga"])*float(oPara["realL"])
    if Vyeti_eDing-Vyeti_CaoDao>1e-6:
        yesail_dn=(Vyeti_dn-Vyeti_CaoDao)/float(product["chongqiqianga"])
        print("低温工况液赛长度：",yesail_Up)
    else:
        yesail_dn=(Vyeti_dn-Vyeti_CaoDao)/float(product["caoa"])
        print("低温工况液赛长度：",yesail_Up)
    res["code"]=oPara["code"]
    res["name"]=oPara["name"]
    res["tempdn"]=oPara["tempdn"]
    res["yesaidn"]=str(round(yesail_dn,2))
    res["tempup"]=oPara["tempup"]
    res["yesaiup"]=str(round(yesail_Up,2))
    res["tempeding"]=oPara["tempeding"]
    res["yesaieding"]=str(round(yesail_eDing,2))
    return res
    































































































