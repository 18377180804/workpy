#-*- encoding:utf-8 -*-
import os
import sys
import json
import codecs
import xlrd

xlrd.Book.encoding = "gbk"
# 确定运行环境的encoding
inputname="标签测试数据zzc_20191217.xlsx"
outputname="标签测试数据zzc_20191217.json"
data = xlrd.open_workbook("D:/桌面/check/exceltojson/"+inputname)
file = codecs.open("D:/桌面/check/exceltojson/"+outputname, "w", 'utf-8')

# inputname=sys.argv[1]
# outputname=sys.argv[2]
# bait_type_path = os.path.dirname(__file__)
# data=xlrd.open_workbook(os.path.join(bait_type_path, inputname),'r')
# file=open(os.path.join(bait_type_path, outputname),'w',encoding='utf-8')

def _tongjiFirstRow(inputname,outputname):
    xlrd.Book.encoding = "gbk"
tagtile = ['#loanApplyInfo', '#singleLoanAccountInfo', '#singleLoanRepayInfo', '#singleLoanDelayInfo',
             '#loopLoanAccountInfo', '#loopLoanBillInfo', '#loopLoanBillRepayInfo', '#loopLoanReceiptInfo',
             '#loopLoanReceiptRepayInfo']
for sheetindex in range(0, len(data.sheets())):
  tblTDLYMJANQSXZB = data.sheets()[sheetindex]
  sheetname = data.sheet_by_index(sheetindex).name
  file.writelines(tagtile[sheetindex]+"\n")

  #找到有几列几列
  nrows = tblTDLYMJANQSXZB.nrows #行数
  ncols = tblTDLYMJANQSXZB.ncols #列数
  arr=[]
  startcell = 1
  if ('D3'.__eq__(sheetname) or 'D4'.__eq__(sheetname)):
    startcell == 0
  for i in range(startcell,ncols):
    arr.append(tblTDLYMJANQSXZB.cell(1,i).value)
  #end for
  for rowindex in range(2,nrows):
    dic={}
    for colindex in range(startcell,ncols):
     s=tblTDLYMJANQSXZB.cell(rowindex,colindex).value
     ctype=tblTDLYMJANQSXZB.cell(rowindex,colindex).ctype
     if ctype==2:
         s=int(s)
     dic[arr[colindex-1]]=s
    #end for
    dicarry=json.dumps(dic,ensure_ascii=False)
    file.writelines(dicarry+"\n")



#end
_tongjiFirstRow(inputname,outputname)
print("export OK")