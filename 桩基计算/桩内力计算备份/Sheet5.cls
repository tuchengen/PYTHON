VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet5"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Private Sub CommandButton1_Click()
ff = ClearB37G105()
'Worksheets("低桩承台桩内力计 算").Range("C37").Value = 8989
n = Range("D25")
s = Range("D26")
'MsgBox ActiveSheet.Cells(1, 1)
ix = Math.Sqr(n)
If ix = Int(ix) Then
irow = 37
For i = 1 To Range("D25")
ActiveSheet.Cells(irow + i - 1, 10) = 1
Next i
Do While BStop() = 0
f = opop(ix, s)
f2 = GetN()
f3 = GetH()
f4 = GetM()
f5 = GetiFlg()
Loop
Else
MsgBox "桩数目不能按照n * n排布"
Exit Sub
End If
End Sub


Private Function opop(ix, s)
irow = 37
For i = 1 To ix * ix
ActiveSheet.Cells(irow + i - 1, 2).Value = i
Next i
For j = 1 To ix
For n = 1 To ix
r = irow + (j - 1) * ix + n - 1
Valx = 0.5 * (ix - 1) * s - (j - 1) * s
Valy = 0.5 * (ix - 1) * s - (n - 1) * s
ActiveSheet.Cells(r, 3).Value = Valx
ActiveSheet.Cells(r, 4).Value = Valy
ActiveSheet.Cells(r, 5) = ActiveSheet.Cells(r, 10)
ActiveSheet.Cells(r, 6).Value = GetRnn(ActiveSheet.Cells(r, 5))
Next n
Next j
ff2 = GetrVV()
ff3 = GetrUV()
ff4 = GetrUU()
ff5 = GetrBU()
ff6 = GetrUB()
ff7 = GetrBB()
ff8 = GetV()
ff9 = GetU()
ff10 = GetB()
End Function

Private Function ClearB37G105()
For i = 37 To 105
For j = 2 To 10
ActiveSheet.Cells(i, j).Value = ""
Next j
Next i
End Function

Private Function GetRnn(iflg)
If iflg = 1 Then
GetRnn = 1 / (0.85 * Range("S37") * Range("D18") / (Range("S39")) + 1 / (Range("S38") * Range("S19")))
Else
GetRnn = (Range("S39") / (0.85 * Range("S37") * Range("D18")))
End If
End Function


Private Function GetrVV()
irow = 37
rVV = 0
For i = 1 To Range("D25")
rVV = rVV + ActiveSheet.Cells(irow + i - 1, 6).Value
Next i
rVV = rVV + Range("S47") * Range("S53") * 1000
ActiveSheet.Cells(54, 21).Value = rVV
End Function

Private Function GetrUV()
rUV = Range("D12") * Range("S47") * Range("S53") * 1000
ActiveSheet.Cells(55, 21).Value = rUV
End Function

Private Function GetrUU()
ActiveSheet.Cells(56, 21).Value = Range("S45") * Range("S48") + Range("D25") * Range("S41")
End Function

Private Function GetrBU()
ActiveSheet.Cells(57, 21).Value = Range("U61") * Range("S49") - Range("D25") * Range("S42")
End Function

Private Function GetrBB()
irow = 37
rBB = 0
For i = 1 To Range("D25")
rBB = rBB + ActiveSheet.Cells(irow + i - 1, 6).Value * ActiveSheet.Cells(irow + i - 1, 3).Value * ActiveSheet.Cells(irow + i - 1, 3).Value
Next i
rBB = rBB + Range("D25") * Range("S44") + Range("S47") * Range("S52")
ActiveSheet.Cells(59, 21).Value = rBB
End Function
Private Function GetN()
irow = 37
For i = 1 To Range("D25")
ActiveSheet.Cells(irow + i - 1, 7).Value = (Range("U60") + Range("U62") * ActiveSheet.Cells(irow + i - 1, 3)) * ActiveSheet.Cells(irow + i - 1, 6)
Next i
End Function
Private Function GetH()
irow = 37
For i = 1 To Range("D25")
ActiveSheet.Cells(irow + i - 1, 8).Value = Range("U61") * Range("S41") - Range("U62") * Range("S43")
Next i
End Function
Private Function GetM()
irow = 37
For i = 1 To Range("D25")
ActiveSheet.Cells(irow + i - 1, 9).Value = Range("U62") * Range("S44") - Range("U61") * Range("S42")
Next i
End Function
Private Function GetiFlg()
irow = 37
For i = 1 To Range("D25")
ActiveSheet.Cells(irow + i - 1, 10).Value = IIf(ActiveSheet.Cells(irow + i - 1, 7) > 0, 1, -1)
Next i
End Function
Private Function GetrUB()
ActiveSheet.Cells(58, 21).Value = Range("S45") * Range("S49") - Range("D25") * Range("S42")
End Function
Private Function GetV()
ActiveSheet.Cells(60, 21).Value = Range("L8") / Range("U54")
End Function
Private Function GetU()
ActiveSheet.Cells(61, 21).Value = (Range("U59") * Range("L9") - Range("U58") * Range("L10")) / (Range("U56") * Range("U59") - Range("U58") * Range("U58")) - (Range("L8") * Range("U55") * Range("U59")) / (Range("U54") * (Range("U56") * Range("U59") - Range("U58") * Range("U58")))
End Function
Private Function GetB()
ActiveSheet.Cells(62, 21).Value = (Range("U56") * Range("L10") - Range("U58") * Range("L9")) / (Range("U56") * Range("U59") - Range("U58") * Range("U58")) - (Range("L8") * Range("U55") * Range("U58")) / (Range("U54") * (Range("U56") * Range("U59") - Range("U58") * Range("U58")))
End Function
Private Function BStop()
irow = 37
For i = 1 To Range("D25")
If ActiveSheet.Cells(irow + i - 1, 10) <> ActiveSheet.Cells(irow + i - 1, 5) Then
BStop = 0
Exit Function
End If
Next i
BStop = 1
End Function




