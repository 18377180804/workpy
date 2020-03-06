# !/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import xlrd
import os
import re

inputfiname=sys.argv[6]
#设置文件路径
bait_type_path = os.path.dirname(__file__)
fname1=xlrd.open_workbook(os.path.join(bait_type_path, inputfiname),'r')
fname2=open(os.path.join(bait_type_path, "condition.txt"),'r',encoding='utf-8')
RE_CHINESE = re.compile(r'^[\u4e00-\u9fa5\u36c3\u4DAE][\u4e00-\u9fa5·\u36c3\u4DAE]{0,30}[\u4e00-\u9fa5\u36c3\u4DAE]$')
ER_SHA256 = re.compile(r'^([0-9a-fA-F]){64}$')
ER_MD5 = re.compile(r'^([0-9a-fA-F]){32}$')




# fname1=xlrd.open_workbook('D:\\桌面\\check\\filterExcel\\excelDate.xlsx','r')
# fname2=open('D:\\桌面\\check\\filterExcel\\condition.txt','r',encoding='utf-8')

# 获取当前文件的表格
sheets=fname1.nsheets
print('sheets-----',sheets)

sheet2=fname1.sheet_by_index(0)  #获取表对象
print('sheet2---',sheet2)

#获取行数
nrows = sheet2.nrows
# 获取列数
ncols = sheet2.ncols
# 获取某一行的数据
sheet_rows=sheet2.row_values(1)
# 获取第一行 1-2列的数据
sheet_rowss=sheet2.row_values(1,1,3)
# 获取第1行第0列的数据
sheet_cells=sheet2.cell_value(1,0)
###除了cell值内容外还有附加属性，如：text:"字段名"
sheet_cell=sheet2.cell(1,0)
#获取第一列，第二行以下的数据
sheet_cols=sheet2.col_values(1,2)
# 获取第一列，第二至第四行的数据
sheet_cols1=sheet2.col_values(1,2,5)

def is_chinese(uchar):
    a=RE_CHINESE.match(uchar)
    return RE_CHINESE.match(uchar)

def mobile_pid(uchar,type):
    if type==2 or type==4:
        return ER_SHA256.match(uchar) and len(uchar)==64
    elif type ==3:
        return ER_MD5.match(uchar) and len(uchar)==32
    else:
        return False



# 获取各行的数据
hang=int(sys.argv[1])-1
j=int(sys.argv[2])-1
inputname=int(sys.argv[3])-1
inputpid=int(sys.argv[4])-1
inputmobile=int(sys.argv[5])-1
# hang=6-1
# j=2-1
# inputname=2-1
# inputpid=3-1
# inputmobile=4-1
sheet_rowslist=[]
encryptType=2
for i in range(hang,nrows):
    sheet_rowslist.append(sheet2.row_values(i,j))

    rows_list=sheet2.row_values(i,j)
    if ''.__eq__(str(rows_list[inputname-j])) or is_chinese(str(rows_list[inputname-j]))==None or is_chinese(str(rows_list[inputname-j]))==False:
        print(i+1,'行姓名为空 或中文名字不合法' )
    if ''.__eq__(str(rows_list[inputpid-j])) or mobile_pid(str(rows_list[inputpid-j]),encryptType)!=True :
        print(i+1,'行身份证为空 或身份证密文格式错误')
    if ''.__eq__(str(rows_list[inputmobile-j])) or mobile_pid(rows_list[inputmobile-j],encryptType)!=True :
        print(i+1,'行手机号码为空 手机密文格式错误')

