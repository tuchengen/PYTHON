import math


def Pressure(T):
    if T <= 195.5:
        return 0.0
    else:
        return 0.0000016821 * math.pow(T, 3) - 0.0011231072 * math.pow(T, 2) + 0.2526437188 * T - 19.080838


def Temperature(P):
    if P > 0.42938:
        return -0.01544047 * math.pow(P, 6) + 0.35101172 * math.pow(P, 5) - 3.23179387 * math.pow(P, 4) + 15.62331157 * math.pow(P, 3) - 43.87353857 * math.pow(P, 2) + 85.21543622 * P + 243.99113264
    else:
        return -427466.3607 * math.pow(P, 6) + 608580.98877 * math.pow(P, 5) - 339795.45531 * math.pow(P, 4) + 94753.67528 * math.pow(P, 3) - 14112.16472 * math.pow(P, 2) + 1231.29066 * P + 191.05927

#页面1的计算公式
def CalRC(A,B,C,D,E):
    #传入参数有误时，返回-999999999999999
    if C==0 or D==0 or E==0:
        return math.nan
    if (Pressure(A)-Pressure(D))/D-(Pressure(B)-Pressure(E))/E==0:
        return math.nan
    partA=(Pressure(B)-Pressure(C))/C
    partB=(Pressure(A)-Pressure(D))/D-(Pressure(B)-Pressure(E))/E
    return partA/partB

#页面2的计算公式
def CalQ(F,G,H,K,M,N):
    partA=M*(Pressure(H)-Pressure(G))
    if F==0 or partA==0:
        return math.nan
    partB=K-M*(Pressure(H)-Pressure(F))/F
    return 1-N*G*partB/partA

#页面3的计算公式
def Calh(F,G,K,M,N,Q):
    partA=N*K*G*F+N*M*G*Pressure(F)+F*M*(1-Q)*Pressure(G)
    partB=M*N*G+F*M*(1-Q)
    if partB==0:
        return math.nan
    return KToC(Temperature(partA/partB))

#摄氏度转华氏度
def CToK(value):
    return value+273.15

#华氏度转摄氏度
def KToC(value):
    return value-273.15

    
