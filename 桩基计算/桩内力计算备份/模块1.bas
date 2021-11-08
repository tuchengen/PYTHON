Attribute VB_Name = "模块1"
Function GetInsertValue(ParamArray inputdata())
GetInsertValue = -99999999
Dim Mydata1, Mydata2
Mydata1 = Application.WorksheetFunction.Transpose(inputdata(1))
Mydata2 = Application.WorksheetFunction.Transpose(inputdata(2))
'MsgBox "共有" & UBound(Mydata1) & "个数据！"
If inputdata(0) <= Mydata1(1) Then
GetInsertValue = Mydata2(1)
ElseIf inputdata(0) >= Mydata1(UBound(Mydata1)) Then
GetInsertValue = Mydata2(UBound(Mydata1))
Else
For i = 1 To UBound(Mydata1) - 1
If inputdata(0) > Mydata1(i) And inputdata(0) > Mydata1(i + 1) Then
Dim a, b, c, d
a = Mydata1(i)
b = Mydata1(i + 1)
c = Mydata1(i)
d = Mydata2(i + 1)
GetInsertValue = (d - c) * (inputdata(0) - a) / (b - a) + c
End If
Exit For
Next i
End If
End Function

Function GetKh(ParamArray inputdata())
ah = CDbl(inputdata(0))
tpype = CStr(inputdata(1))
C0 = CDbl(inputdata(2))
I0 = CDbl(inputdata(3))
a = CDbl(inputdata(4))
ei = CDbl(inputdata(5))
If tpype = "非岩石类土中" Then
If ah < 2.5 Then
GetKh = C0 * I0 / a * ei
Else
GetKh = 0
End If
End If
If tpype = "基岩石表面" Then
If ah < 3.5 Then
GetKh = C0 * I0 / a * ei
Else
GetKh = 0
End If
End If
If tpype = "嵌固岩层" Then
GetKh = 0
End If
End Function

Function GetKx2(ParamArray inputdata())
Dim pp As Range
GetKx2 = 0
For Each pp In inputdata(0)
GetKx2 = GetKx2 + CDbl(pp) * CDbl(pp)
Next pp
End Function
