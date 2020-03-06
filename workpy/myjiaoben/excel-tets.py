#-*- encoding:utf-8 -*-
import sys
import locale
import os.path
import os
import time
import shutil
import datetime
import types
import sqlite3
import pypyodbc
import traceback
import json
import codecs
import xlrd
import xlwt
# from xlutils.copy import copy
# 确定运行环境的encoding
inputname=sys.argv[1]
outputname=sys.argv[2]
__g_codeset = sys.getdefaultencoding()
if "ascii"==__g_codeset:
  __g_codeset = locale.getdefaultlocale()[1]
#
def object2double(obj):
  if(obj==None or obj==""):
    return 0
  else:
    return float(obj)
  #end if
#
def utf8_to_mbs(s):
  return s.decode("utf-8").encode(__g_codeset)
#
def mbs_to_utf8(s):
  return s.decode(__g_codeset).encode("utf-8")
#
def _tongjiFirstRow(inputname,outputname):
  #xlrd.Book.encoding = "gbk"
  data = xlrd.open_workbook("D:/桌面/check/exceltojson/",inputname,formatting_info=True)
  file = codecs.open("D:/桌面/check/exceltojson/",outputname, "w", 'utf-8')
  tblTDLYMJANQSXZB = data.sheets()[0]
  #找到有几列几列
  nrows = tblTDLYMJANQSXZB.nrows #行数
  ncols = tblTDLYMJANQSXZB.ncols #列数
  totalArray=[]
  arr=[]
  for i in range(0,ncols):
    arr.append(tblTDLYMJANQSXZB.cell(0,i).value)
  #end for
  for rowindex in range(1,nrows):
    dic={}
    for colindex in range(0,ncols):
     s=tblTDLYMJANQSXZB.cell(rowindex,colindex).value
     dic[arr[colindex]]=s
    #end for
    dicarry=json.dumps(dic,ensure_ascii=False)
    file.writelines(dicarry+"\n")
    totalArray.append(dic)



#end
_tongjiFirstRow(inputname,outputname)
print("export OK")